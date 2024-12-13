from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from database.models import ClosetInfo, ClothingItem, ClosetStatus, OutfitInfo
from django.contrib.messages.storage.base import Message
import json
from django.http import JsonResponse

@login_required
def register_closet(request):
    if request.method == "POST":
        try:
            # Create new closet instance
            new_closet = ClosetInfo(
                user=request.user,
                closet_name=request.POST['closet_name'],
                closet_type=request.POST['closet_type'],
                closet_location=request.POST['closet_location'],
                closet_size=request.POST['closet_size'],
                closet_color=request.POST['closet_color']
            )
            new_closet.save()
            
            messages.success(request, "Closet registered successfully!")
            return redirect('homepage')
        
        except Exception as e:
            messages.error(request, f"Error registering closet: {str(e)}")
            return render(request, 'ClosetPages/RegisterCloset.html')
    
    return render(request, 'ClosetPages/RegisterCloset.html')

@login_required
def register_clothing(request):
    # Clear any existing messages when first loading the page
    storage = messages.get_messages(request)
    storage.used = True
    
    # Get user's closets for the dropdown
    user_closets = ClosetInfo.objects.filter(user=request.user)
    
    if request.method == "POST":
        try:
            # Create new clothing item (removed file_path)
            new_clothing = ClothingItem(
                user=request.user,
                clothing_item_name=request.POST['clothing_name']
            )
            new_clothing.save()
            
            # Create closet status entry
            closet = ClosetInfo.objects.get(closet_id=request.POST['closet_id'])
            status = ClosetStatus(
                user=request.user,
                closet=closet,
                clothing_item=new_clothing,
                hanger_number=request.POST['hanger_number'],
                status=True
            )
            status.save()
            
            messages.success(request, "Clothing item registered successfully!")
            return render(request, 'ClosetPages/RegisterClothing.html', {'closets': user_closets})
        
        except Exception as e:
            messages.error(request, f"Error registering clothing: {str(e)}")
            return render(request, 'ClosetPages/RegisterClothing.html', {'closets': user_closets})
    
    return render(request, 'ClosetPages/RegisterClothing.html', {'closets': user_closets})

@login_required
def fits(request):
    # Get user's closets for the dropdown
    user_closets = ClosetInfo.objects.filter(user=request.user)
    return render(request, 'ClosetPages/fits.html', {'closets': user_closets})

@login_required
def get_outfits(request, closet_id):
    try:
        # Get the selected closet
        closet = ClosetInfo.objects.get(closet_id=closet_id, user=request.user)
        
        # Get all clothing items that are marked as out of the closet (picked out)
        picked_items = ClosetStatus.objects.filter(
            user=request.user,
            closet=closet,
            in_closet=False
        ).values_list('clothing_item_id', flat=True)
        
        if picked_items:
            # Get all outfits that contain ANY of the picked items
            potential_outfits = OutfitInfo.objects.filter(
                user=request.user,
                clothing_items__clothing_item_id__in=picked_items
            ).distinct()
            
            # Filter outfits to only include those that contain ALL picked items
            available_outfits = []
            for outfit in potential_outfits:
                outfit_items = outfit.clothing_items.values_list('clothing_item_id', flat=True)
                if all(item_id in outfit_items for item_id in picked_items):
                    available_outfits.append(outfit)
            
            # Get remaining outfits (those that don't contain all picked items)
            affected_outfits = potential_outfits.exclude(outfit_id__in=[o.outfit_id for o in available_outfits])
        else:
            # If no items are picked out, show all outfits as available
            available_outfits = OutfitInfo.objects.filter(user=request.user)
            affected_outfits = []
        
        # Store the current state in the session
        current_state = ClosetStatus.objects.filter(
            user=request.user,
            closet=closet
        ).values_list('clothing_item_id', 'in_closet')
        request.session[f'closet_state_{closet_id}'] = json.dumps(list(current_state))
        
        context = {
            'closet': closet,
            'available_outfits': available_outfits,
            'affected_outfits': affected_outfits,
            'closets': ClosetInfo.objects.filter(user=request.user),
            'picked_items': ClothingItem.objects.filter(clothing_item_id__in=picked_items)
        }
        
        return render(request, 'ClosetPages/fits.html', context)
        
    except ClosetInfo.DoesNotExist:
        messages.error(request, "Closet not found")
        return redirect('Fits')

@login_required
def register_outfit(request):
    # Clear any existing messages
    storage = messages.get_messages(request)
    storage.used = True
    
    # Get user's clothing items for the multi-select
    user_clothing = ClothingItem.objects.filter(user=request.user)
    
    if request.method == "POST":
        try:
            # Handle the uploaded file
            outfit_pic = request.FILES.get('outfit_pic')
            
            # Create new outfit
            new_outfit = OutfitInfo(
                user=request.user,
                outfit_name=request.POST['outfit_name'],
                outfit_pic_file_path=outfit_pic
            )
            new_outfit.save()
            
            # Add selected clothing items to the outfit
            selected_items = request.POST.getlist('clothing_items')
            for item_id in selected_items:
                clothing_item = ClothingItem.objects.get(clothing_item_id=item_id)
                new_outfit.clothing_items.add(clothing_item)
            
            messages.success(request, "Outfit registered successfully!")
            return render(request, 'ClosetPages/RegisterOutfit.html', {'clothing_items': user_clothing})
        
        except Exception as e:
            messages.error(request, f"Error registering outfit: {str(e)}")
            return render(request, 'ClosetPages/RegisterOutfit.html', {'clothing_items': user_clothing})
    
    return render(request, 'ClosetPages/RegisterOutfit.html', {'clothing_items': user_clothing})

@login_required
def check_updates(request, closet_id):
    try:
        # Get the current state of items in the closet
        current_state = ClosetStatus.objects.filter(
            user=request.user,
            closet_id=closet_id
        ).values_list('clothing_item_id', 'in_closet')
        
        # Convert to a string for comparison
        current_state_str = json.dumps(list(current_state))
        
        # Get the last known state from the session
        last_state = request.session.get(f'closet_state_{closet_id}')
        
        if last_state != current_state_str:
            # State has changed, update the session and notify client
            request.session[f'closet_state_{closet_id}'] = current_state_str
            return JsonResponse({'updated': True})
        
        return JsonResponse({'updated': False})
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
from django.db import models
from django.contrib.auth.models import User

class ClosetInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    closet_id = models.AutoField(primary_key=True)
    closet_name = models.CharField(max_length=255)
    closet_type = models.CharField(max_length=255)
    closet_location = models.CharField(max_length=255)
    closet_size = models.CharField(max_length=255)
    closet_color = models.CharField(max_length=255)

    class Meta:
        db_table = 'closet_info'
        unique_together = (('user', 'closet_id'),)

    def __str__(self):
        return f"{self.user.username}'s {self.closet_name}"

class ClothingItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothing_item_id = models.AutoField(primary_key=True)
    clothing_item_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'clothing_item'
        unique_together = (('user', 'clothing_item_id'),)

    def __str__(self):
        return f"{self.clothing_item_name}"

class ClosetStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    closet = models.ForeignKey(ClosetInfo, on_delete=models.CASCADE)
    hanger_number = models.IntegerField()
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    in_closet = models.BooleanField(default=True)

    class Meta:
        db_table = 'closet_status'
        unique_together = [
            ('user', 'closet', 'clothing_item'),
            ('closet', 'hanger_number'),
        ]

    def __str__(self):
        return f"Hanger {self.hanger_number} in {self.closet.closet_name}"

class OutfitInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outfit_id = models.AutoField(primary_key=True)
    outfit_name = models.CharField(max_length=255)
    outfit_pic_file_path = models.ImageField(upload_to='outfits/', default='outfits/default.jpg')
    clothing_items = models.ManyToManyField(ClothingItem)

    class Meta:
        db_table = 'outfit_info'
        unique_together = (('user', 'outfit_id'),)

    def __str__(self):
        return f"{self.outfit_name}"

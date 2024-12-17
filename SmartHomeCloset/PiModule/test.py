import psycopg2

conn = psycopg2.connect(dbname='webappdb', 
        user='postgre',
        password='1q2w3e4R.',
        host='192.168.86.22',
        port='5432')


sql = """ UPDATE closet_info
        SET in_closet = %s
        WHERE id = %s"""

hanger_id = 1
in_closet = False

try:
    with  conn.cursor() as cur:
        # execute the UPDATE statement
        cur.execute(sql, (hanger_id, in_closet))
    # commit the changes to the database
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    print("done")

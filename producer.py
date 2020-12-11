from kafka import KafkaProducer
from app.internal.models import model
import time
import random
import psycopg2
import json


# producer = KafkaProducer(bootstrap_servers='localhost:9092',
#                          client_id='4561')

while True:
    conn = psycopg2.connect("postgresql://postgres:qwerty@localhost/test")

    cur = conn.cursor()

    cur.execute(f"SELECT * FROM parking")
    lst = cur.fetchall()

    print(lst)

    parking_lst = []

    for item in lst:
        tmp = model.Parking(id=int(item[0]), occupied=bool(item[1]))
        tmp.occupied = random.choice((True, False))
        parking_lst.append(tmp)

    random.shuffle(parking_lst)

    print(parking_lst)

    obj_dict = {x.id: x.occupied for x in parking_lst[:1]}

    msg = json.dumps(obj_dict).encode('UTF-8')

    get_msg = msg.decode("UTF-8")

    items = json.loads(get_msg)

    print(f"Parse items{items}")

    for id, occupied in items.items():
            # cur = model.cursor
        # cur.execute(f"SELECT * FROM parking WHERE id={id}")
        
        # res = cur.fetchone()

        # print(res)

        try:
            cur.execute(f"UPDATE parking SET occupied={occupied} WHERE id={id} RETURNING id")
            res1 = cur.fetchone()
            print(res1)
            conn.commit()

        except Exception as e:
            print(e)
            conn.rollback()

        # print(id, occupied)
        # tmp = model.Parking(id=id, occupied=bool(occupied))
        # print(f"TMP OBJ {id, tmp.id}")
        # a = model.session.query(model.Parking).filter_by(id=tmp.id).first()
        # print(f"A obj {a}")
        # try:
        #     a.occupied = occupied
        #     print(f"Formatterd {a}")
        #     model.session.commit()
        # except Exception as e:
        #     print(e)
        #     model.session.rollback()

    # print(items)
    # producer.send("parkingzxc", value=msg)
    time.sleep(5)
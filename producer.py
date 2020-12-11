from kafka import KafkaProducer
from app.internal.models import model
import time
import random
import json


# producer = KafkaProducer(bootstrap_servers='localhost:9092',
#                          client_id='4561')



while True:
    lst = model.session.query(model.Parking).order_by(model.Parking.id).all()
    for item in lst:
        item.occupied = random.choice((True, False))
        
    print(f"DB_Res: {lst}")

    random.shuffle(lst)

    obj_dict = {x.id: x.occupied for x in lst[:1]}
    
    print(f"Gen item{obj_dict}")

    msg = json.dumps(obj_dict).encode('UTF-8')


    get_msg = msg.decode("UTF-8")

    items = json.loads(get_msg)

    print(f"Parse items{items}")

    for id, occupied in items.items():
        print(id, occupied)
        tmp = model.Parking(id=id, occupied=bool(occupied))
        a = model.session.query(model.Parking).filter_by(id=id).first()
        try:
            a.occupied = occupied
            model.session.commit()
        except Exception as e:
            print(e)
            model.session.rollback()

    print(items)
    # producer.send("parkingzxc", value=msg)
    time.sleep(5)
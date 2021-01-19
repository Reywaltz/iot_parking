from kafka import KafkaConsumer
import json

from app.internal.models import model
from sqlalchemy import update

# lst = model.session.query(model.Parking).all()
# print(lst)

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], 
                         client_id='1232',
                         group_id='parkingzxc')

consumer.subscribe("parking")
print(consumer.topics())

for msg in consumer:
    a = msg.value
    a = a.decode("UTF-8")

    b = json.loads(a)

    for id, occupied in b.items():
        print(id, occupied)
        tmp = model.Parking(id=id, occupied=bool(occupied))
        a = model.session.query(model.Parking).filter_by(id=id).first()
        print(a)
        try:
            a.occupied = occupied
            model.session.commit()
        except Exception as e:
            print(e)
            model.session.rollback()

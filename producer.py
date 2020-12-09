from kafka import KafkaProducer
from app.internal.models import model
import time
import json


lst = model.session.query(model.Parking).order_by(model.Parking.id).all()
print(lst)

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         client_id='456')

print(producer)

while True:
    print("send")
    lst = model.session.query(model.Parking).order_by(model.Parking.id).all()
    obj_dict = {x.id: x for x in lst}
    print(obj_dict)
    while True:
        # data = {slot.id: slot.occupied}
        msg = json.dumps(lst).encode('UTF-8')
        producer.send("iot", value=msg)
        time.sleep(1)
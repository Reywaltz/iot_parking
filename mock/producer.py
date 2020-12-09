from kafka import KafkaProducer
from internal.models import model
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
    for slot in lst:
        data = {slot.id: slot.occupied}
        msg = json.dumps(data).encode('UTF-8')
        producer.send("iot", value=msg)
        time.sleep(10)
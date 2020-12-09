from kafka import KafkaConsumer
# from internal.models import model

from ..internal.models import model

lst = model.session.query(model.Parking).all()
print(lst)

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], 
                         client_id='123',
                         group_id='iot_group')

consumer.subscribe("iot")

for msg in consumer:
    print(msg)

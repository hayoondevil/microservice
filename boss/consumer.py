import pika
import json
from main import Shop, Order, db

params = pika.URLParameters('amqps://qkvaehyt:U0avfIqb3IuLd7UsgMlK2AOJhIzsM5eL@dingo.rmq.cloudamqp.com/qkvaehyt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='boss')

def callback(ch, method, properties, body):
  print('Received in boss')  
  data = json.loads(body)  
  print(data)

  if properties.content_type == 'shop_create':
    shop = Shop(id=data['id'], shop_name=data['shop_name'], shop_address=data['shop_address'])
    db.session.add(shop)
    db.session.commit()

  elif properties.content_type == 'shop_update':
    shop = Shop.query.get(data['id'])
    shop.shop_name = data['shop_name']
    shop.shop_address = data['shop_address']
    db.session.commit()

  elif properties.content_type == 'shop_delete':
    shop = Shop.query.get(data)
    db.session.delete(shop)
    db.session.commit()

  elif properties.content_type == 'order_create':
    order = Order(id=data['id'], shop=data['shop'], address=data['address'])
    db.session.add(order)
    db.session.commit()

  elif properties.content_type == 'order_update':
    order = Order.query.get(data['id'])
    order.shop = data['shop']
    order.address = data['address']
    db.session.commit()
        
  elif properties.content_type == 'order_delete':
    order = Order.query.get(data)
    db.session.delete(order)
    db.session.commit()       


channel.basic_consume(queue='boss', on_message_callback=callback, auto_ack=True)

print('Started boss consuming')

channel.start_consuming()

channel.close
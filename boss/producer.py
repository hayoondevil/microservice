import pika
import json

params = pika.URLParameters('amqps://qkvaehyt:U0avfIqb3IuLd7UsgMlK2AOJhIzsM5eL@dingo.rmq.cloudamqp.com/qkvaehyt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
  properties = pika.BasicProperties(method)  
  channel.basic_publish(exchange='', routing_key='order', body=json.dumps(body), properties=properties) 

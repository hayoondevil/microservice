import pika

params = pika.URLParameters('amqps://qkvaehyt:U0avfIqb3IuLd7UsgMlK2AOJhIzsM5eL@dingo.rmq.cloudamqp.com/qkvaehyt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
  channel.basic_publish(exchange='', routing_key='boss', body='hello')

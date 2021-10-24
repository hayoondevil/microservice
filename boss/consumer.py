import pika

params = pika.URLParameters('amqps://qkvaehyt:U0avfIqb3IuLd7UsgMlK2AOJhIzsM5eL@dingo.rmq.cloudamqp.com/qkvaehyt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='boss')

def callback(ch, method, properties, body):
  print('Received in boss')
  print(body)


channel.basic_consume(queue='boss', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close
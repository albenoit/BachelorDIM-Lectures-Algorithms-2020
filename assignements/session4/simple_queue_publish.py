import pika
import config
import os

url = os.environ.get('CLOUDAMPQ_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')


channel.basic_publish(exchange='', routing_key='hello', body='hello world')
print ("[x] sent hello world")
connection.close()
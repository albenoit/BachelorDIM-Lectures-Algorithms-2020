import pika
import config
import os

url = os.environ.get('CLOUDAMPQ_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def publish():
    channel.basic_publish(exchange='', routing_key='hello1', body='hello world', properties=pika.BasicProperties(delivery_mode=2))
    print ("[x] sent hello world")
    connection.close()
import pika
import config
import os

url = os.environ.get('CLOUDAMPQ_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
queueName='queueName'
channel.queue_declare(queue=queueName, durable=True)

def publish():
    channel.basic_publish(exchange='', routing_key=queueName, body='hello world', properties=pika.BasicProperties(delivery_mode=2))
    print ("[x] sent hello world")
    connection.close()
import mykeys
import pika
import os

url = os.environ.get('CLOUDAMQP_URL',mykeys.cloudamqplink)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello world!')

print(" [x] Sent 'Hello World!'")
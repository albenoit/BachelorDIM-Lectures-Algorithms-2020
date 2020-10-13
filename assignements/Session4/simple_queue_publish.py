import mykey
import pika
import os

# Configure a connexion to a remote RabbitMQ instance:
amqp_url= mykey.cloudlink
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                    routing_key='hello',
                    body='Hello world!')
print(" [x] Sent 'Hello World!'")
connection.close()
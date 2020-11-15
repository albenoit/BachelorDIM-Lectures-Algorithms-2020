import pika
import myKeysCloudAMQP
import os

amqp_url= myKeysCloudAMQP.cloud_amqp_key
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5


connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
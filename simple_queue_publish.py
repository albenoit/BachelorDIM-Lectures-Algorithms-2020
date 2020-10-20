import pika
import os
import config

amqp_url=config.AMQP_URL
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() 
channel.queue_declare(queue='hello')
i=0
for i in range(0, 10):
    i+=1
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body="Hello World - "+str(i),
                          properties=pika.BasicProperties(
                                  delivery_mode=2))

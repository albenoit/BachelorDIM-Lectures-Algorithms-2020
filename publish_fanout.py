import pika
import os
import config

amqp_url=config.AMQP_URL
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
message="Hello World"
channel = connection.channel() 
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
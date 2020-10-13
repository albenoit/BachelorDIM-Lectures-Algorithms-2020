import pika
import os
import config

amqp_url=config.AMQP_URL
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() 

def callback(ch, method, properties, body):
    print(' [X] Received %r' % body)
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body="Hello World")
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)
print(' [*] Waiting for messages. To exit press Ctrl+C')
channel.start_consuming()
connection.close()
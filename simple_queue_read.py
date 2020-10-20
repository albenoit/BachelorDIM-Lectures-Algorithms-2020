import pika
import os
import config
counter = 0
amqp_url=config.AMQP_URL
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() 

def callback(ch, method, properties, body):
    global counter
    counter+=1
    print(' ['+str(counter)+'] Received %r' % body)
    channel.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=False)
print(' [*] Waiting for messages. To exit press Ctrl+C')
channel.start_consuming()
connection.close()
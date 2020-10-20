import pika
import config
import os

#url = os.environ.get('CLOUDAMPQ_url', config.keyAMQP)
#params = pika.URLParameters(url)
#params.socket_timeout = 5

#connection = pika.BlockingConnection(params)
#channel = connection.channel()
#queueName='queueName'
#channel.queue_declare(queue=queueName, durable=True)

def publish(channel, queueName, connection.):
    channel.exchange_declare(exchange='logs',exchange_type='fanout')
    channel.basic_publish(exchange='logs', routing_key='', body='hello world')
    print ("[x] sent hello world")
    connection.close()
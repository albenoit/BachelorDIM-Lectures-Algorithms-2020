import pika
import config
import os
import simple_queue_read as reader
import simple_queue_publish as publisher
import argparse


url = os.environ.get('CLOUDAMPQ_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
#queueName='queueName'
#channel.queue_declare(queue=queueName, durable=True)

channel.exchange_declare(exchange='logs', exchange_type='fanout')


parser=argparse.ArgumentParser(description="how to")
parser.add_argument('-read', action='store_true')
FLAGS=parser.parse_args()

if FLAGS.read :
    reader.consume(queue_name)
else:
    publisher.publish(queue_name)
    
    

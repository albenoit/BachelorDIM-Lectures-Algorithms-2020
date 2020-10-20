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
queueName='queueName'
channel.queue_declare(queue=queueName, durable=True)


parser=argparse.ArgumentParser(description="how to")
parser.add_argument('-concurrency', action='store_true')
FLAGS=parser.parse_args()

if FLAGS.concurrency :
    reader.consume(queueName)
else:
    publisher.publish(queueName)

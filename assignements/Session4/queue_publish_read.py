import argparse
import mykey
import pika
import os
import simple_queue_publish
import simple_queue_read

parser= argparse.ArgumentParser(description="How to")
parser.add_argument('-read', action='store_true')
parser.add_argument('-concurrency',help='mutliple concurrent queue readers', action='store_true')
flags = parser.parse_args()

#flags.read = True

amqp_url= mykey.cloudlink
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()



if flags.concurrency:
    channel.queue_declare(queue='t  ',durable=True)
    channel.basic_qos(prefetch_count=1)
    simple_queue_publish.simple_queue_publish(channel, connection)
#Test pour savoir le type d'exucution à effectuer
elif flags.read:
    channel.queue_declare(queue='hello')
    simple_queue_read.simple_queue_read(channel, connection)
else:
    channel.queue_declare(queue='hello')
    simple_queue_publish.simple_queue_publish(channel, connection)
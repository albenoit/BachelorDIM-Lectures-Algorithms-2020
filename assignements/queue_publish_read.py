import argparse
import pika, os
from assignements import simple_queue_publish
from assignements import simple_queue_read
from assignements import mykey

url = os.environ.get('CLOUDAMQP_URL', mykey.myKey)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue

parser = argparse.ArgumentParser(description='How to')
parser.add_argument('-read', action='store_true')
flags = parser.parse_args()

if(flags.read):
    simple_queue_read.read_queue(channel)
else:
    simple_queue_publish.publish_queue(channel)
connection.close()

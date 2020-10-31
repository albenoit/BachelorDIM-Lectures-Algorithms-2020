import argparse

import os
import pika
from decouple import config
import importlib
simple_queue_read = importlib.import_module('simple_queue_read')
simple_queue_publish = importlib.import_module('simple_queue_publish')

URL = config('URL')

url = os.environ.get('CLOUDAMQP_URL', URL)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='hello')  # Declare a queue

parser = argparse.ArgumentParser(description='How to')
parser.add_argument('-read', action='store_true')
flags = parser.parse_args()

if flags.read:
    simple_queue_read.read_queue(channel)
else:
    simple_queue_publish.publish_queue(channel)
connection.close()

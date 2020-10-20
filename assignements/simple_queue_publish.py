import pika
import argparse
from keys import Keys
key = Keys()
AMQP_url = key.getAMQP_URL()
properties = None

connection = pika.BlockingConnection(pika.URLParameters(AMQP_url))
channel = connection.channel()
channel.queue_declare(queue='presentation')

parser = argparse.ArgumentParser()
parser.add_argument('-concurrency', action='store_true')
FLAGS = parser.parse_args()

if FLAGS.concurrency:
    properties = pika.BasicProperties(delivery_mode=2)

body = 'test save'

channel.basic_publish(exchange='', routing_key='presentation', body=body, properties=properties)
print("[SEND] Sent:", body)
connection.close()
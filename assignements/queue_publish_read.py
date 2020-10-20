import pika
import argparse
from keys import Keys

key = Keys()
AMQP_url = key.getAMQP_URL()
QUEUE = 'presentation'
body = 'Coucou'
properties = None

parser = argparse.ArgumentParser(description='How to')
parser.add_argument('-read', action='store_true')
parser.add_argument('-concurrency', action='store_true')
FLAGS = parser.parse_args()

connection = pika.BlockingConnection(pika.URLParameters(AMQP_url))
channel = connection.channel()
channel.queue_declare(queue=QUEUE)

def callback(ch, method, properties, body):
    print("[READ] Received: " + body.decode('UTF-8'))
    ch.basic_ack(delivery_tag = method.delivery_tag)

if FLAGS.concurrency:
    properties = pika.BasicProperties(delivery_mode=2)

if FLAGS.read:
    channel.basic_consume(queue=QUEUE, on_message_callback=callback)
    channel.start_consuming()
else:
    channel.basic_publish(exchange='', routing_key=QUEUE, body=body, properties=properties)
    print("[SEND] Sent:", body)
    connection.close()
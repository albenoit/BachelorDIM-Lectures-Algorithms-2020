import pika
import os
import mykeys
import argparse

url = os.environ.get('CLOUDAMQP_URL', mykeys.cloudamqplink)
params = pika.URLParameters(url)
params._socket_timeout= 5

parser = argparse.ArgumentParser(description='How to')
parser.add_argument("-concurrency", action='store_true')
FLAGS = parser.parse_args()

connection = pika.BlockingConnection(pika.URLParameters(mykeys.cloudamqplink))
channel = connection.channel()
channel.queue_declare(queue='hellothere')

def publish():
    '''
    Connect to the hellothere route and publish "Hello World" to the RabbitMQ service.

    :return: no returns.
    '''
    channel.basic_publish(exchange='',
                          routing_key='hellothere',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()

def publishWithConcurrency():
    channel.basic_publish(exchange='',
                          routing_key='hellothere',
                          body='Hello World!',
                          properties=pika.BasicProperties(
                              delivery_mode=2
                          ))
    print(" [x] Sent 'Hello World!'")
    connection.close()

if FLAGS.concurrency:
    publishWithConcurrency()
else:
    publish()
# publish.py
import pika, os

def callback(ch, method, properties, body):
    print(" [" + str(method.delivery_tag) + "] Received " + str(body))

def read_queue(channel):
    channel.basic_consume('hello', callback, auto_ack=True)
    print(' [*] Waiting for messages:')
    channel.start_consuming()



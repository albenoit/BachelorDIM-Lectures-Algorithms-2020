import pika
import config
import os

url = os.environ.get('CLOUDAMPQ_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello1')

def callback(ch,method, properties, body):
    print("[X] recevied %r" %body)
    print("[X] message processed, acknowledging (to delete message from the queue)")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume():
    channel.basic_consume(queue='hello1', on_message_callback=callback, auto_ack=True) 
    print("[X] waiting for message. to exit press CTRL+C")
    channel.start_consuming()
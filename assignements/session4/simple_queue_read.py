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


channel.basic_consume(queue='hello1', on_message_callback=callback, auto_ack=True)
    
print("[X] waiting for message. to exit press CTRL+C")

channel.start_consuming()
import pika
import os
import keys
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--concurrency", "-C", action="store_true")
args = parser.parse_args()

print(args.concurrency)

url = os.environ.get('CLOUDAMQP_URL', keys.amqpkey)
params = pika.URLParameters(url)
params.socket_timeout = 5

count = 0

# reader
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')

def callback(ch, method, properties, body):
    global count
    count = count + 1
    if args.concurrency:
        ch.queue_declare(queue='task_queue', durable=True)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        
    ch.basic_qos(prefetch_count=1)
    print(" [X] Received %r" % body)
    print("J'ai recu " + str(count) + " message(s)")
    time.sleep(0.5)

channel.basic_consume(queue='presentation',
    on_message_callback=callback,
    auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
import pika
import os
import keys

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
    print(" [X] Received %r" % body)
    print("J'ai recu " + str(count) + " message(s)")

channel.basic_consume(queue='presentation',
    on_message_callback=callback,
    auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
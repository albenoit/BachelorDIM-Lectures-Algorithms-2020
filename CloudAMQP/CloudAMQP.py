import pika
import os
import keys

print(keys.amqpkey)
url = os.environ.get('CLOUDAMQP_URL', keys.amqpkey)
params = pika.URLParameters(url)
params.socket_timeout = 5

# publish
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
    routing_key='hello',
    body='Hello World!')

print(" [X] Send 'Hello World!'")
connection.close()

# reader
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [X] Received %r" % body)

channel.basic_consume(queue='hello',
    on_message_callback=callback,
    auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
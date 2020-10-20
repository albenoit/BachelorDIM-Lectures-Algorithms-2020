import pika
import mykeys
import os

url = os.environ.get('CLOUDAMQP_URL', mykeys.cloudamqplink)
params = pika.URLParameters(url)
params._socket_timeout= 5

connection = pika.BlockingConnection(pika.URLParameters(mykeys.cloudamqplink))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

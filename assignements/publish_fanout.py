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

channel.basic_publish(exchange='myWorkingQueue',
                      routing_key='',
                      body="yo le rap")
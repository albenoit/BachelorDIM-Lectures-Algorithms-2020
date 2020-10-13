import pika
import os
import mykeys

url = os.environ.get('CLOUDAMQP_URL', mykeys.cloudamqplink)
params = pika.URLParameters(url)
params._socket_timeout= 5

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hellothere')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
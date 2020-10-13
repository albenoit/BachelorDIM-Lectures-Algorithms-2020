import pika
from keys import Keys
key = Keys()
AMQP_url = key.getAMQP_URL()

connection = pika.BlockingConnection(pika.URLParameters(AMQP_url))
channel = connection.channel()
channel.queue_declare(queue='presentation')

channel.basic_publish(exchange='', routing_key='presentation', body='Hello World !')
print(" [x] Sent 'Hello World!'")
connection.close()
import pika
from keys import Keys
key = Keys()
AMQP_url = key.getAMQP_URL()

connection = pika.BlockingConnection(pika.ConnectionParameters(host=AMQP_url, port=1883))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World !')
print(" [x] Sent 'Hello World!'")
connection.close()
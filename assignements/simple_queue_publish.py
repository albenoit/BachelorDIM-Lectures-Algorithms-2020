import pika
from keys import Keys
key = Keys()
AMQP_url = key.getAMQP_URL()

connection = pika.BlockingConnection(pika.URLParameters(AMQP_url))
channel = connection.channel()
channel.queue_declare(queue='presentation')

body = 'Coucou'

channel.basic_publish(exchange='', routing_key='presentation', body=body)
print("[SEND] Sent:", body)
connection.close()
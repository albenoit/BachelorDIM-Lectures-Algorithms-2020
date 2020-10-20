import pika
from keys import Keys

key = Keys()
AMQP_url = key.getAMQP_URL()
QUEUE = 'presentation'

connection = pika.BlockingConnection(pika.URLParameters(AMQP_url))
channel = connection.channel()
channel.queue_declare(queue=QUEUE)

channel.basic_consume(queue=QUEUE, on_message_callback=callback, auto_ack=True)
channel.start_consuming()

def callback(ch, method, properties, body):
    print("[READ] Received: " + body.decode('UTF-8'))

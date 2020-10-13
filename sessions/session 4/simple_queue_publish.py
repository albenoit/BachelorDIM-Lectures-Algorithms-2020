# publish.py
import pika, os
from decouple import config

URL = config('URL')
  
# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', URL)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
channel.basic_publish(exchange='',
                  routing_key='hello',
                  body='Hello CloudAMQP!')

print(" [x] Sent 'Hello World!'")

def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()
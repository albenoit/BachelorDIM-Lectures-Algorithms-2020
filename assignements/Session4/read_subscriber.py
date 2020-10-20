import pika
import config
import os
import time

counter = 0

#configuration
url = os.environ.get('CLOUDAMQP_URL', config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

#connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange='posts', exchange_type='fanout')
# channel.basic_qos(prefetch_count=1)

result = channel.queue_declare(queue='', exclusive=True)
queue_name =result.method.queue #get the reader specific queue name

channel.queue_bind(exchange='posts', queue=queue_name)

def callback(ch, method, properties, body):
    global counter
    counter = counter + 1
    print(" [x] Reveived %r" % body)
    

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

print((" [*] Reading %r queue." % queue_name))
print((" [*] Waiting for messages. To exit press CTRL+C"))
# if(sleep != False):
#         print('Running with sleep mode with 5 sec timer')
channel.start_consuming()
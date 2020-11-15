import pika
import myKeysCloudAMQP
import os

amqp_url= myKeysCloudAMQP.cloud_amqp_key
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)

count = 0
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_qos(prefetch_count=1)


def callback (ch, method, properties, body):
    print("[x] Received %r" % body)
    global count
    count += 1
    print("[x] Message Processed, acknowledging, nb message sent: "+str(count)+" (o delete message from the queue)")

channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)
channel.start_consuming()


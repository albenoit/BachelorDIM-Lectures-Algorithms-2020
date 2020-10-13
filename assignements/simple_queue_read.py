import pika
import mykeys

connection = pika.BlockingConnection(pika.URLParameters(mykeys.cloudamqplink))
channel = connection.channel()
channel.queue_declare(queue='hellothere')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hellothere',
                      on_message_callback=callback,
                      auto_ack=True)
print(' [x] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()

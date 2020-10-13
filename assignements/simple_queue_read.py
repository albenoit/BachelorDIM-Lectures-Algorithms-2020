import pika
import mykeys

connection = pika.BlockingConnection(pika.URLParameters(mykeys.cloudamqplink))
channel = connection.channel()
channel.queue_declare(queue='hellothere')

count = 0

def callback(ch, method, properties, body):
    global count
    count += 1
    print("Count: " + str(count) + " ; [x] Received %r" % body)


channel.basic_consume(queue='hellothere',
                      on_message_callback=callback,
                      auto_ack=True)
print(' [x] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()

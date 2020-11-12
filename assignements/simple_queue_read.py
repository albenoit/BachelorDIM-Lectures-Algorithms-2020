import pika
import mykeys

connection = pika.BlockingConnection(pika.URLParameters(mykeys.cloudamqplink))
channel = connection.channel()
channel.queue_declare(queue='myWorkingQueue', durable=True)

count = 0
def callback(ch, method, properties, body):
    global count
    count += 1
    print("Count: " + str(count) + " ; [x] Received %r" % body)
    print(" [x] Message Processed, aknowledging (to delete message from the queue)")
    channel.basic_ack(delivery_tag= method.delivery_tag)

channel.basic_consume(queue='myWorkingQueue',
                      on_message_callback=callback,
                      auto_ack=False)
print(' [x] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()

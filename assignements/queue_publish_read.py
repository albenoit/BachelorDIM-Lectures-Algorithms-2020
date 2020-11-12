import argparse
import pika
import mykeys

connection = pika.BlockingConnection(pika.URLParameters(mykeys.cloudamqplink))
channel = connection.channel()
channel.queue_declare(queue='hellothere')

parser = argparse.ArgumentParser(description='How to')
parser.add_argument("-read", action='store_true')
FLAGS = parser.parse_args()

def read():
    '''
    Get to read all the incoming data of the hellothere queue.

    :return: no returns.
    '''
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

def publish():
    '''
    Connect to the hellothere route and publish "Hello World" to the RabbitMQ service.

    :return: no returns.
    '''
    channel.basic_publish(exchange='',
                          routing_key='hellothere',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()


if FLAGS.read:
    read()
else:
    publish()

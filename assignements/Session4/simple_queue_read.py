import pika
import config
import os

counter = 0

def simple_queue_read(concurrency):
    '''
    Function to received and print in console 
    some message with CLOUDAMPQ
    '''

    #configuration
    url = os.environ.get('CLOUDAMQP_URL', config.amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    #connexion
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')

    def callback(ch, method, properties, body):
        global counter
        counter = counter + 1
        print(" [x] Reveived %r" % body)
        print('%r messages received' % counter)
        if(concurrency != False):
            print(' [x] Message Processed, acnowledging (to delete message from the queue)')
            ch.basic_ack(delivery_tag= method.delivery_tag)
        

    channel.basic_consume(queue='presentation', on_message_callback=callback, auto_ack=False)

    print((" [*] Waiting for messages. To exit press CTRL+C"))
    channel.start_consuming()
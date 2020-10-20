import pika

def simple_queue_publish(channel, connection):
    '''
        publish all messages
        Parameters:
            channel, connection
        Returns:
            void
        Raises:
            no raise
    '''
    #channel.exchange_declare(exchange='',
    #                        exchange_type='fanout')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!',
                          properties=pika.BasicProperties(
                              delivery_mode = 2,
                          ))

    print(" [x] Sent 'Hello World!'")
    connection.close()
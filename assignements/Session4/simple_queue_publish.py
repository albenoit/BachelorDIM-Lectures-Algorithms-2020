import pika

def simple_queue_publish(channel, connection):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!',
                          properties=pika.BasicProperties(
                              delivery_mode = 2,
                          ))

    print(" [x] Sent 'Hello World!'")
    connection.close()
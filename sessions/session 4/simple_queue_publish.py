# publish.py


def publish_queue(channel):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello CloudAMQP!')
    print(" [x] Sent 'Hello World!'")

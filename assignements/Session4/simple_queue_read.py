def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))
  ch.basic_ack(delivery_tag = method.delivery_tag)


def simple_queue_read(channel, connection):
    channel.basic_consume('hello',
                      on_message_callback=callback,
                      auto_ack=False)
    print(' [*] Waiting for messages:')
    channel.start_consuming()
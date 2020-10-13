def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))


def simple_queue_read(channel, connection):
    channel.basic_consume('hello',
                      on_message_callback=callback,
                      auto_ack=True)
    print(' [*] Waiting for messages:')
    channel.start_consuming()
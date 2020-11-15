import pika
import uuid
import os
import config


class RpcClient(object):

    """
    Class to instance rpc servers
    Methods:
        __init__ : create the connection. get the channel and the callback_queue
        on_response : method who chekx the response correlation_id and get the response body
        call : method call to send message to servers and wait for response
    """

    # configuration
    url = os.environ.get("CLOUDAMQP_URL", config.amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    def __init__(self):
        self.connection = pika.BlockingConnection(self.params)

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, message):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(message),
        )
        while self.response is None:
            self.connection.process_data_events()
        return self.response


rpc_client = RpcClient()

print(" [x] Requesting to client")
response = rpc_client.call("Hi, how fine?")
print(" [*] Got %r" % response.decode("utf-8"))
import pika 

class ReceiverOrder():
    def __init__(self):
        self.exchange = 'orders'
        self.routing_key = 'receive_data'
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='topic')
            pika.ConnectionParameters(host='localhost'))
        self.declare_queue('order_ms')
        self.channel.queue_bind(
            exchange=self.exchange,
            queue=self.queue,
            routing_key=self.routing_key,
        )

    def consume_message(self):
        print('Ready to receive')

        self.channel.basic_consume(
            queue = self.queue,
            on_message_callback=self.callback_order_ms,
            auto_ack=True
        )
        self.channel.start_consuming()

    def callback_order_ms(self, ch, method, properties, body):
        body = body.decode("UTF-8")
        body = json.loads(body)

        print(f'Received {body}')
    
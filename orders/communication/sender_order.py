import pika


class SenderOrder():

    def __init__(self):
        self.exchange = 'orders'
        self.routing_key = 'request_data'
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='topic')
            pika.ConnectionParameters(host='localhost'))
    
    def send_request(self, client_id):

        message = {'client_id': client_id}
        self.channel.basic_publish(
            exchange=self.exchange, routing_key=self.routing_key, body=message)
        print(" [x] Sent %r:%r" % (self.routing_key, message))
        connection.close()




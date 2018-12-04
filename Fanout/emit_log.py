import pika
import sys


url = 'amqp://debzppsy:Kg2KfgbHxvTEztQxWkelEx5sH8jnIMDW@toad.rmq.cloudamqp.com/debzppsy'
connection = pika.BlockingConnection(pika.URLParameters(url))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "Fanout Exchange Example!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
import pika

url = 'amqp://debzppsy:Kg2KfgbHxvTEztQxWkelEx5sH8jnIMDW@toad.rmq.cloudamqp.com/debzppsy'
connection = pika.BlockingConnection(pika.URLParameters(url))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
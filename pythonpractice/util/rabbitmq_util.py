# coding=utf-8
import pika
from pika.spec import BasicProperties
from pythonpra.config.rabbitmq_config import RABBITMQ_CONFIG
from pika.spec import BasicProperties

class RabbitmqUtil(object):

    @staticmethod
    def send_message(field=None, domain='test', queue=None, message=None):

        parameters = pika.URLParameters(RABBITMQ_CONFIG[field][domain])
        print RABBITMQ_CONFIG[field][domain]
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        properties = BasicProperties(content_type="application/json")
        flag = channel.basic_publish(exchange='', routing_key=queue, body=message, properties=properties)

        connection.close()
        print "send message!"
        return flag

    @staticmethod
    def callback(ch, method, properties, body):
        print "Received %r" %(body)

    @staticmethod
    def get_message(domain='test', queue=None):

        parameters = pika.URLParameters(RABBITMQ_CONFIG[domain])
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=queue)

        channel.basic_consume(RabbitmqUtil.callback, queue=queue, no_ack=True)
        channel.start_consuming()


if __name__ == '__main__':
    RabbitmqUtil.send_message('own_biz', 'test', 'local_test', 'hello,python rabbitmq!')

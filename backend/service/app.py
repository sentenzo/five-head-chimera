import asyncio

import pika
import tornado.web


class FeedbackHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "*")

    def get(self):
        self.write("Hello, world")
        connection = pika.BlockingConnection(
            pika.ConnectionParameters("rabbitmq")
        )
        channel = connection.channel()
        channel.queue_declare(queue="hello")
        channel.basic_publish(
            exchange="", routing_key="hello", body="Hello World!"
        )
        self.write("\n [x] Sent 'Hello World!'")
        connection.close()

    def put(self):
        self.write("Hello from backend!")

    def options(self):
        self.set_status(204)
        self.finish()


class QueueHandler(tornado.web.RequestHandler):
    def get(self):
        ...
        # connection = pika.BlockingConnection(
        #     pika.ConnectionParameters("rabbitmq")
        # )
        # channel = connection.channel()
        # channel.queue_declare(queue="hello")

        # def callback(ch, method, properties, body):
        #     self.write(" [x] Received %r" % body)
        #     channel.stop_consuming()

        # channel.basic_consume(
        #     queue="hello", auto_ack=True, on_message_callback=callback
        # )
        # channel.start_consuming()


def make_app():
    return tornado.web.Application(
        [
            (r"/feedback", FeedbackHandler),
            (r"/queue", QueueHandler),
        ],
        autoreload=True,
    )


async def main():
    app = make_app()
    app.listen(8000)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())

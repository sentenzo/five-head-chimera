import asyncio
import os

import pika
import tornado.web


RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", default="localhost")
QUEUE_NAME = os.environ.get("QUEUE_NAME", default="feedback")


def push_to_queue(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(RABBITMQ_HOST)
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_publish(exchange="", routing_key=QUEUE_NAME, body=message)
    connection.close()


class FeedbackHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "*")

    def get(self):
        self.write("pong")

    def put(self):
        push_to_queue(self.request.body)
        print(self.request.body)

    def options(self):
        self.set_status(204)
        self.finish()


def make_app():
    return tornado.web.Application(
        [
            (r"/feedback", FeedbackHandler),
        ],
        autoreload=True,
    )


async def main():
    app = make_app()
    app.listen(8000)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())

import os
import time

import pika


RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", default="localhost")
QUEUE_NAME = os.environ.get("QUEUE_NAME", default="feedback")
DELAY = 5


def process_one_message(method_frame, header_frame, body):
    print(
        "The message is processed:",
        method_frame,
        header_frame,
        body,
        sep="\n\t",
    )
    return True


def loop_event(connection):
    while True:
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME, durable=True)
        method_frame, header_frame, body = channel.basic_get(QUEUE_NAME)

        if method_frame is None:
            print("No message returned")
        elif not process_one_message(method_frame, header_frame, body):
            print(
                "Faild to process message:",
                method_frame,
                header_frame,
                body,
                sep="\n\t",
            )
        else:
            channel.basic_ack(method_frame.delivery_tag)
            continue

        time.sleep(DELAY)


def main():
    while True:
        connection = None
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(RABBITMQ_HOST)
            )
            loop_event(connection)
        except Exception as ex:
            print("Faild to connect to RabbitMQ:")
            print(ex)
            time.sleep(DELAY)


if __name__ == "__main__":
    main()

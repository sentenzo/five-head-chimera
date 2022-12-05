import json
import os
import time

import pika
import pika.exceptions
import psycopg2


RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", default="localhost")
QUEUE_NAME = os.environ.get("QUEUE_NAME", default="feedback")
DELAY = 5

DB_HOST = os.environ.get("DB_HOST", default="localhost")
DB_NAME = os.environ.get("POSTGRES_DB", default="feedback")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")


def db_insert_single_feedback(
    first_name: str,
    last_name: str,
    phone: str,
    feedback_text: str,
    patronym: str | None = None,
):
    conn = psycopg2.connect(
        f"host={DB_HOST} "
        f"dbname={DB_NAME} "
        "user=postgres "
        f"password={DB_PASSWORD}"
    )
    cur = conn.cursor()
    print(
        "db_insert_single_feedback "
        "(first_name, last_name, patronym, phone, feedback_text)"
    )
    print((first_name, last_name, patronym, phone, feedback_text))
    cur.execute(
        "INSERT INTO feedback "
        "(first_name, last_name, patronym, phone, feedback_text) "
        "VALUES (%s, %s, %s, %s, %s)",
        (first_name, last_name, patronym, phone, feedback_text),
    )
    conn.commit()
    cur.close()
    conn.close()


def process_one_message(method_frame, header_frame, body):
    try:
        body_dict = json.loads(body)
        db_insert_single_feedback(
            first_name=body_dict["sender"]["first_name"],
            last_name=body_dict["sender"]["last_name"],
            patronym=body_dict["sender"]["patronym"],
            phone=body_dict["sender"]["phone"],
            feedback_text=body_dict["message"],
        )
        print(
            "The message is processed:",
            method_frame,
            header_frame,
            body,
            sep="\n\t",
        )
        return True
    except psycopg2.Error as exc:
        print(
            "The message is failed:",
            method_frame,
            header_frame,
            body,
            sep="\n\t",
        )
        print(exc)
        return False


def loop_event(connection):
    while True:
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME, durable=True)
        method_frame, header_frame, body = channel.basic_get(QUEUE_NAME)

        if method_frame is None:
            print("No message returned")
        elif not process_one_message(method_frame, header_frame, body):
            print(
                "Failed to process message:",
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
        except pika.exceptions.AMQPError as exc:
            print("Failed to connect to RabbitMQ:")
            print(exc)
            time.sleep(DELAY)


if __name__ == "__main__":
    main()

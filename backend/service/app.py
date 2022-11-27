import asyncio

import tornado.web


class FeedbackHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "*")

    def get(self):
        self.write("Hello, world")

    def put(self):
        self.write("Hello from backend!")

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

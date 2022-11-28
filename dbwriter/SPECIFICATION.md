This document contains  detailed description of the **database writer** service as a part of the **User Feedback Processing System**. 

To read more about the system as a haul, see: `SPECIFICATION.md`.

# Database writer

It is written on Python, FastAPI. Though it has no API. No idea why were we asked to use FastAPI 🤷.

It takes the messages from **RabitMQ** and writes it to **Database**.
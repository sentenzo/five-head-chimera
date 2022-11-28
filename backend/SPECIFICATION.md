This document contains  detailed description of the **backend** service as a part of the **User Feedback Processing System**. 

To read more about the system as a haul, see: `SPECIFICATION.md`.

# Backend

It is written on Python, Tornado framework.

The handles are: 
- (`PUT`)`/feedback` - takes a JSON of a predetermined format (see the **frontend** service) and pushes this data to **RabitMQ** (addressed to the **DB writer** service)
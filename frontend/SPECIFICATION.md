This document contains  detailed description of the **frontend** service as a part of the **User Feedback Processing System**. 

To read more about the system as a haul, see: `SPECIFICATION.md`.

# Frontend

This is a very simple one-page site with a web-form on it. 

It has a button "Send", which pushes a JSON file to the **backend** service. 

The JSON contains the field-values from the form. The form itself has the follow fields (all required):
- first name (required)
- last name (required)
- patronim (optional)
- phone number (required)
- message text (required)

There are no restrictions on the JSON format or used js/css frameworks in the initial task, but it is advised to keep it reasonably simple.
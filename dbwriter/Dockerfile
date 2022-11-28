FROM python:3.10.8-slim-bullseye

RUN python -m pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY ./service .

CMD ["python", "app.py"]
FROM python:3.11

COPY . /app
COPY './requirements.txt' .

WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt

ENV PORT=5000
EXPOSE $PORT

CMD [ "python", "main.py" ] 


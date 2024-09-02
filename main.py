from time import sleep

import redis
from celery import Celery

REDIS_HOST = "redis://localhost:6379/0"

app = Celery("main")
app.conf.broker_url = REDIS_HOST
app.conf.result_backend = REDIS_HOST

redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
channel = "my_channel"


@app.task
def add(x, y):
    print("Calculando a soma:")
    return x + y


if __name__ == "__main__":
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)

    redis_client.publish(channel, "redis message")

    task = add.delay(2, 3)
    print("fazendo outras coisas enquanto a tarefa é executada")
    print("sleeping 10 segundos")
    sleep(10)
    print("chamando get:")
    print(task.get())

    print(f"Subscribed to {channel}. Waiting for messages...")
    for message in pubsub.listen():
        if message["type"] == "message":
            print(f"Received: {message['data'].decode('utf-8')}")

# this code existed for 24/7 bot working
from flask import Flask
from threading import Thread

app = Flask('telegramQR')


@app.route('/')
def main():
  return "Your bot is alive!"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()

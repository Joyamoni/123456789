

from flask import Flask
apple = Flask(__name__)

@apple.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  apple.run()

from flask import Flask, abort

from getHeritageIsles import getHeritageIsles

main = Flask(__name__)

@main.route('/')
def index():
    return getHeritageIsles()

if __name__ == "__main__":
    main.run(debug=True)

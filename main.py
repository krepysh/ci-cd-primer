from flask import Flask


app = Flask(__name__)

count = 0


@app.route("/")
def index(count=count):
    count += 1
    return f"Hello, World from Germany! You visited this page {count} times."


if __name__ == "__main__":
    app.run(debug=True)

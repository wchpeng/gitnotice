from flask import Flask, request

app = Flask(__name__)


@app.route("/github/event/push", methods=["POST"])
def handle_push_event():

    print("alpha:request.data: ", request.data)
    print("\nrequest.get_json: ", request.get_json())
    return "SUCCESS"


if __name__ == "__main__":
    app.run('localhost', 7701, debug=True)

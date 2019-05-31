from flask import Flask, request

app = Flask(__name__)


@app.route("/github/event/push", methods=["POST"])
def handle_push_event():
    try:
        content = request.get_json()
        branch = content["ref"].split("/")[-1]
        repository_name = content["repository"]["name"]
        print("branch: ", branch)
        print("repository_name: ", repository_name)
    except Exception as e:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>> ERROR")
        print(e)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    return "SUCCESS"


if __name__ == "__main__":
    app.run('localhost', 7701, debug=True)

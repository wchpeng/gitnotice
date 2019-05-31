from flask import Flask, request

from exec_shell import exec_shell

app = Flask(__name__)


@app.route("/github/event/push", methods=["POST"])
def handle_push_event():
    # 解析 github 发过来的数据，提取出分支名 branch 和项目名 repository_name, 交给 exec_shell 去处理
    try:
        content = request.get_json()
        branch = content["ref"].split("/")[-1]
        repository_name = content["repository"]["name"]
        exec_shell(branch, repository_name)
    except Exception as e:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>> ERROR")
        print(e)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    return "SUCCESS"


if __name__ == "__main__":
    app.run('localhost', 7701, debug=True)

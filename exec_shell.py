# -*- coding:utf-8 -*-
import os


# 定义每个不同的仓库名字执行的 shell 语句
SHELL_DICT = {
    "my_blog": "cd /home/wcp/work/github-projects/my_blog && git pull origin master && supervisorctl restart wcp_blog_uwsgi",
    "SharePic": "cd /home/wcp/work/github-projects/SharePic && git pull origin master && supervisorctl restart wcp_SharePic_uwsgi wcp_SharePic_celery_worker"
}


def exec_shell(branch, repository_name):
    # 过滤掉非 master 提交的更改，其他执行
    if branch != "master":
        return None
    if repository_name not in SHELL_DICT:
        return None
    return os.system(SHELL_DICT[repository_name])
    return os.popen(SHELL_DICT[repository_name])

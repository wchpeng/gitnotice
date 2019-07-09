# -*- coding:utf-8 -*-
import os


# 定义每个不同的仓库名字执行的 shell 语句
SHELL_DICT = {
    "my_blog": "cd /home/wcp/work/github-projects/my_blog && "
               "git pull origin master && "
               "/home/wcp/.virtualenvs/py3_django2/bin/uwsgi --stop /home/wcp/var/pids/uwsgi_pidfile.log && "
               "supervisorctl start wcp_blog_uwsgi",
    "SharePic": "cd /home/wcp/work/github-projects/SharePic && "
                "git pull origin master && "
               "/home/wcp/.virtualenvs/py3_django2/bin/uwsgi --stop /home/wcp/var/pids/uwsgi_SharePic.pid && "
                "supervisorctl restart wcp_SharePic_uwsgi wcp_SharePic_celery_worker",
    "Stock": "cd /home/wcp/work/git-projects/Stock && "
             "git pull origin master &&"
             "supervisorctl restart Stock_project:*"
}


def exec_shell(branch, repository_name):
    # 过滤掉非 master 提交的更改，其他执行
    if branch != "master":
        return None
    if repository_name not in SHELL_DICT:
        return None
    return os.system(SHELL_DICT[repository_name])

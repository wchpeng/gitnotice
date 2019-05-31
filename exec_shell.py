import os


SHELL_DICT = {
    "my_blog": "cd /home/wcp/work/github-projects/my_blog && git pull && supervisorctl restart wcp_blog_uwsgi"
}


def exec_shell(branch, repository_name):
    if branch != "master":
        return None
    if repository_name not in SHELL_DICT:
        return None
    return os.system(SHELL_DICT[repository_name])

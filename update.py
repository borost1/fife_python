import requests
import json

url = 'https://api.github.com/repos/borost1/fife_python/git/trees/master?recursive=1'
r = requests.get(url, allow_redirects=True)

if r.status_code == 200:
    files_list = json.loads(r.text)
    repo_files = [f['path'] for f in files_list['tree'] if f['path'][-6:] == ".ipynb" and 'checkpoints' not in f['path']]
    lessons = [f for f in repo_files if '/' not in f]
    tasks = [f for f in repo_files if '/' in f]
    print(lessons)
    print(tasks)

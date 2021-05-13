import requests
import json
import os

url = 'https://api.github.com/repos/borost1/fife_python/git/trees/master?recursive=1'
r = requests.get(url, allow_redirects=True)


def copy_from_github(file_list):
    for file_name in file_list:
        if '/' in file_name:
            dir_name = file_name.split('/')[0]
            if os.path.isdir(dir_name) is False:
                os.mkdir(dir_name)
                print(f'Directory {dir_name} not found, so it was created.')
            else:
                print(f'Directory {dir_name} already exists.')
        raw_url = f'https://raw.githubusercontent.com/borost1/fife_python/master/{file_name}'
        content = requests.get(raw_url, allow_redirects=True)
        file = open(f'{file_name}', 'w', encoding='utf-8')
        file.write(content.text)
        file.close()
        print(f'File: {file_name} updated!')


if r.status_code == 200:
    files_list = json.loads(r.text)
    repo_files = [f['path'] for f in files_list['tree'] if f['path'][-6:] == ".ipynb" and 'checkpoints' not in f['path']]
    copy_from_github(repo_files)
else:
    print("FAILED. Check your internet connection.")


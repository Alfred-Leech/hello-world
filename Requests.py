  # GNU nano 3.2                          test3.py

import json
import requests


# api_url_base = 'https://api.github.com/'
api_url_base = 'https://api.github.com/orgs/'

myheaders = {'Content-Type': 'application/json',
           'User-Agent': 'Python Student',
           'Accept': 'application/vnd.github.v3+json'}

def get_repos(username):

    api_url = '{}{}/repos'.format(api_url_base, username)

    # response = requests.get(api_url, headers=myheaders)
    response = requests.get(api_url) #without header also can work


    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code,
api_url))
        return None

repo_list = get_repos('octokitx')


if repo_list is not None:
    # print((repo_list)[0])
    for item in repo_list:
      print ((item)['id'])
else:
    print('No Repo List Found')

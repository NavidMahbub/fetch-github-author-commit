import requests

REPO = 'NavidMahbub/fetch-github-author-commit'
URL = f'https://api.github.com/repos/{REPO}/commits'

response = requests.get(URL)

print('\n========================================================')
print('===================== Author & Commits =================')
print('========================================================')

if response.status_code == 200:
    commits = response.json()
    for commit in commits:
        commit_message = commit['commit']['message']
        author_name = commit['commit']['author']['name']
        print(f'Author: {author_name}, Commit Message: {commit_message}')
else:
    print(f'Failed to fetch commits: {response.status_code}')

print('========================================================')
print('========================================================')
print('========================================================')

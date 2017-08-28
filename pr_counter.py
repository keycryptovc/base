import github3
import datetime

# authorization
login = ''
password = ''
gh = github3.login(login, password)

# get info about repo
repo_owner = 'keycryptovc'
repo_name = 'base'
repo = gh.repository(repo_owner, repo_name)

# define number of days to check
date_depth = 30
date_depth = datetime.timedelta(days=date_depth)
starting_date = datetime.date.today() - date_depth

# get pulls
pulls = [pull for pull in repo.iter_pulls(state='closed', base='master') if (pull.is_merged() and
         pull.closed_at.date() > starting_date)]

# fill info about PRs by user
contributions = {}
for pull in pulls:
    login = pull.user.login
    if login in contributions:
        contributions[login] += 1
    else:
        contributions[login] = 1

print(contributions)

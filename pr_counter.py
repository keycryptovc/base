import github3

# authorization
login = ''
password = ''
gh = github3.login(login, password)

# get info about repo
repo_owner = 'keycryptovc'
repo_name = 'base'
repo = gh.repository(repo_owner, repo_name)

# define number of PRs to get
number_pr = 200
# get pulls
pulls = [pull for pull in repo.iter_pulls(state='closed', base='master', number=number_pr) if pull.is_merged()]

# fill info about PRs by user
contributions = {}
for pull in pulls:
    login = pull.user.login
    if login in contributions:
        contributions[login] += 1
    else:
        contributions[login] = 1

print(contributions)


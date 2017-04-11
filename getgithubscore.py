import requests
from requests.auth import HTTPBasicAuth

list_of_repos = []
fork_score, star_score, commit_score = (0,)*3
#FUCK YOU CALEB

def final_score(username='arshbot'):
    raw_score = compile_raw_gitscore(username)
    f_commit_score, f_star_score, f_fork_score = (0,)*3
    
    if raw_score['commit_score']<100:
        f_commit_score = 8.66
    elif raw_score['commit_score']<250:
        f_commit_score = 8.66*2
    else:
        f_commit_score = 26

    if raw_score['fork_score']<10:
        f_fork_score = 1.75
    elif raw_score['fork_score']<30:
        f_fork_score = 1.75*2
    elif raw_score['fork_score']<60:
        f_fork_score = 1.75*3
    elif raw_score['fork_score']>100:
        f_fork_score = 1.75*4

    if raw_score['star_score']<15:
        f_star_score = 1.75
    elif raw_score['star_score']<30:
        f_star_score = 1.75*2
    elif raw_score['star_score']<60:
        f_star_score = 1.75*3
    elif raw_score['star_score']>150:
        f_star_score = 1.75*4

    return f_star_score + f_fork_score + f_commit_score

def compile_raw_gitscore(username='arshbot'):
    get_user_repos(username)
    get_num_of_github_commits(username)
    get_num_of_stars_and_forks(username)
    return {'fork_score': fork_score, 'star_score': star_score, 'commit_score': commit_score}

def get_user_repos(username='arshbot'):
    global list_of_repos
    r = requests.get('https://api.github.com/users/'+username+'/repos', auth=HTTPBasicAuth('arshbot', 'e172a7f23e13fc855016bb391bd5f504f3f13d86'))
    repos = r.json()
    if str(r) == '<Response [404]>':
        print "Shit ain't found"
        return []
    elif str(r) == '<Response [200]>':
        for r in repos:
            list_of_repos.append(r['name'])
        #print list_of_repos
        return list_of_repos

def get_num_of_stars_and_forks(username='arshbot'):
    global fork_score 
    global star_score
    for r in list_of_repos:
        rc = requests.get('https://api.github.com/repos/'+username+'/'+r, auth=HTTPBasicAuth('arshbot', 'e172a7f23e13fc855016bb391bd5f504f3f13d86'))
        rc_json = rc.json()
        fork_score += rc_json['forks']
        star_score += rc_json['stargazers_count']

def get_num_of_github_commits(username='arshbot'):
    global list_of_repos
    global commit_score
    for r in list_of_repos:
        rc = requests.get('https://api.github.com/repos/'+username+'/'+r+'/commits', auth=HTTPBasicAuth('arshbot', 'e172a7f23e13fc855016bb391bd5f504f3f13d86'))
        if str(r) == '<Response [404]>':
            print "Shit ain't found for your repo: "+r
            break
        repos=rc.json()
        commit_score+=len(repos)

"""
An simple tool to pull GitHub Traffic Statics for a repository
"""

import json
import urllib2

auth_token = 'token ' + raw_input("GitHub personal access token: ")

gh_api_url = 'https://api.github.com'
repo_path = raw_input("GitHub repo (username_or_orgname/reponame): ")
traffic_stat_list = ['clones', 'views', 'popular/referrers', 'popular/paths']

for traffic_stat in traffic_stat_list:
    url = gh_api_url + '/repos/' + repo_path + '/traffic/' + traffic_stat
    print url
    req = urllib2.Request(url)
    req.add_header('Authorization', auth_token)
    responce = json.loads(urllib2.urlopen(req).read())
    formatted_responce = json.dumps(responce, indent=2)
    print formatted_responce

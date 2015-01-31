#Make sure pygithub3 is installed in python libraries
#sudo pip intsall pygithub3

from pygithub3 import Github

source=Github().repos.list_contributors(user="poise", repo="python")

for x in source:
    for resource in x:
        print resource

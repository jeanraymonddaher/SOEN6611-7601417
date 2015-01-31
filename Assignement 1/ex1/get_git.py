#make sure pygithub is installed

import urllib2
import urllib
import sys
import re
import git
import os
from git import Repo


print "Welcome to get git, let's find the repositories and clone them !"
file=sys.argv[1]+".txt";
f=open(file);
array={};
i=0;

for line in f:
    array[i]=line.strip();
    i=i+1;


url=array[0];
line0=url.split("=",1);
url=line0[1]+"/";
finalurl=url.rstrip();


directory=array[1];
line1=directory.split("=",1);
finaldirectory=line1[1];

#open webpage and store html in response
response = urllib.urlopen(finalurl);
response=response.read();
#print response;

#searchObj=re.findall(r'http.*github\.com.*', response);
searchObj=re.findall(r'http.*github\.com.*\.git', response);

print "Here are our repositories :"

#os.chdir(os.getcwd()+finaldirectory)
directory=os.getcwd()+finaldirectory

if not os.path.exists(directory):
    os.makedirs(directory)


x=set()
for i in searchObj:
    item=i.split("\"",1);
    temp=item   
    x.add(temp[0])
    #print os.getcwd()

os.chdir(directory)

bool=False

for i in x:
    bool=True
    print i+" Cloning"
    git.Git().clone(i)

if (bool==False):
    print("No repositories found, A repository must be of the format http...github... and end with a .git extension");


import sys
import os
import urllib
import time
import random

print "lets find some bug info"

file=sys.argv[1]+".txt";
f=open(file);
array={};
i=0;

for line in f:
    #print line
    array[i]=line.strip();
   # print array[i]
    i=i+1;

url=array[0]
url=url.split('=',1)
url=url[1]
tag=array[1]
tag=tag.split('=',1)
tag=tag[1]
bug_start=array[2]
bug_start=bug_start.split('=',1)
bug_start=bug_start[1]
bug_end=array[3]
bug_end=bug_end.split('=',1)
bug_end=bug_end[1]
max_timeout_secs=array[4]
max_timeout_secs=max_timeout_secs.split('=',1)
max_timeout_secs=max_timeout_secs[1]
root_directory=array[5]
root_directory=root_directory.split('=',1)
root_directory=root_directory[1]

print url
print tag
print bug_start
print bug_end
print max_timeout_secs
print root_directory

directory=os.getcwd()+root_directory
#os.chdir(directory)

if not os.path.exists(directory):
    os.makedirs(directory)

bug_range=int(bug_end)-int(bug_start)

for i in range(bug_range+1):
    url_for_search=url+"/browse/"+str(tag)+"-"+str(bug_start)
    savefile= urllib.URLopener()
    save_directory=directory+"/"+str(bug_start)+".txt"
    savefile.retrieve(url_for_search, save_directory)
    print "Downloading bug # " +str(bug_start)
    random_timeout=random.randrange(1,int(max_timeout_secs))
    print "timeout=" +str(random_timeout)
    time.sleep(random_timeout)
    bug_start=int(bug_start)+1
    


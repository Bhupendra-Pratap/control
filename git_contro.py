import os
from random import randint

# command used git commit --date="x days ago" -m "message"

for i in range(1, 50):

    for j in range(0, randint(0,3)):
        d = str(i)+' days ago '
        with open('test.txt','a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push -u origin main')

#hello
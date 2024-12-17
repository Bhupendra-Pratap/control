import os
from random import randint

# command used git commit --date="x days ago" -m "message"

for i in range(1, 100):

    for j in range(0, randint(1,10)):
        d = str(i)+' days ago '
        with open('test.txt','a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push -u origin main')
import os
import subprocess
from datetime import datetime

dtnow = datetime.now().strftime('%d%m%Y%H%M%S') #generate datetime for filename as of create time.

def tracert():
    tr = subprocess.run(['tracert',ip], shell = True, stdout=f, text = True)

print('*' * 60)
ip = input('Traceroute: ')
iterations = int(input('Iterations: '))
count = 0
print('-' * 60)

with open(f'tracert_{ip}_{dtnow}.txt','w') as f:
    while count < iterations:
        tracert()
        print(f'Iteration {count + 1} Done.')
        count += 1

print('-' * 60)
print('Traceroute for ' + ip + ' Complete')
print('-' * 60)

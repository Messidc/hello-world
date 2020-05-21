# import os
# def find_file(x, path):
#     for root, dirs, files in os.walk(path):        
#         for file in files:            
#             if x in file:                
#                 print(os.path.join(root, file))
                

# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()


print(multiprocessing.cpu_count())
import threading

#
local_school=threading.local()

def process_std():
    std=local_school.student
    print('Hello,%s(in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    local_school.student=name
    process_std()

t1=threading.Thread(target=process_thread,args=('Fuck',))
t2=threading.Thread(target=process_thread,args=('Thank',))

t1.start()
t2.start()
t1.join()
t2.join()




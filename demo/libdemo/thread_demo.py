import threading


class PrintThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print(f'Child : {i}')


t = PrintThread()
t.start()
print(f'Count  = {threading.active_count()}')
for i in range(1, 11):
    print(f'Main : {i}')

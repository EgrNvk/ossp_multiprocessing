# import threading
# import tkinter as tk
#
# def hello():
#     print('Hello world!')
#
# t = threading.Thread(target=hello);
# # t.start()
# # t.join()


# import threading
#
# def hello(i):
#     print(f'Hello world! {i} step!')
#
# t = threading.Thread(target=hello, args=[1]);
# t.start()








import threading
import time

def hello(name):
    print('Thread start')
    print(f"Hello, {name}")
    time.sleep(2)
    print('Thread end')



print("Main start")
treads = []

for i in range(10):
    tmpTread = threading.Thread(target=hello, args=[f'Name___{i}'])
    tmpTread.start()
    treads.append(tmpTread)

for i in range(10):
    treads[i].join()

print("Main end")
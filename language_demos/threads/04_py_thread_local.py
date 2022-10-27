""" py thread local """

import time
import threading

mydata = threading.local()

def fn2() -> None:
    """ fn2 """
    time.sleep(1)
    print(mydata.msg)

def fn1(msg: str) -> None:
    """ fn1 """
    time.sleep(1)
    print("assign " + msg + " to thread local")
    mydata.msg = "python is cool, " + msg
    time.sleep(1)
    fn2()


thread1 = threading.Thread(target=fn1, args=("thread1",))
thread1.start()

thread2 = threading.Thread(target=fn1, args=("thread2",))
thread2.start()


thread1.join()
thread2.join()



print("all done")
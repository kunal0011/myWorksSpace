import threading


class Foo:
    def __init__(self):
        self.first_done = threading.Lock()
        self.second_done = threading.Lock()

        # Initially, the locks are acquired (locked), so threads will be blocked
        self.first_done.acquire()
        self.second_done.acquire()

    def first(self, printFirst):
        # printFirst() outputs "first".
        printFirst()
        # Release the first lock so the second thread can proceed
        self.first_done.release()

    def second(self, printSecond):
        # Wait until the first thread releases the first lock
        self.first_done.acquire()
        # printSecond() outputs "second".
        printSecond()
        # Release the second lock so the third thread can proceed
        self.second_done.release()

    def third(self, printThird):
        # Wait until the second thread releases the second lock
        self.second_done.acquire()
        # printThird() outputs "third".
        printThird()


def printFirst():
    print("first", end='')


def printSecond():
    print("second", end='')


def printThird():
    print("third", end='')


foo = Foo()

# Creating the threads
thread1 = threading.Thread(target=foo.first, args=(printFirst,))
thread2 = threading.Thread(target=foo.second, args=(printSecond,))
thread3 = threading.Thread(target=foo.third, args=(printThird,))

# Starting the threads
thread3.start()
thread1.start()
thread2.start()

# Joining the threads
thread1.join()
thread2.join()
thread3.join()

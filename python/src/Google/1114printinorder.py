"""
LeetCode 1114: Print in Order

Problem Statement:
Suppose we have a class Foo with three functions: first(), second(), and third().
The same instance of Foo will be passed to three different threads:
- Thread A calls first()
- Thread B calls second()
- Thread C calls third()
Design a mechanism to ensure that second() is executed after first(), and third() is executed after second().

Logic:
1. Use threading.Lock() to enforce execution order
2. Create two locks: first_done and second_done
3. Initially acquire both locks to block second and third
4. In first(): release first_done lock
5. In second(): wait for first_done, then release second_done
6. In third(): wait for second_done
7. This ensures the desired execution order regardless of thread start order

Time Complexity: O(1) for each method
Space Complexity: O(1) for storing locks
"""

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


def test_print_in_order():
    def run_test(start_order):
        output = []
        
        def custom_first():
            output.append("first")
            
        def custom_second():
            output.append("second")
            
        def custom_third():
            output.append("third")
        
        foo = Foo()
        threads = []
        thread_funcs = {
            1: (foo.first, custom_first),
            2: (foo.second, custom_second),
            3: (foo.third, custom_third)
        }
        
        # Create and start threads in the specified order
        for i in start_order:
            method, print_func = thread_funcs[i]
            thread = threading.Thread(target=method, args=(print_func,))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
            
        return output
    
    # Test case 1: Start order [1,2,3]
    result1 = run_test([1,2,3])
    assert result1 == ["first", "second", "third"], f"Test case 1 failed. Expected ['first', 'second', 'third'], got {result1}"
    print("Test case 1 passed: Normal order")
    
    # Test case 2: Start order [3,1,2]
    result2 = run_test([3,1,2])
    assert result2 == ["first", "second", "third"], f"Test case 2 failed. Expected ['first', 'second', 'third'], got {result2}"
    print("\nTest case 2 passed: Third thread starts first")
    
    # Test case 3: Start order [2,3,1]
    result3 = run_test([2,3,1])
    assert result3 == ["first", "second", "third"], f"Test case 3 failed. Expected ['first', 'second', 'third'], got {result3}"
    print("\nTest case 3 passed: Second and third threads start before first")
    
    print("\nAll test cases passed!")

if __name__ == "__main__":
    test_print_in_order()

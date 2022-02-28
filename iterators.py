from itertools import count
import os
import time

class FiboIter:
    def __init__(self,max : int):
        self.max = max
        
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.buffer = 0
        self.count = 0
        return self

    def __next__(self):
        if self.buffer + self.n2 < self.max:
            if self.count == 0:
                self.count +=1
                return self.n1
            elif self.count == 1:
                self.count+=1
                return self.n2
            else:
                self.buffer = self.n2 + self.n1
                self.n2, self.n1 = self.buffer, self.n2
                self.count +=1
                return self.buffer
        else:
            raise StopIteration
            

def Fibonacci(num_max : int):
    fib = FiboIter(num_max)
    for element in fib:
        print(element)
        time.sleep(0.1)

    
def run():
    Fibonacci(int(input("ingrese un numero: ")))


if __name__ == "__main__":
    run()

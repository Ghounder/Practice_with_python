import time

def fibo_gen(max : int):
    n1 = 0
    n2 = 1
    count = 0
    max = max
    buffer = n1 + n2
    while True:
        if buffer + n1< max:
            if count == 0:
                count +=1
                yield n1
            elif count == 1:
                count +=1
                yield n2
            else:
                buffer = n1 + n2
                n1, n2 = n2, buffer
                count+=1
                yield buffer


def run():
    fibonacci = fibo_gen(89)
    for element in fibonacci:
        print(element)
        time.sleep(0.1)


if __name__ == "__main__":
    run()
import functools
import time

'''
Napisz dekorator do logowania metryk. Przy wywołaniu dekorowanej funkcji powinien dopisać do pliku "log.txt" 
(lub go stworzyć, jeżeli jeszcze nie istnieje) wiersz postaci:
fun_name,execution_time_in_seconds,function_call_count
'''


class CountCalls:
    def __init__(self, fun):
        functools.update_wrapper(self, fun)
        self.fun = fun
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        start = time.time()
        result = self.fun(*args, **kwargs)
        end = time.time()
        row = f"{self.__name__},{end - start},{self.num_calls}"
        with open('log.txt', 'a+') as f:
            f.write(row + '\n')
        return result


@CountCalls
def f():
    print('hello')
    time.sleep(2)


if __name__ == '__main__':
    f()
    f()
    f()

import sys
import math

if 'PyPy' in sys.version:
    from _continuation import continulet
else:
    import threading

def digitsInFactorial(N):
    if N==1 or N==0:
        return 1
    else:
        return math.ceil(math.log10(math.factorial(N)))

def main():
    T=int(input())
    
    while(T>0):
        N=int(input())
        
        print(digitsInFactorial(N))
        
        T-=1


if __name__ == '__main__':
    if 'PyPy' in sys.version:

        def bootstrap(cont):
            call, arg = cont.switch()
            while True:
                call, arg = cont.switch(to=continulet(lambda _, f, args: f(*args), call, arg))

        cont = continulet(bootstrap)
        cont.switch()

        main()

    else:
        sys.setrecursionlimit(1 << 30)
        threading.stack_size(1 << 27)

        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()

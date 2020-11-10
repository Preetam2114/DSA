import sys
import math

if 'PyPy' in sys.version:
    from _continuation import continulet
else:
    import threading

def termOfGP(A,B,N):
    r = (B/A)
    return math.floor(A*(r**(N-1)))

def main():
    T=int(input())
    
    while(T>0):
        
        AB=[int(x) for x in input().strip().split()]
        A=AB[0]
        B=AB[1]
        
        N=int(input())
        
        print(math.floor(termOfGP(A,B,N)))
        
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

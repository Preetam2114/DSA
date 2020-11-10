import sys
import math

if 'PyPy' in sys.version:
    from _continuation import continulet
else:
    import threading

def quadraticRoots(a,b,c):
    D = (b**2) - (4*a*c)
    if D>=0:
        r1 = math.floor((-b-math.sqrt(D))/(2*a))
        r2 = math.floor((-b+math.sqrt(D))/(2*a))
        print(max(r1,r2),min(r1,r2))
    else:
        print("Imaginary")


def main():
    T=int(input())
    while(T>0):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        
        quadraticRoots(a,b,c)
        
        
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

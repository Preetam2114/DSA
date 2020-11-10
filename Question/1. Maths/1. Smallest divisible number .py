import sys
import math

if 'PyPy' in sys.version:
    from _continuation import continulet
else:
    import threading

def getSmallestDivNum(n):
    a = list(range(1,n+1))
    ans = a[0]
    for i in range(1,len(a)):
        ans = ans*a[i]//math.gcd(ans,a[i])
          
    return ans

def main():
    t=int(input())
    for tcs in range(t):
        n=int(input())
        print(getSmallestDivNum(n))


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

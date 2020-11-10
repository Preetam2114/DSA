import sys

if 'PyPy' in sys.version:
    from _continuation import continulet
else:
    import threading

def isPrime(N):
    if (N <= 1) : 
        return False
    if (N <= 3) : 
        return True
    if (N % 2 == 0 or N % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= N) : 
        if (N % i == 0 or N % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def main():
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        if(isPrime(N)):
            print("Yes")
        else:
            print("No")
            
        
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

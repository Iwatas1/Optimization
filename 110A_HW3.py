import numpy as np
import math

f=np.poly1d([1,-14,60,-70,0])
ro=(3-math.sqrt(5))/2
def Gold(a,b,f):
    while abs(a-b)>=1e-6:
        x_1=a+ro*(b-a)
        x_2=a+(1-ro)*(b-a)
        if f(x_1)<f(x_2):
            b=x_2
        else:
            a=x_1
    min=(a+b)/2
    return min

print("minimum of f(x) is at x=", Gold(0,2,f), "and value is ", f(Gold(0,2,f)))
#%%
def Fibonacci(a,b,f,eps):
    fib={"F_1":1, "F_2":2 }
    i=2
    while fib[f'F_{i}']<(1+2*eps)/(1e-6/2):
        i+=1
        fib[f'F_{i}']=fib[f'F_{i-1}']+fib[f'F_{i-2}']
    i=len(fib)
    while abs(a-b)>=1e-6: 
        ro = 1-(fib[f'F_{i-1}']/fib[f'F_{i}'])
        x_1 = a+ro*(b-a)
        x_2 = a+(1-ro)*(b-a)
        if i == 1:
            break
        if f(x_1)<f(x_2):
                b=x_2
        else:
            a=x_1
        i=i-1
    min=(a+b)/2
    return min

print("minimum of f(x) is at x=", Gold(0,2,f), "and value is ", f(Fibonacci(0,2,f,0.1)))

#%%
g=np.poly1d([1, -12.2, 7.45, 42])

g_prime=g.deriv()

def Newton(x,g,g_prime):
    x_k=x-g(x)/g_prime(x)
    while abs(x-x_k)>= 1e-6:
        x=x_k
        x_k=x-g(x)/g_prime(x)
    return x_k
    
print("Root of g(x) is at x=", Newton(12,g,g_prime))


#%%
g = np.poly1d([1, -12.2, 7.45, 42])

def Secant(x_0,x_1,g):
    while abs(x_0-x_1)>=1e-6:
        x_1_2 = x_1
        x_1=(g(x_1)* x_0 - g(x_0)* x_1)/(g(x_1)-g(x_0))
        x_0 = x_1_2 
    return x_1

print("Root of g(x) is at x=",Secant(13,12,g))
    
        









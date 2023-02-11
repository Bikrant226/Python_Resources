#1
for i in range(5):
    print(i)
for i in range(5,10):
    print(i)

#2
print(list(range(0,10,3)))
print(list(range(-10,-100,-30)))

#3
str=['This','is','a','beautiful','day']
str[4]='morning'
for i in range(len(str)):
    print(str[i])



#4 Break:
print('Break:')
for j in range(1,10):
    if(j==5):
        break   
    else:
        print(j)


#5 Continue:
print('Continue:')
for j in range(1,10):
    if(j==5):
        continue
    else:
        print(j)

#6 Functions:
print("Functions:")

def fib(n):
    a,b=0,1
    while(a<n):
        print(a,' ')
        a,b=b,a+b
fib(20)

#7 Lambda functions:
print("Lambda functions:")

def func(x):
    return lambda a:a+x
f=func(20)
print(f(10))
print(f(40))

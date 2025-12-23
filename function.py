def sum(a,b,c):
    print("sum of numbers", a+b+c)
sum(2,3,4)
# fuction overwriting
def sum(a,b,c,d):
    print("sum of numbers", a+b+c+d)
sum(2,3,4,5)

# arbitrary arguments
def sum(*args):
    sum = 0
for i in args:
    sum = s + i
    print("sum of numbers", sum)
    
    print(args)
    print(type(args))
sum(1,2,3)
sum(1,2,3,4)


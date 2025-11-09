
class Demo:
    # method1 using default arguments
    def add(self,a,b,c=0):
        return a+b+c
    # method2 using variable length  arguments
    def add2(self,*args):
        total = 0
        for arg in args:
            total += arg
        return total

d = Demo()
print(d.add(1,2))
print(d.add(1,2,3))
print(d.add2(1,2,3,4,5,6,8,9))
print(d.add2(1,2,3,7,8,5))
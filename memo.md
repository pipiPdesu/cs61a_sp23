如果你卡在哪里， 直接在github上搜代码

后六周的optional不做了先，回来有空再补

hw04的倒数第二道题一直ok跑不过，明明我本地就能跑过的

lab06 >>> iter(s)竟然是返回Iterator 

hw06的optional 被卡住力 看了题解 原来是这样啊

'''
class A():
    def g(self):
        print('??A')

class B():
    def g(self):
        print("dsfadasd")

a = A()
B.g(a)
'''
竟然可以这样父类实例调用子类函数 注意这样不符合oop self里面用了b独有的属性就会报错

'''
class A:
   x, y = 0, 0
   def __init__(self):
         return
class B(A):
   def __init__(self):
         return
class C(A):
   def __init__(self):
         return

print(A.x,B.x,C.x)
B.x = 2
A.x+=1
print(A.x,B.x,C.x)
'''
注意这里 b c都没有x属性
先给b套上了x属性 b的x就不是继承a的了 c的x是继承了a的 所以输出是1 2 1

args is bound to all positional arguments (which are all arguments passed without keywords), and kwargs is bound to all the keyword arguments.

完形填空真不会
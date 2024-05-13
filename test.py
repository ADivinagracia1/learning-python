print("hgello")

# x = 1
# y = 0
# z = 0 
# res = 2
# try:
#     z = z + 1
#     res = x/y
#     z = z+1
#     print("0")
# except ZeroDivisionError:
#     z = z + res
#     print("1")
# else:
#     z = z + 1
#     print("2")
# finally:
#     z = z + 1
#     print("3")
# z = z + 1
# print(z)


# bef = [1,2,3,4,5]
# def bar(lst):
#     return lst.append(7)
# aft = bar(bef)
# print(bef)
# print(aft)



# for n in range(2,10):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else:
#         print(n)




# from collections import defaultdict
# wl = ["pee", "poo", "pee"]
# wc =defaultdict(int)
# for w in wl:
#     wc[w] += 1
# print(wc)


# i, j = 150, 300
# if ((True == False) and (False in (False,))) == True:
#     print(i)
# elif (True == False) in (False,) == False:
#     print(j)
# else:
#     print("nops")
# print(False in (False,))


# def foo(n):
#     var1, var2 = 0, 1
#     while var1 < n: 
#         print(var1, end=' ')
#         var1 , var2 = var2, var1+var2
#     print()

# def bar(n):
#     res = []
#     var1, var2 = 0, 1
#     while var1 < n:
#         res.append(var1)
#         var1 , var2 = var2, var1+var2
#     return res


# l = [0,1,2,3,4,5,6]
# def f1(x):
#     return x*2
# def f2(x):
#     if x % 2 == 0: return True
# print([f1(x) for x in l if f2(x)])

# class vehicles:
#     count = 0
#     def __init__(self, value) -> None:
#         self.value = value
#         vehicles.count += 1
#     def getval(self):
#         return self.value
#     def getcount(self):
#         return vehicles.count
#     counter = classmethod(getcount)
# t1 = vehicles("Car")
# t2 = vehicles("Bus")
# t3 = vehicles("Bikes")
# print(t1.getval(), t2.getval(), vehicles.counter(), t2.getcount())

# class k:
#     def __init__(self) -> None:
#         self.__foo = 10
#     def mX(self):
#         self.__mY()
#         print(self.__foo)
#     def __mY(self):
#         self.__foo += 1
# o = k()

# o.k__mY()
# o.mX()
# # o.__mY()
# # o.__init()
# # o.__foo


# class foo(object):
#     def __str__(self) -> str:
#         return 'Testing'
#     def __repr__(self) -> str:
#         return 'Programming'
# print('{0!s} {0!r}'.format(foo()))

def f():
    yield True

try: 
    g = f()
    h = next(g)
    assert h is True
    print("True")
    h = next(g)
    assert h is None
    print("None")
except AssertionError:
    print("assertion failed")
except GeneratorExit:
    print("exit")
except StopIteration:
    print("stop")
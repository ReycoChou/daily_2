

def ip2int(addr):
   """将ip地址转化成整数"""
   id = [int(x) for x in addr.split('.')]
   return sum(id[i] << [24, 16, 8, 0][i] for i in range(4))



def andOr():
   """
   Python的and or布尔运算
   1.or返回第一个为真的式子，否则返回最后一个
   2.and返回第一个为假的例子，否则返回最后一个
   3. and or 比如 1 and v1 or v2: 类似 bool ？true：false这种三目运算符
   """
   print("1 and 3: ", 1 and 3)
   print("1 or 3: ", 1 or 3)
   print("0 or 1: ", 0 or 1)
   print("0 and 1: ", 0 and 1)
   print("0 and 1 or 3: ", 0 and 1 or 3)
   print("1 and 1 or 3: ", 1 and 1 or 3)




def isEqual():
   """
   Python的is 和 ==
   一般is是比较地址的，而==是比较内容的，类似Java中==是比较地址的，而equal是比较内容的，Python也类似Java可以重写__eq__
   使用is注意python对于小整数使用对象池存储问题:
      python对[-5,256]范围内的数进行了缓存(这是基于命令行，一些ide比如pycharm进行了优化，即使超过了256，使用is也是成立)
   使用is注意python关于字符串的intern机制存储:
      python中虽然字符串对象是不可变对象，但是python存在intern机制
      简单说就是维护一个字典，这个字典维护已经创建字符串(key)和它的字符串对象的地址(value),
      每次创建字符串对象都会和这个字典比较,没有就创建，重复了就用指针进行引用就可以了。相当于python对于字符串也是采用了对象池原理
      (但是注意：如果字符串（含有空格），不可修改，没开启intern机制，不共用对象。比如"a b"和"a b",这种情况使用is不成立的形式 只有在命令行中可以。使用pycharm同样是True，因为做了优化)
   """
   a, b = 1000, 1000
   print(f'a is b: {a is b} ##### a == b: {a == b} ##### {id(a)} ##### {id(b)}')
   a, b = 100, 100
   print(f'a is b: {a is b} ##### a == b: {a == b} ##### {id(a)} ##### {id(b)}')
   a, b = "aaa", "aaa"
   print(f'a is b: {a is b} ##### a == b: {a == b} ##### {id(a)} ##### {id(b)}')



def change():
   """
   Python 在 heap 中分配的对象分成两类：可变对象和不可变对象:
      不可变对象：int，string，float，tuple
      可变对象 ：list，dictionary
   python中变量存放的是对象的引用，例如a = 1，那么a是变量，1是对象，这里的1是int类型，属于不可变对象，不可变对象可以被多个变量共享，如b = 1，那么id(a) == id(b)的
   但是不可变对象不可被改变，如 a += 1 ==> a = 2，由于对象1不可变，此时id(a)已经变化
   而可变对象，比如list， a = [1, 2, 3], b = [1, 2, 3] a和b其实是不同的对象的，可变对象不被变量共享
   但是可变对象可以被改变，比如a.append(4), id(a)还是不变

   可变对象以及不可变对象在函数的传递，由于可变对象可以被改变，但是一般不允许函数改变，所以可变对象通过复制进行传递，而不可变对象可以通过引用调用
   """
   pass


def stringCommon():
   """
   字符串常用的方法，做题和面试需要掌握
   """
   val = "hello world"
   print(val.find('l'))
   print(val.index('l')) # 寻找某个字符的索引，找不到则返回-1
   #print(val.index('s')) # 寻找某个字符的索引，找不到则报错
   print(val.split(" ")[0])
   print(val.capitalize())  # 首字母大写，其他字母小写
   print(val.upper())  # 全部大写
   print(val.lower())  # 全部小写
   print(val.startswith("hello", 0, len(val)))  #用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查
   print(val.endswith("world"))
   print(val.strip())  # 去掉两侧空格，lstrip去掉左侧，rstrip去掉右侧
   print(val[0].isdigit())  # 判断是否是数字
   print(val[0].isalpha())  # 判断是否是字母
   print(val.swapcase())  # 大小写翻转

def dictCommon():
   """
   dict常用的方法，做题和面试需要掌握
   """
   # dict = {'a': 1, 'b': 2, 'c': 3}
   # for k in dict:  # 输出全部的键
   #    print(k)
   # for k, v in dict.items():  # 输出k，v
   #    print(k, v)
   #
   # dict.pop('a') # 删除键，如果没有会报错
   # dict.popitem() # 随机删除键
   # dict.update({'d': 4, 'e': 5})  # 增加一个新的字典
   v = dict.fromkeys(['k1', 'k2'], [])  # 批量导入
   v['k1'].append(666) # 都会导入，包括k2
   print(v)
   v['k1'] = 777
   print(v)
   # {'k1': [666], 'k2': [666]}
   # {'k1': 777, 'k2': [666]}

def listCommon():
   """
   list常用的方法，做题和面试需要掌握
   """
   l = [1, 2, 3, 4]
   l.append(5)
   l.insert(3, 6)  # 按照固定索引插入
   for i in l:
      print(i)
   l.extend([7,8,9])  # 增加一个新的list
   print(l.count(4))  # 计算某个元素出现次数
   print(l.index(4))  # 从列表中找出某个值第一个匹配项的索引位置
   l.reverse()  # 反向列表中元素


def copyCommon():
   """
   关于浅拷贝和深拷贝：
   浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象
   深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象
   直接赋值：其实就是对象的引用（别名）
   """
   l1 = [1, 2, 3]
   l2 = l1.copy()
   l2.append(4)
   print(l1, l2)
   import copy
   l3 = copy.deepcopy(l1)
   l3.append(4)
   print(l1, l3)


def trash():
   """
   python垃圾回收:看谷歌春招收藏夹
   """


def multipliers1():
   """
   返回四个lambda表达式，都是3 * x
   """
   return [lambda x : i * x for i in range(4)]
   # 怎么改成是 0 * x, 1 * x, 2 * x, 3 * x呢

def multipliers2():
   """
   返回四个lambda表达式，是 0 * x, 1 * x, 2 * x, 3 * x
   """
   return (lambda x : i * x for i in range(4)) # 返回生成器表达式



def mapAndfilter():
   def mul(x):
      return x * x
   def exclude(x):
      return x & 1 == 0

   l = [1, 2, 3, 4, 5]
   res = list(map(mul, l))  # 函数名和列表
   print(res)
   res = list(filter(exclude, l))  # 函数名和列表
   print(res)



def instanceAndtype():
   """
   isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
   isinstance() 与 type() 区别：
   type() 不会认为子类是一种父类类型，不考虑继承关系。
   isinstance() 会认为子类是一种父类类型，考虑继承关系。
   """
   a = 2
   print(isinstance(a, int))
   print(isinstance(a, str))


def zipAndzipped():
   a = [1, 2, 3]
   b = [4, 5, 6]
   zipped = zip(a, b)
   print(zipped)
   print(zip(*zipped))  # 理解为解压或者转置


def reduceTest():
   def add(x, y):
      return x + y
   l = [1, 2, 3]
   from functools import reduce
   print(reduce(add, l)) # 累加或者累乘什么的


"""
re的match和search区别？
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
re.search 扫描整个字符串并返回第一个成功的匹配。

什么是正则的贪婪匹配？
尽可能匹配长的字符串，成功匹配之后还会继续向右匹配
"""



"""
print(( i % 2 for i in range(10) ))
#  <generator object <genexpr> at 0x00000000020CEEB8> 生成器
# 在Python中，有一种自定义迭代器的方式，称为生成器（Generator）。
# 定义生成器的两种方式：
# 1.创建一个generator，只要把一个列表生成式的[]改成()，就创建了一个generator：
# generator保存的是算法，每次调用next()，就计算出下一个元素的值，直到计算到最后一个元素，
没有更多的元素时，抛出StopIteration的错误。
# 2.定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
而是一个generator 
"""

"""
Python的链式比较：
在其他语言中，有一个变量x，如果要判断x是否大于1，小于5，可能需要这样写代码：
   if (1 < x and x < 5)
但是在Python中，可以这样写代码：
   if 1 < x < 5
Python能够正确处理这个链式对比的逻辑

在Python中，你可能会发现这样一个奇怪的现象：
>>> 2 == 2 > 1
True
>>> (2 == 2) > 1
False
>>> 2 == (2 > 1)
False
回到最开始的问题上，==等于符号和<小于符号，本质没有什么区别。
所以实际上2==2>1也是一个链式对比的式子，它相当于2==2 and 2>1。此时，这个式子就等价于True and True。所以返回的结果为True
"""




if __name__ == '__main__':
   reduceTest()

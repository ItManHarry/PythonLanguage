#列表声明
l1 = [1,2,3,4,5,6]
print('List 1 : ', l1)
#函数生成
l2 = list(range(1,10))
print('List 2 : ', l2)
#元组声明
t1 = (1,2,3,4,5)
print('Tuple 1 : ', t1)
#函数生成
t2 = tuple(range(1,20))
print('Tuple 2 : ', t2)
#只有一个元素的元组必须加逗号','
t3 = (1,)
print('Tuple 3 : ', t3)
#元组转换为列表
l = list(tuple(range(1,10)))
print('List from tuple : ', l)
#列表转换元组
l = [1,2,3,4,5]
t = tuple(l)
print('Tuple from list : ', t)
#取一个、多个列表/元组数据(索引不可越界)
print('The first element of the list : ', l[0])
print('The third and forth elements of the list : ', l[2:4])
print('The first element of the tuple : ', t[0])
print('The third and forth elements of the tuple : ', t[2:4])
#列表元组相加
l1 = [1,2,3]
l2 = ['a','b','c']
l = l1 + l2
print('l1 and l2 : ', l)
t1 = (10,20,30)
t2 = ('e','f','g')
t = t1 + t2
print('t1 and t2 : ', t)
#列表元组元素加倍
print('Double list :', l * 2)
print('Double tuple :', t * 2)
print('Double string :', 'abcdef' * 2)
#列表元组长度、最大最小值
l = list(range(1,5))
t = tuple(range(1,10))
print('Length of the list : ', len(l))
print('Max value of the list : ', max(l))
print('Min value of the list : ', min(l))
print('Length of the tuple : ', len(t))
print('Max value of the tuple : ', max(t))
print('Min value of the tuple : ', min(t))
#序列封包
p = 1,3,4,'a',3.14
print('Type of p : ', type(p), ', and value is : ', p)
#全部解包
ps = [1,2,3,'Python']
a,b,c,d = ps
print('a is : ', a, ', b is : ', b, ', c is : ', c, ', d is : ',d)
#部分解包
a, *b = ps
print('a is : ', a, ', b is : ', b)
a, *b, c = ps
print('a is : ', a, ', b is : ', b, ', c is : ', c)
#追加、删除、替换元素
l = [1,2,3]
print('List is : ', l)
#追加单个元素
l.append('Java')
l.append('Groovy')
l.append('Python')
#追加列表
l.append(list(range(1,10)))
l.extend(tuple(range(0,5)))
print('After append elements : ', l)
del l[0]
del l[2]
print('After delete elements : ', l)
#插入数据
l.insert(3, 'Go')
print('After insert element : ', l)
l.insert(2, [100,200,300])
print('After insert list : ', l)
#移除元素-remove(移除第一个匹配的元素)
l.remove('Groovy')
print('After remove : ', l)
#更改元素值
l[2] = 'Java'
print('After change element : ', l)
l[3:5] = 'Harry'
print('Now the list is : ', l)
l = []
s = 'Harry'
l[0:] = s
print('List is : ', l)
#统计元素个数
print('Count of r : ', l.count('r'))
#弹出元素
l.pop()
print('Remove last : ', l)
#翻转
l.reverse()
print('After reverse elements : ', l)
#排序(默认升序排列)
l = [1,4,2,35,39,12,23,45,21,48]
print('Before sorted : ', l)
l.sort()
print('After sorted : ', l)
l.reverse()
print('After reverse : ', l)
#去重 - 方式一
l = [1,2,5,23,12,21,12,34,43,34,1,2,45,54,43]
print('The raw list : ', l)
nl = []
for e in l:
    if e not in nl:
        nl.append(e)
nl.sort()
print('Unique elements 1 : ', nl)
#方式二 - set()集合
#print('The raw list : ', l)
st = set(l)
nl = list(st)
nl.sort()
print('Unique elements 2 : ', nl)
import itertools as its
l.sort()
it = its.groupby(l)
#print('Type of it : ', type(it))
nl = []
for e in it:
    #print('Element : ', type(e))
    nl.append(e[0])
nl.sort()
#print('The raw list : ', l)
print('Unique elements 3 : ', nl)
#字典
#基本方式创建
d = {'a':100,'b':200,'c':300}
print('Dictionary : ', d)
#使用dict函数创建，参数为二维列表：
# 参数格式一：[['a',100],['b',200]...]
# 参数格式二：[('a',100),('b',200)...]
# 参数格式三：(['a',100],['b',200]...)
# 参数格式四：(('a',100),('b',200)...)
d = dict([['a',1000],['b',2000],['c',3000]])
print('Dictionary : ', d)
d = dict([('aa',1000),('bb',2000),('cc',3000)])
print('Dictionary : ', d)
d = dict((['aaa',1000],['bbb',2000],['ccc',3000]))
print('Dictionary : ', d)
d = dict([['aaaa',1000],['bbbb',2000],['cccc',3000]])
print('Dictionary : ', d)
#指定关键字创建字典
d = dict(a=1000,b=2000,c=3000)
print('Dictionary : ', d)
#数据访问
print('Dictionary element : ', d['a'])
print('Dictionary element : ', d.get('a'))
#修改值，如果存在key则直接修改对于的值，不存在则新增元素
d['a'] = 6000
print('Dictionary : ', d)
d['d'] = 5000
#update函数，参数和dict函数一样，还可以传入字典作为参数
d.update({'a':'a','b':'b'})
d.update([['c','c'],['d','d']])
d.update((('e','e'),('f','f')))
print('Dictionary : ', d)
#删除元素
del d['d']
print('Dictionary : ', d)
#判断是否存在某个元素
print('a in dictionary ? ', 'a' in d)
#清空字典
d.clear()
print('Now the ditionary is : ', d)
#遍历字典
d = {'a':'a','b':'b','c':'c','d':'d'}
for k, v in d.items():
    print('Key is : ', k, ', value is : ', v)
#取默认值
v = d.setdefault('e', 100)
print('Dictionary : ', d)
print('Element e : ', d['e'])
#根据key列表创建字典
d = dict.fromkeys(['A','B','C','D'])
print('Dictionary : ', d)
#key列表创建字典同时指定默认值
d = dict.fromkeys(['A','B','C','D'], '0')
print('Dictionary : ', d)
#字符串格式化输出
#元组匹配
s = 'The book <<%s>>\'s price is %d'
print(s %('Python', 120))
#名称匹配
s = 'The book <<%(name)s>>\'s price is %(price)d'
print(s %{'price':140,'name':'Java'})
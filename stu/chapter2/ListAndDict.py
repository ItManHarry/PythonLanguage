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

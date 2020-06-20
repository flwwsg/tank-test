classmate = ['bo', 'li', 'zhang']
# 列出所有名字
classmate
# 获取list元素的个数
len(classmate)
# 用索引来访问list中每个元素
# 访问‘bo’元素
classmate[0]
# 访问最后一个元素
classmate[-1]
# list是一个有序表
# 增加元素到末尾
classmate.append('hong')
# 增加元素到指定位置
classmate.insert(1,'dong')
print(classmate)
# 删除list末尾的元素,pop(i) i为元素的位置
classmate.pop(1)
# 替换某个元素的值
classmate[0]='gong'
# list里可以是其它list
classmate=['2','4',['li','si']]

# tuple 有序列表，初始化后，不能修改指定元素的对应位置
# tuple中t值改变
t=('a','b',['c','d'])
t[2][0]='C'
t[2][1]='D'

colors=('green','yellow','red')
# 定义只有一个元素时
color=('red',)
# if
age=20
if age>10:
    print('青少年')
elif age>18:
    print('成年人')
# if简写
x=0
if x:
    print('简写的if')
# input() 读取用户的输入
'''date=input('date')
# input返回类型str转换为int
date=int(date)
if date>19900101:
    print("90后")'''
# range()生成一个整数序列,list()函数转换为list
list(range(10))
# 求1-10的和
sum=0
for x in range(10):
    sum=sum+x
print(sum)

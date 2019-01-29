

#作业
import random
r1=random.randint(0,9)
r2=random.randint(0,9)
r3=random.randint(0,9)
list=[]
s=input("请输入一个0-9之间的数字:")
#s.isdigit() 所有字符都是数字，为真返回 Ture，否则返回 False。
while s.isdigit()==False:
    s = input("您输入的不是数字，请输入一个0-9之间的数字:")
while int(s)>9 or int(s)<0:
    s=input("您输入数字不在0-9间，请输入0-9间的数字:")
while True:
    if r1!=r2 and r1!=r3 and r2!=r3:
        break
    else:
        r1=random.randint(0,9)
        r2=random.randint(0,9)
        r3=random.randint(0,9)
    print(r1,r2,r3)
list.append(r1)
list.append(r2)
list.append(r3)

if int(s)==r1:
    print("获得第一名")
if int(s)==r2:
    print("获得第二名")
if int(s)==r3:
    print("获得第三名")
else:
    a=int(input("用户未得奖,(按1表示重新开始，按2表示结束游戏）"))
    if a==1:
        s=input("请输入一个0-9之间的数字:")
    if a==2:
        exit()
print(list)
     



"""
1判断语句（要求掌握多条件判断：
计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。比如，输入用户年龄，根据年龄打印不同的内容，在 Python 程序中，用 if 语
句实现

"""
"""age = 20
if age >= 18:
    print 'your age is', age
    print 'adult
"""

"""
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars: 
if car == 'bmw':
    print(car.upper())
else:
    print(car.title())
"""
"""
1.1 
每条if 语句的核心都是一个值为True 或False 的表达式，这种表达式被称为条件测试 。Python根据条件测试的值为True 还是False 来决定是否执行if 语句中的代码。如果
条件测试的值为True ，Python就执行紧跟在if 语句后面的代码；如果为False ，Python就忽略这些代码。
"""
"""
1.2 if-else 语句
"""

"""
age = 17 
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?") 
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

"""
"""
1.3 if-elif-else 结构
age = 12
if age < 4:
    print("Your admission cost is $0.") 
elif age < 18:
    print("Your admission cost is $5.") 
else:
    print("Your admission cost is $10."
"""
"""
2、循环语句
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
"""
"""
3、迭代
如果给定一个 list 或 tuple，我们可以通过 for 循环来遍历这个 list 或 tuple，这种遍历我们
称为迭代（Iteration）。
在 Python 中，迭代是通过 for ... in 来完成的，而很多语言比如 C 或者 Java，迭代 list
是通过下标完成的，比如 Java 代码：
for (i=0; i<list.length; i++) {
 n = list[i];
>>> from collections import Iterable>>> isinstance('abc', Iterable) # str 是否可迭代
True>>> isinstance([1,2,3], Iterable) # list 是否可迭代
True>>> isinstance(123, Iterable) # 整数是否可迭代
Fal


4、三目式

python中的格式为

为真时的结果 if 判定条件 else 为假时的结果  1

实例:

print(1 if 5>3 else 0) 1

是先输出结果，再判定条件 
输出1，如果5大于3，否则输出0

一般用于判断赋值中，例如：


x,y = 50,25
small = x if x<y else y
print(small)123

还可以嵌套使用，还可以多层嵌套


a,b,c=10,20,6
min_num = a if a<b and a<c else (b if b<a and b<c else c)
print(min_num)


5、生成器

通过列表生成式，我们可以直接创建一个列表，但是，受到内存限制，列表容量肯定是有限的，而且创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
　　所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间，在Python中，这种一边循环一边计算的机制，称为生成器：generator
　　生成器是一个特殊的程序，可以被用作控制循环的迭代行为，python中生成器是迭代器的一种，使用yield返回值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。
　　生成器类似于返回值为数组的一个函数，这个函数可以接受参数，可以被调用，但是，不同于一般的函数会一次性返回包括了所有数值的数组，生成器一次只能产生一个值，这样消耗的内存数量将大大减小，而且允许调用函数可以很快的处理前几个返回值，因此生成器看起来像是一个函数，但是表现得却像是迭代器
python中的生成器
　　要创建一个generator，有很多种方法，第一种方法很简单，只有把一个列表生成式的[]中括号改为（）小括号，就创建一个generator

（1）通常的for..in...循环中，in后面是一个数组，这个数组就是一个可迭代对象，类似的还有链表，字符串，文件。他可以是a = [1,2,3]，也可以是a = [x*x for x in range(3)]。
它的缺点也很明显，就是所有数据都在内存里面，如果有海量的数据，将会非常耗内存。
　　（2）生成器是可以迭代的，但是只可以读取它一次。因为用的时候才生成，比如a = (x*x for x in range(3))。!!!!注意这里是小括号而不是方括号。
　　（3）生成器（generator）能够迭代的关键是他有next()方法，工作原理就是通过重复调用next()方法，直到捕获一个异常。
　　（4）带有yield的函数不再是一个普通的函数，而是一个生成器generator，可用于迭代
　　（5）yield是一个类似return 的关键字，迭代一次遇到yield的时候就返回yield后面或者右面的值。而且下一次迭代的时候，从上一次迭代遇到的yield后面的代码开始执行
　　（6）yield就是return返回的一个值，并且记住这个返回的位置。下一次迭代就从这个位置开始。
　　（7）带有yield的函数不仅仅是只用于for循环，而且可用于某个函数的参数，只要这个函数的参数也允许迭代参数。
　　（8）send()和next()的区别就在于send可传递参数给yield表达式，这时候传递的参数就会作为yield表达式的值，而yield的参数是返回给调用者的值，也就是说send可以强行修改上一个yield表达式值。
　　（9）send()和next()都有返回值，他们的返回值是当前迭代遇到的yield的时候，yield后面表达式的值，其实就是当前迭代yield后面的参数。
　　（10）第一次调用时候必须先next（）或send（）,否则会报错，send后之所以为None是因为这时候没有上一个yield，所以也可以认为next（）等同于send(None)
　举例如下：
1
2
3
4
5
6
7
8
9
10
#列表生成式
lis = [x*x for x in range(10)]
print(lis)
#生成器
generator_ex = (x*x for x in range(10))
print(generator_ex)
 
结果：
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
<generator object <genexpr> at 0x000002A4CBF9EBA0>

def fib(max):
    n,a,b =0,0,1
    while n < max:
        a,b =b,a+b
        n = n+1
        print(a)
    return 'done'
 
a = fib(10)
print(fib(10))

"""












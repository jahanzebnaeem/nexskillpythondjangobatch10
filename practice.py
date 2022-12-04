# mySalary = 100000
# myTax = 16/100
# myPayableTax = mySalary*myTax
# print(mySalary-myPayableTax)

# print(len('Welcome to today\'s lecture'))

# s = 'My name is {a} and my age is {b}'.format(a='Faisal', b=19)
# # print(s)
# # s = 'Hassan'
# print(s)

# my_list = [1,2,3,4]
# # # my_list[1] = 5
# # my_list.append(5)
# # print(my_list)
# # my_list.pop(0)
# # print(my_list)
# # my_list.pop(0)
# # print(my_list)
# my_list.reverse()
# print(my_list)
#
# lst_1=[1,2,3]
# lst_2=[4,5,6]
# lst_3=[7,8,9]
#
# matrix = [lst_1,lst_2,lst_3]
#
# my_matrix = [matrix[1][1:], matrix[2][1:]]
#
# print(my_matrix)

# my_dict = {'name': 'Jahanzeb', 'age': '75', 'product': [2, 333, 675]}
# # my_dict['product'][1] -= 123
# # print(my_dict['product'][1])
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# t = (1,2,3,1,2,4,6,1)
# # t[2] = 'Ali'
# t.add('Ali')
# print(t)

# y = set()
# y.add(1)
# y.add(2)
# y.add(1+2)
# y.add(1)
# y.add(2)
# print(y)

# l = [1,1,2,2,3,4,5,6,1,1]
# se = set(l)
# print(se)

# if 1==1:
#     print('Hello')
# else:
#     print('world!')
#     print('Hello again')

# if 1 == 1:
#     print('first')
# elif 3 == 3:
#     print('middle')
# else:
#     print('Last')

# seq = [1,2,3,4,5]
#
# for item in seq:
#     print(item+item)

# ages = {"Sam":3,"Frank":4,"Dan":29}
#
# for key in ages:
#     print("This is the key")
#     print(key)
#     print("This is the value")
#     print(ages[key])
#     print("\n")
#
# mypairs = [(1,10),(3,30),(5,50)]
#
# for tup1, tup2 in mypairs:
#     print(tup1)
#     print(tup2)

# my_list = list(range(1,10))
# print(my_list)

# for i in range(0, 10, 2):
#     print(i)

# x = [1,2,3,4]

# out = []
# for item in x:
#     out.append(item**2)
#
# print(out)
#
# out = [item**2 for item in x]
# print(out)

# userName = input("Enter your name: ")
# print("Welcome to this lecture " + userName)

# print(type(1))
# print(type([]))

# class Sample():
#     pass
#
# x = Sample()
#
# print(type(x))

# class Dog():
#
#     species = 'mammal'
#
#     def __init__(self,breed):
#         self.breed = breed
#
# sam = Dog(breed='Lab')
# bil = Dog(breed='Huskie')
#
# print(sam.species)
# print(bil.species)

# class Circle():
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def area(self):
#         return self.radius * self.radius * Circle.pi
#
#     def setRadius(self, radius):
#         self.radius = radius
#
#     def getRadius(self):
#         return self.radius
#
# c = Circle()
#
# print ('Radius is :', c.getRadius())
# c.setRadius(2)
# print ('Radius is: ',c.getRadius())
# print ('Area is: ',c.area())

# class Animal():
#     def __init__(self):
#         print ("Animal created")
#
#     def whoAmI(self):
#         print ("Animal")
#
#     def eat(self):
#         print ("Eating")
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print ("Dog created")
#
#     def whoAmI(self):
#         print ("Dog")
#
#     def bark(self):
#         print ("Woof!")
#
# d = Dog()
# d.whoAmI()
# d.eat()
# d.bark()
# d.length()

# class Book():
#     def __init__(self, title, author, pages):
#         print ("A book is created")
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return ("Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages))
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print ("A book is destroyed")
#
# book = Book("Python Rocks!", "Jahanzeb Naeem", 159)
#
# #Special Methods
# print (book)
# print (len(book))
# del (book)

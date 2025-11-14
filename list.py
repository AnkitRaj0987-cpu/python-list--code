a = ["ankit", "raj", "kumar",]
print(a)
num = [10, 20, 30, 40, 50]
a = num[2]
print(a)
colors = ["red", "blue"]
colors.append(3)

colors.append("green")
print(colors)

lis = ["cat", "dog","cow"]
lis[1] = "tiger"
print(lis)

names = ["ankit", "rahul", "neha"]
for i in names:
    print(i)
cities = ["delhi","mumbai","kolkata"]
cities.insert(1,"chennai")
print(cities)

nums = [1,2,3,4,2,5]
nums.remove(2)
print(nums)

letters = ["a","b","c","d"]
popedvalue= letters.pop(2)
print(popedvalue)
marks = [50,10,90,30,70]
marks.sort()
print(marks)
print(sorted(marks))
marks.reverse()
print(marks)
nums = [12,45,7,89,34]
max = max(nums)
print(max)

fruits = ["apple", "banana", "apple","mango"]
count = fruits.count("apple")
print(count)

list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2) #or
list1.extend(list2)
print(list1)


data = [1,2,3,4,4,5]
d = list(set(data))
print(d)

marks = [40,10,90,50,70]
marks.sort()
value = marks[-2]
print(value)


data = [[1,2],[3,4,5],[6]]
flatlist = [x for m in data for x in m]
print(flatlist)

pairs = [(1,2), (5,1),(2,2)]
sorted = sorted(pairs, key = lambda x: x[1])
print(sorted)

nums = [2,4,9,34,5,3,7,9]
evennums = [x for x in nums if x%2==0]
print(evennums)



a = [1,2,3,4,5,6,7]
b = [4,5,6,7]
commonelement = list(set(a) &set(b))
print(commonelement)
#or
commonelement = [x for x in a if x in b]
print(commonelement)

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
square = [x*x for x in num if x%3==0]
print(square)




# first = int(input("enter first : "))
# second = int(input("enter first : "))
# print("sum =a",first + second)
# side = float(input("enter square side : "))
# print("area =",side*side))
# side = float(input("enter square side :"))
# print("area =",side ** 2)

# # a = float(input("enter square first :"))
# # b = float(input("enter square second :"))
# # print("average =",(a + b)/2)
# # '''
# # a = int(input("enter square first :"))
# # b = int(input("enter square second :"))
# # print(a >= b)
# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a pice of furniture","lisst of fact on figuer"]
# # }
# # print(dictionary)
# # subjects = {
# #     "python","java","C++","python","javascript","java",
# #     "python","java","C++", "C"
# # }
# # print(subjects)
# # print(len(subjects))
# # marks = {}

# # x = i9 , 9.0}
# # print(value)
# # value = {9 , "9.0"}
# # print(value)nt(input("enter phy : "))
# # marks.update({"phy" : x})

# # x = int(input("enter maths : "))
# # marks.update({"maths" : x})

# # x = int(input("enter urdu : "))
# # marks.update({"urdu" : x})

# # x = int(input("enter chem : "))
# # marks.update({"chem" : x})

# print(marks)
# value = {
# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)
# i = 1
# while i<=100:
#     print(i)
#     i +=1
# i = 100
# while i >= 1 :
#     print(i)
#     i -= 1
# i = 1
# while i <= 10:
#     print(3*i)
#     i += 1
# i = 1 
# while i <= 10:
#         print(8*i)
#         i += 1
# n = int(input("enter number : "))
# i = 1

# while 1 <= 10:
#     print ( i)
#     i += 1
# i = 1
# while 1 <= 10:
#     print(3*i)
#     i += 1
# n = int(input("Enter number: "))
# i = 1

# while i <= 10:
#     print(n * i)
#     i += 1
# n = int(input("Enter number: "))
# i = 1

# while i <= 10:
#     print(n * i)
#     i += 1
# numbers = [8,6,3,4,5,2,7,9,1,10]
# print(numbers)
# print(type(numbers))
# indx = 0
# while indx <len(numbers):
#     print(indx)
# #     indx += 1
# indx = 0
# while indx <len(numbers):
#         print(numbers[indx])
#         indx += 1
# nums = (1, 4,  9,  16,  25 , 36, 49, 64, 81, 100)

# x = 36

# i = 0
# while i < len(nums):
#   if(nums[i] == x):
#     print(" found at index ", i)
#     i += 1
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1
# i = 0
# while i < len(nums):
#   print(nums[i])
#   i += 1
# x = 36

# i = 0
# while i < len(nums):
#   if(nums[i] == x):
#     print("FOUND AT INDEX",i)
#     i += 1
# x = 36
# for i in range(len(nums)):
#     if nums[i] == x:
#         print("FOUND AT INDEX", i)

# nums = (1, 4,  9,  16,  25 , 36, 49, 64, 81, 100)

# i = 0

# x = 36

# while i < len(nums):
#  if(nums[1] == x):
#   print("found at index",i)
#   i += 1
# nums = [10, 20, 30, 36, 50]

# x = 36   # ✅ define kiya

# for i in range(len(nums)):
#     if nums[i] == x:
#         print("FOUND AT INDEX", i)

nums = (1, 4,  9,  16,  25 , 36, 49, 64, 81, 100)

x = 36
 
i = 0

# while i < len(nums):
#     if(nums[i] == x):
#         print("fount at index",i)
#         break
#     else:
#             print("finding..")
#     i += 1
#     print("end of loop")
# i = 0
# while i <= 5:
#     if (i == 3) :
#         continue
#         print(i)

#         i += 1
# i = 0
# while i <= 5:
#     if i == 3:
#         i += 1   # 🔥 increment pehle karo
#         continue

#     print(i)
#     i += 1
# i = 0
# while i <= 10 :
#     if i%2 == 0:
#         i += 1   # 🔥 increment pehle karo
#         continue

#     print(i)
#     i += 1

# nums = [1 , 4 , 9 , 16 , 45 , 49 , 100]
# for el in nums:
#     print(el)
# nums = ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 2 , 9 , 10)
# x = 2
# index = 0
# for el in nums:
#     if(el == x):
#         print("number found at index",index)
#     index += 1
# seq = range(10)

# for i in seq:
#     print(i)
# for i in range(10):
#    print(i)
# for i in range(2,10):
#     print(i)
# for i in range(2,10,2):
#    print(i)
# for i in range(2 , 100 , 2 ):
#    print(i)
# for i in range(3 , 100 , 3):
#    print(i)

# for i in range(1 , 101):
#     print(i)
# for i in range(100 , 0 ,-1):
#     print(i)
# n = int(input("enter number : "))
# for i in range(1, 11):
#    print(n*i)

# n = int(input("enter number : "))
# for i in range(1,10):
#    print(n*i)
# n = 5
# sum = 0
# for i in range(1 , n+1):
#     sum += i
#     print(i)
n = 9
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print("factorial = ", factorial)
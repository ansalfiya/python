# text = "Python Programming"
# # Kya "Python Programming" ke end me "ing" aata hai?
# print(text.startswith("Py", 0))
# nam = "Ahmad is a good boy. but he is very mischiesf boy"
# name = "Ahmad is a good boy. but he is very mischief boy"

# pos = name.find("a")

# while pos != -1:
#     print(pos)
#     pos = name.find("a", pos + 1)
# print(nam.find("a", +  1))
# ham = "Haroon, Aamir, Rehana"
# print(ham.istitle())

# what is string 




# if you write any word double or single code then python easily convert in string
# first string 

# how to send next line

# name1 = "haroon is a good boy.\nhe is studying in college.\nbut right now.

# if you want to run this code then easily run. but you want to first sentance 
# first line and second sentance second line and third sentance third line
# you use \n  ka use kare ya phir aap use kar sakte  hai tirple single code ya 
# tirple doube code double me likhe ho to single ya single me likhe ho to double

# print(name1)

# print("""haroon is a good boy.
# he is studying in college.
#  but right now.""") 
 
#  ya phir aise kar ke aap sentance ko dusri line me kar sakte ho

# print(name1)

        #    highlight

# a = "who is the best 'person' in the world "
# print(a)

# b = "who is \"haroon\" and i want to highlight haroon"
# print(b)

# aise me koe word highlight hota hai but ye single me hog magar aap chahte hai 
# single ke bajaye double me aaye to "" code \ dena hoga ya single me aap ka code 
# hai aur chahte hai single me hi highlightdu to us ke liye bhi back sales \ dena hoga

# how to chechk index

# name = "haroon is good boy"
# for i in name:
#    print(i)
   
#    if you want to check evry index then you use for loop

# x = "what is python"
# print(len(x))

# estariqw se lenth malum kar sakte hai 

# y = "why are you learning english"
# print(y[-5:0])
# this is question marks is ko samajh na hai 

# How to oprate with string 

#  1 first. sstring are immutable 
# what is string 
# string are not modify in python 
# matlab string ko badlA NAHI JATA HAI 
 
# how many oprater in string 

# first 1
# upper()method 
# if you have alredy written code in python then you want you all code in capital then you use 
# uppermethod 
# name = "who is the best person in your life "
# print(name.upper())

# second method 
#  first ka opposite ya es me lower me aayega 

# name = "WHO IS THE BEST PERSON IN YOUR LIFE."
# print(name.lower())

# third method 
# rstrip() es me koe word ke baad aap ko achha nahi laga to phir aap hata sakte ho har kisi ko only
# backsales ko nahi hata sakte \ word ke pahle laga ho usko nahi hata sakte 

# a = "haroon "
# print(a.rstrip(""))

# fourth method 
# replace() method es me koe word ko aap hata ke dusra worad rakhna chahte ho to replace ka use kare

# haroon = "Ahmad is a good boy"
# print(haroon.replace("Ahmad","haroon"))

# 5th method 
# split() es sme ye hota hai ki jaha jah space hot ahai wah ye alag alag kar ta  hai coma and single 
# code lag at hai
# h = "haroon  ahmad nabi "
# print(h.split(" "))

# 6th method 
# capitalize method esme koe word ko first alfabed ko capital me convert karega aur bich me hoto usko 
# small me karega

# a = "who Is the Best person.\ni want to know"
# print(a.capitalize())

# 7th method 
# center() method es me ye hota hai ki aapko title bana ho aur aapne first me likha hai to usko 
# center me layega
# esko center me lane ke liye kuch number dena hoga jitna aapko center me chahye 
# j = "block boster movie"
# print(j.center(50))

# 8th method 
# count() method es me ye check kar sakte hai ki kaunsa word kitne baar aaya hai 
# ya phir aap ye chahte hai ki koe alfabed bhi check kar sakte hai 
# h = "i love is best , you want to take tea"
# print(h.count("i"))

# 9th method 
# endswith() method es me ye hota hai ki aap koe word ya koe chinha se End karte hai 
# to true aayega warna false aayega 
# u = "i want to go any beautiful place" 
# print(u.endswith("e")) 
# es me aisa bhi karsate hai 
# print(u.endswith("go",1,12)) 

# 10th method 
# startswithJ() es me kaunsa word se start hota hai ye pata karta hai 
# g = "python is the best language and easy to learn "
# print(g.startswith("python"))

# 11th find() method 
# find() method ye bata hai ki kaunsa ward kitne index par hai es me ek aur bhi haiki jitna hai 
# wah sab aayega but abahi wah mujhe nahi malum hai malum karna hai ? 
# name = "Ahmad is good boy "
# print(name.find("a"))

# 12th method 
# isalnum() method es me ye malum karte hai ki cpital A se capital Z tak ya phir small a se small z tak 
# and 0 se 9 tak  hai ki nahi nahi to phir true ya false dega
#  es me koe thodda mistake hai 

# w = "harron1"
# print("isalnum",w.isalnum())

# username = "Haroon!45@!"
# print(username.isalnum())
# 13th method 
# isalpha() method es me capital A se capital Z tak and small a se small z tak hota hai es me 
# 0 se 9 nahi hota hai 
# q = "who is haroon "
# print(q.isalpha())
#  esme bhi question mark hai ? 

# 14th method 
# islower() es me aapne code likha hai apag wah sirf small me likha hoga to dega true warna false 
# w = "i want to take sleep"
# print(w.islower())

# 15th method 
# isprintable()  esme har ek print hog abut \n back n doge to true nahi false aayega
# t = "hello word \n"
# print(t.isprintable())

# 16th method 
# isspace() method esme sirf space hoga to true warna false dega ya phir tab ho to chalega
# r = "    "
# print(r.isspace())

# 17th method 
# istitle() method es me yedekh ta hai hiki har ek word ka first latter capital hai ki nahi hai to 
# True warna false 
# a = "Haroon Is Good Boy"
# print(a.istitle())

# 18th method 
# swapcase() method ye convert kar ta hai lower ko upper me and upper ko lower me 
# e = "haroon Is gOOd boy"
# print(e.swapcase())

# 19th method 
# title() method es ka matlab ye hai ki ye har ek word ka first alfabed capital me convert kar ta hai 
# a = "haroon i love you "
# print(a.title())



# userRecord = " "

# print("isspace", userRecord.isspace())


studenRecord = "Nabi"
print("isTittile", studenRecord.istitle())


description = "A paragraph is a self-contained unit of discourse in writing that deals with a particular point or idea. It typically consists of a group of related sentences—or sometimes just a single sentence—and is distinguished by starting on a new line"

#index = [i for char in enumerate (description) if char.lower() == 'a' ]
indexes = [i for i, char in enumerate(description) if char.lower() == 'd']
print("Real Index", indexes)
#print("Discription", description.find("A")) 
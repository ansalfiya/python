# '''
# a = 2 
# b = 4
# sum = a+b
# print(sum)
# a = 10
# b = 2
# diff = (a-b)
# print(diff)
# print("haroon")
# a = 4
# b = 8.3
# sum = a + b
# print(sum)
# a = "5"
# b = 4.3
# sum = a + b
# print(sum)
# '''
# a = float("4")
# b = 8.3

# aum = a + b
# print(type(a))
# print(sum)
# string = 'that is boy"s and you'
# print(string)
# string = "this is book./n and i want to read this book"
# print(string)
# string2 = "this is book. \n and i want to read this book"
# print(string2)
# string3 = "this is book.\nI wand to read this book"
# print(string3)
# string1 = 4
# string2 = 5
# haroon = string1 + string2
# print(haroon)
# # print(type(haroon))
# haroon = { 1, 2, 2, 4, 4, "arya" ,"then"}
# print(haroon)
# print(type(haroon))
# print(len(haroon))
student =[
    {"id": 101, "name": "nabi", "class": "l2th", "roll_number": 1, "div": "A" },
    {"id": 102, "name": "haroon", "class": "10th", "roll_number": 2, "div": "B"},
    {"id": 103, "name": "Abrar", "class": "11th", "roll_number": 3, "div": "c"},
    {"id": 104, "name": "ansari", "class": "9th", "roll_number": 4, "div": "d"},
    {"id": 105, "name": "alwahab", "class": "13th", "roll_number": 5, "div": "r"},
    {"id": 106, "name": "alkahar", "class": "8th", "roll_number": 6, "div": "B"}

]
# print(student[1]["class"]["div"])
print(student[2]["name"], student[2]["class"], student [2]["div"])
print(student[3]["name"], student[3]["class"], student [3]["div"],student[3]["id"])
print(student[5]["name"], student[2]["class"], student [1]["div"],student[4]["id"])


ai_data = {
    "hello":"hey!  how can i help you?",
    "hi":"hello there!  ",
    "what is python":,"python is a powerful programing language used for apps,AI,data  science and more!  ",
    "who is elon musk": "is th founder of tesla, spacex and the richest person in the world! ",
    "who is bill gates":"the founder of microsoft,one of richest person in world  ",
    "what is ai":"AI means Artificial Intelligence - machines that can think and learn!  ",
    "bye":"Goodbye!  Have a great day! "
    "who are you"  "i am AI"

} 
print("AI Chatbot Activated! type 'exit' to stop.")

while True:
    user = input("you: ")

    if user.lower() == "exit":
        print("AI: Goodbye!")
        break

    elif "hi" in user.lower() or "hii" in user.lower():
        print("AI: Hello! How are you?")

    elif "how are you" in user.lower():
        print("AI: I am fine. Thanks for asking!")

    elif "your name" in user.lower():
        print("AI: I am your Python AI chatbot.")

    else:
        print("AI: Sorry, I don't understand.")
        new_answer  = input("Teach me the answer   ")
print("AI Chatbot Activated! type 'exit' to stop.")

while True:
    user = input("you: ").lower()

    if user == "exit":
        print("AI: Goodbye!")
        break

    elif "hi" in user or "hello" in user or "hii" in user:
        print("AI: Hello! Kaise ho?")

    elif "your name" in user:
        print("AI: Mera naam Python AI hai.")

    elif "ai" in user:
        print("AI: AI ek artificial intelligence system hota hai.")

    elif "how are you" in user:
        print("AI: Main theek hoon!")

    else:
        print("AI: Sorry, I don't understand.")
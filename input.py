#name = input("enter your age : ")
#print("you entered : ",name)
#v3alue = int(input("enter some value :"))
#print(type(value),value)
#value = float(input("enter some value :"))
#print(type(value),value)
# name = input("enter name : ")
# age = int(input("enter age : "))
# marks = float(input("enter marks : "))
ai_data = {
    "hello":"hey!  how can i help you?",
    "hi":"hello there!  ",
    "what is python":"python is a powerful programing language used for apps,AI,data  science and more!  ",
    "who is elon musk": "is th founder of tesla, spacex and the richest person in the world! ",
    "who is bill gates":"the founder of microsoft,one of richest person in world  ",
    "what is ai":"AI means Artificial Intelligence - machines that can think and learn!  ",
    "bye":"Goodbye!  Have a great day! "

} 
print(" AI Chatboat Activated! type'exit' to stop. \n")

while True:
    user_input = input("you: ").lower()
    "Taking user input"

if user_input =="exit":
        print("AI: Chat Ended!  ")
        'break'
if user_input in  ai_data:
    print("AI:", ai_data[user_input])
else:

    # print("AI: Sorry , I don't know this........
    #   '')
    print("AI: Sorry , I don't know this......")
new_answer  = input("Teach me the answer   ")
ai_data[user_input] = new_answer
print("AI: Goat it! I will remember this! \n")
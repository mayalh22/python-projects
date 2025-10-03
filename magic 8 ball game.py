import random
print("welcome to the magic 8 ball!")
responses = ["concentrate and ask again", "it is certain", "it is decidedly so", "most likely", "my reply is no", "very doubtful", "better not tell you now", "outlook good", "without a doubt", "my sources say no"]
while 0==0:
    input("ask a question")
    print("the magic 8 ball says...")
    listnum = random.randint(0, 9)
    print(responses[listnum])
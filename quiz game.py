print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)")
score=0

answer =input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("What does gpu stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("What does psu stands for? ")
if answer.lower() == "power supply":
    print("correct!")
    score +=1
else:
    print("Incorrect!")
print("you got " + str(score) +" questions correct!")
print("you got " + str((score/4)*100) +"%.")


import random
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()
if playing != "yes":
	print("Okay! Have a great day:)")
	quit()

NumberOfPoints=0 

questions_dict = {
	"What does CPU stand for? ": "central processing unit",
	"What does GPU stand for? ": "graphics processing unit",
	"What does RAM stand for? ": "random access memory",
	"What does PSU stand for? ": "power supply unit"
}
print("Okay! Let's play :)")

q, a = random.choice(list(d.items()))

while True:
	answear = input(q).lower()
	if answear == a:
		print("Correct!")
		NumberOfPoints+=1
	else:
		print("Incorrect!")
	playing = input("Would you like to answear another question?").lower()
	if playing != "yes":
		print("You got " + str(NumberOfPoints) + " questions correct!  \nThanks for playing :)")
		break()

"""	
answear = input("What does CPU stand for? ").lower()
if answear == "central processing unit":
	print("Correct!")
	NumberOfPoints+=1
else:
	print("Incorrect!")

answear = input("What does GPU stand for? ").lower()
if answear == "graphics processing unit":
	print("Correct!")
	NumberOfPoints+=1
else:
	print("Incorrect!")

answear = input("What does RAM stand for? ").lower()
if answear == "random access memory":
	print("Correct!")
	NumberOfPoints+=1
else:
	print("Incorrect!")

answear = input("What does PSU stand for? ").lower()
if answear == "power supply unit":
	print("Correct!")
	NumberOfPoints+=1
else:
	print("Incorrect!")

print("You got " + str(NumberOfPoints) + " questions correct!  \nThanks for playing :)")
"""
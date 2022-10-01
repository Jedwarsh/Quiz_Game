import random

print("Welcome to my computer quiz!")

playing = input("Do you want to play?\n").lower()

if playing != "yes":

	print("Okay! Have a great day:)")

	quit()

NumberOfPoints = 0 
NumberOfQuestions = 0

questions_dict = {
	"What does CPU stand for? ": "central processing unit",
	"What does GPU stand for? ": "graphics processing unit",
	"What does RAM stand for? ": "random access memory",
	"What does PSU stand for? ": "power supply unit"
}

print("Okay! Let's play :)")

while True:

	NumberOfQuestions +=1
	
	q, a = random.choice(list(questions_dict.items()))

	answear = input(q + "\n").lower()

	if answear == a:

		print("Correct!")

		NumberOfPoints+=1

	else:

		print("Incorrect!")

	playing = input("Would you like to answear another question?\n").lower()

	if playing != "yes":

		percent = (NumberOfPoints/NumberOfQuestions)*100

		print("You got " + str(NumberOfPoints) + " questions correct! (" + str(percent) + " %)" + "  \nThanks for playing :)")

		break
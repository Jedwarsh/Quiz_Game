print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing != "yes":
	print("Okay! Have a great day:)")
	quit()

NumberOfPoints=0 

print("Okay! Let's play :)")	

answear = input("What does CPU stand for? ")
if answear.lower == "central processing unit":
	print("Correct!")
	NumberOfPoints+=1
else:
	print("Incorrect!")

answear = input("What does GPU stand for? ")
if answear.lower == "graphics processing unit":
	print("Correct!")
	NumberOfPoints+=1
else:
	print("Incorrect!")

answear = input("What does RAM stand for? ")
if answear == "random access memory":
	print("Correct!")
	NumberOfPoints+=1
else:
	print("Incorrect!")

answear = input("What does PSU stand for? ")
if answear.lower == "power supply unit":
	print("Correct!")
	NumberOfPoints+=1
else:
	print("Incorrect!")

print("You got " + str(NumberOfPoints) + " questions correct!  \nThanks for playing :)")
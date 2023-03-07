runProgram = input("Do you wish to continue? (Y/N)").upper()

while runProgram == "Y" or runProgram == "Yes":
    
    count = 0
    lastName = input("Enter last name: ")
    score1 = int(input("Enter exam score #1: "))
    score2 = int(input("Enter exam score #2:"))
    avg = (score1 + score2) / 2

    count = count + 1
    print("Average Score: " + str(avg))
    print(count)

    
    break



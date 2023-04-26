'''
Dynamic List processing
Write the code for the following activities. Put all code into one file. You can comment sections out as you complete and test them so you don’t have to keep running the same code. 
1.	Prompt the user for a number which will represent the number of items in a list. Then use a for loop to add that many integers to the list. For example, if the use enters 3, the for loop should get 3 integers from the user and load them into the list. Then display the list.  

2.	Insert the score of 99 at position 1 within the list. Display the updated list.

3.	Replace the value of 99 with the value 100. Display the updated list.  

4.	Create a second list with the values 500, 600, 700, 800, 900. Display this list. Extend the first list with this second list. Display the first list. 

5.	Remove the value 800 from the first list. Display the first list. 

6.	Remove the third item from the first list. Display the first list. 

7.	Create a list of grades: grades =["A", "B", "C", "A", "A", "C"]

8.	Display a count of the number of A grades. 

9.	Display the index (position) of the first B grade. 

10.	Look for grade of F in the grades list. Display a message that F is not in the list. (Do not let the code generate an error). 

11.	Clear (but do not delete) the second list of integers. Display the list. 

12.	Delete the second list. Try to display it. (should get an error because the list no longer exists. 

13.	Create a list of players in this order (“Rizzo”, “Davis”, “Baez”, “Happ”, “Bryan”)

14.	Sort the list of players. Display the sorted list. 

15.	Make a copy of the list of players called players2. Display players2.

16.	Reverse the order of players2. Display players, then display players2. 

'''
# Function creates list based off user input.
def create(myList):
    number = int(input("How many items do you want for your list? "))
    for number in range(0, number, 1):
        value = int(input("Enter an integer: "))
        myList.append(value)
    return myList

# This function will display the list 
def display(myList):
    for item in myList:
        print(item)

myList = []
myList = create(myList) 
display(myList)
print(myList)

#2
myList.insert(0, 99)
print(myList)

#3
myList[0] = 100
print(myList)

#4
list2 = [500, 600, 700, 800, 900]
print(list2)
myList.extend(list2)
print(myList)

#5
myList.remove(800)
print(myList)

#6
del myList[2]
print(myList)

#7
grades = ["A", "D", "C", "C", "B", "B", "A"]

#8
print(grades.count("A"))

#9
print(grades.index("B"))

#10
look_for = "F"
# See if the item is in the list.
if look_for in grades:
    # If it's in the list, get and show the index.
    print(str(look_for) + " is at index " + str(grades.index(look_for)))
else:
    # If not in the list, don't even try for index number.
    print(str(look_for) + " isn't in the list.")

#11
list2.clear()
print(list2)

#12
#del list2
#print(list2)

#13
players = ["Rizzon", "Davis", "Baez", "Happ", "Bryan"]

#14
players.sort()
print(players)

#15
players.reverse()
print(players)
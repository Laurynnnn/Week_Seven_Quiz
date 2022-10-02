# 1. Your task is to create slightly different animals, which should have the same properties and methods, 
# but should implement the talk() method 
# in different ways. For example. should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and 
# a Cow "Muuu". They should all share the following (private) properties: name (string), age (number), food 
# (list of strings), and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food.
# Finally, all the animals must have the talk function, but that function must, as I said, be implemented in each
#  animal, as the animals have different sounds.
# When you have made the classes, create instances of the classes and put in a list - loop through the list - 
# and let all the animals talk! :)

class Animal:
    def __init__(self):
        self.__name = "name"
        self.__age = 0
        self.__food = "[food, water]"

    def set_name(self, namee):
        self.__name = namee

    def get_name(self):
        return self.__name
        
    def set_age(self, agee):
        self.__age = agee

    def get_age(self):
        return self.__age

    def set_food(self, foods):
        self.food = foods
        
    def add_food(self, ):
        pass

    def remove_food(self):
        pass

    def talk(self):
        print("I can talk")

    def details(self):
        print(f"I am a {self.__name} and I am {self.__age} months old")

class Cat(Animal):
    def __init__(self):
        super().__init__()

    def talk(self):
        print("Meow")

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def talk(self):
        print("Woof")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def talk(self):
        print("Blub")

class Cow(Animal):
    def __init__(self):
        super().__init__()

    def talk(self):
        print("Moo")

animals = [Cat(), Dog(), Cow(), Fish()]

animals[0].set_name("cat")
animals[1].set_name("dog")
animals[2].set_name("cow")
animals[3].set_name("fish")

animals[0].set_age(12)
animals[1].set_age(11)
animals[2].set_age(10)
animals[3].set_age(9)

for animal in animals:
    animal.details()
    animal.talk() 

# 2. The snail climbs up 7 feet each day and slips back 2 feet each night. How many days will it take the 
# snail to get out of a well with the given depth?. Using python, write a function to solve this problem. 
# Sample Input: 31 Sample Output: 6

def Days(depth):
    day = 0
    feet_covered = 0
    while feet_covered < depth:
        day = day + 1
        feet_covered = feet_covered + 7
        if feet_covered >= depth:
            print(day)
            break
        feet_covered = feet_covered - 2

depth = int(input("Enter depth of well: ")) 
Days(31)      


# 3.Write a function that takes a list of numbers and returns the largest number in the list.
distances = [200, 1000, 600, 500, 5]
def getMax(list):
    print(max(list))

getMax(distances)

# 4. Write a program that accepts a sentence and calculate the number of upper case letters and 
# lower case letters. Suppose the following input is supplied to the program: Hello world! 
# Then, the output should be: UPPER CASE 1 LOWER CASE 9

sentence = input("Enter the string you want to check: ")
lower_case = 0
upper_case = 0

for i in sentence:
    if i.isupper():
        upper_case += 1
    elif i.islower():
        lower_case += 1
    else:
        pass
print("Number of upper case: {}".format(upper_case))
print("Number of lower case: {}".format(lower_case))

# 5. Using Object Oriented Programming, write a program that implements a dice game. The game should 
# have two players, and each player should have a name and a score. The game should have a method 
# called play that takes two players as arguments and simulates the game. The game should be played 
# as follows:

# Each player rolls a die.
# The player with the highest roll wins the round.
# The winner gets one point added to their score.
# The game ends when one player has 5 points.
# The player with the most points at the end of the game wins.
# The program should print out the winner's name and score.
# If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. 
# If they roll a 6 a third time, they get an extra roll, but their turn ends.
import random

def roll():
    return random.choice([1, 2, 3, 4, 5, 6])
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score:


    def play(player1, player2):
        score = 0

class Game:
    score = 0
    round = 1
    
    print("Player one...")
    value1 = roll()
    print(value)
    if value1 = 6:
        while round <= 3:
            new_value1 = roll()
        print(f"Your value is: {new_value1}")
    else:
        print(value1)
    
    print("Player two...")
    value2 = roll()
    print(value2)
    if value2 = 6:
        while round <= 3:
            new_value2 = roll()
        print(f"Your value is: {new_value2}")
    else:
        print(value2)

    def get_score():
         



# 6. Write a Python program that lists out all the default as well as custom properties of the class.

# 7. Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, 
# pop, and traversal methods.
class Stack:
    def __init__(self):
        self.stack = [9,0]

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return ("Stack is empty. Stack Underflow :(")
        return self.stack.pop()

    def size(self):
        return len(self.stack)
    
    def show(self):
        return self.stack

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.show())
print(s.pop())
print(s.show())
print(s.size())

class Node:
    def __init__(self, x):

        stack = []

        self.data = x
        self.right = None
        self.left = None

    def POI(root):
        while(True):
            while(root != None):
                stack.append(root)
                stack.append(root)
                root = root.left


            if(len(stack) == 0):
                return

            root = stack.pop()

            if(len(stack) > 0 and stack[-1] == root):
                root = root.right
            else:
                print(root.data, end = " ")
                root = NotImplemented

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left = Node(7)

    print("Post order Traversal of binary tree is: ")
    POI(root)

# 8. Using list comprehension, write a program that takes a list of numbers and returns a list of the squares 
# of the numbers.

my_list = [x*x for x in range(20) if x != 0]
print(my_list)



# 9. Using only functions and lists, Implement a queue data structure. The queue should have the following 
# methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO).
class Queue:
    def __init__(self):
        self.queue = [20, 23]

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def show(self):
        return self.queue

q = Queue()
q.isEmpty()
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print("Before dequeue, size: ")
print(q.size())
q.dequeue()
q.dequeue()
print("After dequeue, size: ")
print(q.size())
print(q.show())

# 10. Using a while loop, implement merge sort algorithm.
def mergesort(x):
    if len(x) < 2:
        return x
     
    result = []                  
    mid = int(len(x) / 2)  

    #first half of array 
    y = mergesort(x[:mid]) 

    #second half of array      
    z = mergesort(x[mid:])       
    i = 0
    j = 0
    while i < len(y) and j < len(z):  
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]             
    result += z[j:]             
    return result
    print(result)

if __name__ == '__main__':
    nums = [54, 56, 66, 77, 34, 23, 1]
    mergesort(nums)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print()
zero = int(input("How many letters would you like in your password? ")) 
print()
one = int(input(f"How many symbols would you like? "))
print()
two = int(input(f"How many numbers would you like?"))
print()

password = str()


while zero != 0 or one !=0 or two !=0:
  x = random.randint(0,2)
  if x==0 and zero >0:
    password+= random.choice(letters)
    zero=zero-1

  elif x==1 and one > 0:
    password+= random.choice(symbols)
    one = one -1

  elif x==2 and two > 0:
    password+= random.choice(numbers)
    two = two -1

print(password)
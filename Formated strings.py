##[Formated strings]##

name = "Johnny"
age = 55

print("Hi " + name + '. you are ' + str(age) + ' years old')

print(f"Hi {name}. You are {age} years old") #recomended use of formated strings (clean and easy)

print("Hi {}. You are {} years old".format('Jhonny','55'))

print("Hi {}. You are {} years old".format(name,age))

print("Hi {1}. You are {0} years old".format(name,age))

print("Hi {new_name}. You are {age} years old".format(new_name="Sally",age=100))
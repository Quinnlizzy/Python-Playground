def greeting():
    print("Hello Friend!")
    
greeting()

#Hello Friend!

def greeting(name):
    print("Hello " + name + "!")
    
greeting("Brian")

#Hello Brian!


def greeting(name,age):
    print("Hello " + name + ", you are " + age + "!")
    
greeting("Brian","32")

#Hello Brian, you are 32!



def greeting(name,age):
    print("Hello " + name + ", you are " + age + "!")
    print(f"Hello {name}, you are {age}!")
    
greeting("Brian","32")

#›Hello Brian, you are 32!
#›Hello Brian, you are 32!




def greeting(name,age="28"):
    print("Hello " + name + ", you are " + age + "!")
    print(f"Hello {name}, you are {age}!")
    
greeting("Brian","32")
greeting("Judith")

# ›Hello Brian, you are 32!
# ›Hello Brian, you are 32!
# ›Hello Judith, you are 28!
# ›Hello Judith, you are 28!
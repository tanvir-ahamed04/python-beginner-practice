# making house using funtion in python
def brick_dsi():
    print_hash(5)
    
    # head
    
def print_hash(width):
    for i in range(width):
        for have in range(width - i -1):
            print(" ", end="")
        for empty in range(i + 1): 
            print("#", end=" ")
        for dolar_sign in range(width + 12):
            print("$", end=" ")
        print()
        
def body_inside():
    print_body(5)
    
    # body-setup- 
def print_body(height):
    for a in range(height):
        for b in range(height):
            print(" # ", end="")
        if a == 3:
            break
        for dolar_body_sign in range(5):
            print(" $" , end="")
        
        # fro door space
        for door_space in range(3):
            print(" ", end="")
        for dolar_body_sign_again in range(7):
            print(" $" , end="")
        print("")


# tail

def tail_inside():
    print_tail(15)
    
def print_tail(long):
    for tail_long in range(long):
        print("# ", end="")
        
    print(" ")
        
# last tail 
def last_tail():
    for last_tail_long in range(45):
        print("#", end="")
    print("")
            
brick_dsi()
body_inside()
tail_inside()
last_tail()
last_tail()
last_tail()


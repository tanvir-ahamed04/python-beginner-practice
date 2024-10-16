def make_squares(n):
    for i in range(1, 5):
        for j in range(i - 1):
            print("*", end="")
        print("*")
        for left_side in range(n - i):
            print("%", end="")
        
        




make_squares(4)

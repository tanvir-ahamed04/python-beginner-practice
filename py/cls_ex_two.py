my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if all(x % 2 == 0 for x in my_list):
    print("even number", my_list)
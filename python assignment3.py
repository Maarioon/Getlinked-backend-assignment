# task 3 of the assignment

def numbers(list):
     if list[0] == list[-1]:
          return True
     else:
          return False
     
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print(numbers(numbers_x))
print(numbers(numbers_y))

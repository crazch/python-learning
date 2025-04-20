# TODO: Build CLI calculator  
# Features: Add, subtract, multiply, divide  
def add(a, b):
  return a + b
  
def subtract(a, b):
  return a - b
  
def multiply(a, b):
  return a * b
  
def divide(a, b):
  if b != 0:
    return round(a / b, 2)
  else:
    return "Error Division by  zero!"

def calculator():
  while True:
    print("Select Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    user_input = input("Select(1/2/3/4/5): ")
    if user_input == '5':
      print("Exiting...")
      break
    
    if user_input not in ['1', '2', '3', '4']:
      print("Invalid Option!")
      continue
    
    try:
      num1 = float(input("Enter First Number: "))
      num2 = float(input("Enter Second Number: "))
    except ValueError:
      print("Invalid Input!")
      continue
    
    if user_input == '1':
      print(f"{num1} + {num2} = {add(num1, num2)}")
    elif user_input == '2':
      print(f"{num1} - {num2}  = {subtract(num1, num2)}")
    elif user_input == '3':
      print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif user_input == '4':
      print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
      print("Invalid")

if __name__ == "__main__":
  calculator()
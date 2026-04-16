def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        print("Division by zero error")
    else:
        return a / b
def show_menu():
    print("1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Exit")
while True:
    show_menu()
    choice = input("Select: ")
    if choice == '5':
        break
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    if choice == '1':
        print(add(a, b))
    elif choice == '2':
        print(subtract(a, b))
    elif choice == '3':
        print(multiply(a, b))
    elif choice == '4':
        print(divide(a, b))

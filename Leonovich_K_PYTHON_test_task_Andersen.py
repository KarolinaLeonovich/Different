# 1. Составить алгоритм: если введенное число больше 7, то вывести “Привет”

def print_hello(compared_value=7.0):
    user_input = input("Введите число\n")
    user_input = user_input.replace(",", ".")
    try:
        condition_1 = user_input.replace(".", "").isdigit()
        condition_2 = float(user_input) > compared_value
        if all((condition_1, condition_2)):
            print("Привет")
    except ValueError:
        pass

# 2. Составить алгоритм: если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”, если  нет, то  вывести
# "Нет такого имени"

def hello_name():
    permitted_names = ["Вячеслав"]
    user_input = input("Введите имя\n")
    if user_input in permitted_names:
        print("Привет, " + user_input)
    else:
        print("Нет такого имени")

# 3. Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3

def mult_check(arr, divider=3):
    for num in arr:
        if num % divider == 0:
            print(num, end =" ")

# 4. Дана скобочная последовательность: [((())()(())]]
# - Можно ли считать эту последовательность правильной?
# - Если ответ на предыдущий вопрос “нет” - то что необходимо в ней изменить, чтоб она стала правильной?

#Ответ: Нет - надо так: [[((()))()(())]]
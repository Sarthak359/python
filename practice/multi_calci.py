def sum_all():
    rnumber: int = int(input("enter the number of inputs: "))
    s_sum = 0
    for numb in range(rnumber):
        ssnum = float(input("Enter a number: "))
        s_sum = s_sum + ssnum
    print(s_sum)


def sum_of_even():
    rnumber: int = int(input("enter the number: "))
    s_sum: int = 0
    for numb in range(rnumber):
        if numb % 2 == 0:
           s_sum += numb
    print(s_sum)


def vowel_count():
    string = input("Enter the string: ")
    vowel = 0
    for char in string:
        if char in "aeiou":
            vowel += 1
    print(vowel)


def area_circle():
    radius = float(input("Enter the radius of circle: "))
    pi = 3.14
    area = pi * radius * radius
    circumference = 2 * pi * radius
    print(area)
    print(circumference)


def filter_string_by_length():
    strings = input("Enter strings with spaces: ").split()

    filtered_string = []
    for string in strings:
        if len(string) > 5:
            filtered_string.append(string)
    print(filtered_string)


while True:
    x = float(input('''
    Type Number to perform calculation:
    1 : Addition
    2 : Subtraction
    3 : Multipy
    4 : Divide
    5 : sum of multiple numbers
    6 : sum of even numbers
    7 : Number of vowels in string
    8 : Area and circumference of circle
    9 : Filter string by length 5 and more
    10 : Exit
    '''))
    if 1 <= x <= 4:
        a = float(input("Enter 1st number: "))
        b = float(input("Enter 2nd number: "))
    if x == 1:
        r = a + b
        print("Answer is: ", r)
    if x == 2:
        r = a - b
        print("Answer is: ", r)
    if x == 3:
        r = a * b
        print("Answer is: ", r)
    if x == 4:
        r = a / b
        print("Answer is: ", r)
    if x == 5:
        sum_all()
    if x == 6:
        sum_of_even()
    if x == 7:
        vowel_count()
    if x == 8:
        area_circle()
    if x == 9:
        filter_string_by_length()
    if x == 10:
        break


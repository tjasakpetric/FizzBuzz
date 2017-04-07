#Naloga FizzBuzz

print "*FizzBuzz game*"

choice = raw_input("Enter a number between 1 and 100: ")

try:
    for number in range(int(choice)+1):
        if number % 3 == 0 and number % 5 == 0:
            print "FizzBuzz!"
        elif number % 3 == 0:
            print "Fizz"
        elif number % 5 == 0:
            print "Buzz"
        elif number % 3 != 0 and number % 5 != 0:
            print number

except ValueError:
    print "Numbers only!"

# code asks user for number and divides 10 by it
# enter '0' to trigger exception
try:
    answer = 10 / int(input("Enter Number: "))
except ZeroDivisionError as e:
    print(e)
except:
    print("Caught any exception")
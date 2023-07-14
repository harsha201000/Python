import random
import string

def random_password(length_input):
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    nums = string.digits
    symbols = string.punctuation

    #print(lowers)
    #print(uppers)
    #print(nums)
    #print(symbols)

    use_all_characters = lowers + uppers + nums + symbols
    #print(use_all_characters)

    temp = random.sample(use_all_characters, length_input)
    #print(temp)


    password = "".join(temp)
    return password

length = int(input("Welcome to Password Generator. Please enter a length for the password> "))
return_password = random_password(length)
print(return_password)



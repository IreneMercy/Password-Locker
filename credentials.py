import string, random
class Generator:
    def passwordGenarator(length):
        print("Your generated  password is:")
        password = ''
        for i in range(length):
            n = random.randint(0,20)
            password += string.printable[n]
        return password
    print (passwordGenarator(5))

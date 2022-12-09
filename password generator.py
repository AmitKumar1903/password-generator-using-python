import random


def password_generator():
    length = int(input("Enter the length of the password:  "))
    if length >= 12:
        def generator():
            a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 +-:|~!@#$%^&*?\/"
            special = " +-:|~!@#$%^&*?\/"
            special_count = 0
            password = ""
            for i in range(length):
                char = random.choice(a)
                password += char
            for j in password:
                if j in special:
                    special_count += 1
            if special_count >= 1:
                print("The Password is:", password)
            else:
                generator()
        generator()
    else:
        print("Password length must be at least 12 characters long")
        password_generator()


password_generator()



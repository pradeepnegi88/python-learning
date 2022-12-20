def addition():
    n1 = int(input("Enter First Number : "))
    n2 = int(input("Enter Second Number : "))
    print(n1 + n2)
    print("Thanks for adding" + n1)


# try:
#     addition()
# except:
#     print("Something went wrong")
# # Execute if there is an error
#
# else:
#     print("You did great")
# # code execute when no error
#
# finally:
#     print("That's all")
# # this code execute always

try:
    addition()
except TypeError:
    print("TypeError")


except ValueError:

    print("ValueError")
# Execute if there is an error

else:
    print("You did great")
# code execute when no error

finally:
    print("That's all")
# this code execute always


def ask_number():
    while True:
        try:
            number = int(input("Enter a number"))
        except:
            print("That is not a number")
        else:
            print(f'You have enter number {number}')
            break
    print("Thank you")

ask_number()
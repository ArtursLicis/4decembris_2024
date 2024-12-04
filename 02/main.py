""" Method 1 """

num = int(input("Give me a number to check: "))          # Ļauj ievadīt ciparu ko pārbaudīt
check = int(input("Give me a number to divide by: "))    # Ļauj ievadīt ciparu ar ko dalīt

if num % 4 == 0:                                         # Ja cipars ko gribi pārbaudīt  
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:                                                    #
    print(num, "doesn't divide evenly by", check)

""" Method 2 """
num = int(input("Enter a number: "))                     # Prasa, lai ievada ciparu
mod = num % 2
if mod > 0:                                  
    print("You picked an odd number.")                   # Izprintē tekstu kas saka, ka tu izvēlējies nepāra ciparu
else:                                                    # Ja nē
    print("You picked an even number.")                  # Izprintē tekstu kas saka, ka tu izvēlējies pāra ciparu

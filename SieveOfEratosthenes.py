# Krzysztof Kuziel www.krzykustudio.pl
# Sieve of Eratosthenes 
# Find prime numbers up to any given limit
#helpers

def sieve(upper_limit):
    lower_range = 2

    #Generate all numbers
    numbers = [int(x) for x in range(lower_range, upper_limit + 1)]
    while True:
        #filter the list 
        numbers = [x for x in numbers if funkcja(x,numbers[0])]
        
        #if list is empty brek
        if(numbers==[]):
            break
        #else print prime number
        print(numbers[0])
          
def funkcja(x, number):
    """
    Funkcja return False if x is muliplication of number
    """
    if(x % number !=0):
        return True
    return False

#main 
try:
    upper_limit = int(input("Please enter upper limit: "))
    sieve(upper_limit)
except Exception as e:
    print(e)

try:
	int(input("Press Enter key to continue..."))
except:
	pass	
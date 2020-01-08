import random
import math
def funcionEjemplo(number):
    randNum = random.randrange(1,number+1)
    factNum = math.factorial(randNum)
    print("Numero al azar es {} y su factorial es {}".format(randNum,factNum))
	
def funcionEjemplo2():
    number = 5
    randNum = random.randrange(1, number + 1)
    if randNum == 1:
        print(randNum)
        print("El numero al azar entre uno y cinco es: uno")
    elif randNum == 2:
        print(randNum)
        print("El numero al azar entre uno y cinco es: dos")
    elif randNum == 3:
        print(randNum)
        print("El numero al azar entre uno y cinco es: tres")
    elif randNum == 4:
        print(randNum)
        print("El numero al azar entre uno y cinco es: cuatro")
    elif randNum == 5:
        print(randNum)
        print("El numero al azar entre uno y cinco es: cinco")
    else:
        print(randNum)
        print("numero no valido")
	
	
#print(funcionEjemplo(20))

anio=int(input("Digite un año: "))
if anio%4==0:
   if anio%100 !=0 or anio%400 ==0:
        print("El año es bisiesto")
   else:
        print ("El año no es bisiesto")
else:
   print("El año no es bisiesto")

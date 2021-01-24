#Jose Pablo Ponce 19092
#28-02-19
# Programa que calcula total y descuento de producto
precio = 0
subtotal = 0
descuento = 0
while precio != "fin":
    #Crear condiciones
    if precio !="fin":

        print ('tienda por departamentos')
        print ('1. electronicos')
        print ('2. plomeria')
        print ('3. ferreteria')
        print ('4. iluminacion')
        print ('5. Mostrar subtotal y total')
        
        #Ingresar opcion y precio
        subtotal += precio
        
        opcion = input ('ingrese una opcion')
        precio= input('ingrese precio')
        precio = int(precio)

        
        #convertir precio a entero

        #Asignar valor a subtotal

        #Crear condiciones
        if opcion == '1':
            precio1 = (precio * 0.5)

        
        elif opcion =='2':
            precio1 = (precio * 0.7)

            
        elif opcion =='3':
            precio1 = (precio * 0.10)

        elif opcion =='4':
            precio1 = (precio * 0.15)

            
        elif opcion =='5':
            descuento += precio1
            total = subtotal - precio1

            print ('subtotal:', subtotal)
            print ('total:', total)
            
            
            

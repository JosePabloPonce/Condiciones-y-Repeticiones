#Jose Pablo Ponce, 19092
#27-02-19
#ejercicio1
#programa que al ingresar el porcentaje me muestre la nota traducida a letras o escala 4.0

#mostrar el rango de notas
notas = 0
while notas != "fin":


    notas = input ('ingrese una nota o salga del programa escrivbiendo "fin"')
    if notas !="fin":
        notas = int (notas)
        #mostrar los rangos dependiendo del dato que se ingrese
        if 97 <= notas <=100:
            print ("Letra : A+ = Escala 4.0 :4.0")
        elif 93 <= notas <=96:
            print ("Letra: A = Escala 4.0: 4.0")
        elif 90 <= notas <=92:
            print ("Letra: A- = Escala 4.0: 3.7")
        elif 87 <= notas <=89:
            print ("Letra: B- = Escala 4.0: 3.3")
        elif 83 <= notas <=86:
            print ("Letra: B = Escala 4.0: 3.0")
        elif 80 <= notas <=82:
            print ("Letra: B- = Escala 4.0: 2.7")
        elif 77 <= notas <=79:
            print ("Letra: c+ = Escala 4.0: 2.3")
        elif 73 <= notas <=76:
            print ("Letra: C = Escala 4.0: 2.0")
        elif 70 <= notas <=72:
            print ("Letra: C- = Escala 4.0: 1.7")
        elif 67 <= notas <=69:
            print ("Letra: D+ = Escala 4.0: 1.3")
        elif 64 <= notas <=66:
            print ("Letra: D = Escala 4.0: 1.0")
        elif 61 <= notas <=63:
            print ("Letra: D- = Escala 4.0: 0.7")
        elif 61 > notas:
            print ("Letra: F = Escala 4.0: 0.0")
        #terminar programa
        else:
         
            print ("fin")
    
    
    
    
  
        
        
        
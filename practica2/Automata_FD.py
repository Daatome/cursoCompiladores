diccionario = {"0","1"}
def estado0( cadena, cont):
    #validacion si introdocuce caracteres no permitidos
    if cont== len(cadena):
        return False
    if cadena=="" or diccionario.__contains__(cadena[cont])==False :
        return "na"
    
    if cadena[cont]=="1":
        cont+=1
        return estado0(cadena,cont)
    elif cadena[cont]=="0":
        cont+=1
        return estado1(cadena,cont)
    

def estado1(cadena,cont):
    if cont>=len(cadena):
        return False
    if cadena=="" or diccionario.__contains__(cadena[cont])==False :
        return "na"

    
    elif cadena[cont]=="0":
        cont+=1
        return estado2(cadena,cont)

    elif cadena[cont]=="1":
        cont+=1
        return estado0(cadena,cont)
    

def estado2(cadena,cont):
    if cont>=len(cadena):
        return True
   
    if cadena=="" or diccionario.__contains__(cadena[cont])==False :
        return "na"

    
    elif cadena[cont]=="0":
        cont+=1
        return estado2(cadena,cont)

    elif cadena[cont]=="1":
        cont+=1
        return estado0(cadena,cont)
    


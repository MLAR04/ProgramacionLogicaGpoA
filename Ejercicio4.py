# Predicado 1

# Funcion de Multiplo de 6
def multiplo_6 (n):
    if n % 2 == 0 and n % 3 == 0: 
        return True
    else:
        return False 

# Funcion de puede votar    
def puede_votar(edad, credencial, lista_nominal):
    return edad > 18 and credencial and lista_nominal

# Funcion de puede conectarse a internet
def conectarse_internet(wifi, ethernet, modem):
    return (wifi or ethernet) and modem 


# ---- Probar multiplo_6 ----
print(multiplo_6(12))   
print(multiplo_6(18))  
print(multiplo_6(7))    
print(multiplo_6(20))   

# ---- Probar puede_votar ----
print(puede_votar(20, True, True))   
print(puede_votar(17, True, True))   
print(puede_votar(25, False, True))  
print(puede_votar(15, True, False))  

# ---- Probar conectarse_internet ----
print(conectarse_internet(True, False, True))  
print(conectarse_internet(False, True, True))  
print(conectarse_internet(True, False, False))  
print(conectarse_internet(False, False, True))  



    




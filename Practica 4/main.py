"""
Un número es múltiplo de 6 si es divisible entre 2 y entre 3.
Regla general:
M=R1 AND R2
Reglas:
El número es divisible entre 2
El número es divisible entre 3"""
print("=== Caso 1: Número múltiplo de 6 ===")
n = int(input("Ingresa un número: "))
R1 = (n % 2 == 0)   # divisible entre 2
R2 = (n % 3 == 0)   # divisible entre 3
M = R1 and R2
print(f"¿Es múltiplo de 6?: {'Sí' if M else 'No'}\n")


"""
Una persona puede votar si tiene más de 18 años y tiene credencial de elector y está en la lista nominal.
Regla general:
M= R1 AND R2 AND R3
Reglas:
Tiene más de 18 años.
 Tiene credencial de elector.
Está en la lista nominal."""
print("=== Caso 2: Derecho a votar ===")
R1 = input("¿Tiene más de 18 años? (Si/No): ").lower() == "si"
R2 = input("¿Tiene credencial de elector? (Si/No): ").lower() == "si"
R3 = input("¿Está en la lista nominal? (Si/No): ").lower() == "si"
M = R1 and R2 and R3
print(f"¿Puede votar?: {'Sí' if M else 'No'}\n")


"""
Una computadora puede conectarse a internet si tiene wifi activado o cable de ethernet conectado y además el modem funciona.
Regla general:
M= (R1 OR R2) AND R3
Reglas:
Wifi activado.
Cable ethernet conectado.
El módem funciona."""
print("=== Caso 3: Conexión a Internet ===")
R1 = input("¿Wifi activado? (Si/No): ").lower() == "si"
R2 = input("¿Cable ethernet conectado? (Si/No): ").lower() == "si"
R3 = input("¿El módem funciona? (Si/No): ").lower() == "si"
M = (R1 or R2) and R3
print(f"¿Se puede conectar a Internet?: {'Sí' if M else 'No'}")

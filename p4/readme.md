# P4 - Gonzalez Navarro

## Instrucciones

Resolver los siguientes problemas de descomposición de reglas lógicas

Ejercicios:

"Un número es múltiplo de 6 si es divisible entre 2 y 3"

Descomposición de reglas:

	* El número es divisible entre 2

	* El número es es divisible entre 3

Es múltiplo de 6 	<---> 		Regla 1 ^ Regla 2
		    (Si y solo si)

| R1 | R2 | S | 
| --- | --- | --- |
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |


"Una persona puede votar si tiene más de 18 anios, tiene credencial de elector y está en la lista nominal"

Descomposición de reglas:

	* Tiene más de 18 anios
	
	* Tiene credencial de elector

	* Está en la lista nominal

Una persona puede votar 	<---> 		Regla 1 ^ Regla 2 ^ Regla 3
		    	    (Si y solo si)

| R1 | R2 | R3 | S | 
| --- | --- | --- | --- |
| V | V | V | V |
| V | V | F | F |
| V | F | V | F |
| V | F | F | F |
| F | V | V | F |
| F | V | F | F |
| F | F | V | F |
| F | F | F | F |

"Una computadora puede conectarse a internet si tiene wifi conectado o cable Ethernet conectado y además el módem funciona"

Descomposición de reglas:

	* Tiene Wi-fi conectado
	
	* Tiene Ethernet conectado

	* El módem funciona

Puede conectarse a internet 	<---> 		(Regla 1 ^ Regla 2) v Regla 3
		    	    (Si y solo si)

| R1 | R2 | R3 | S | 
| --- | --- | --- | --- |
| V | V | V | V |
| V | V | F | F |
| V | F | V | V |
| V | F | F | F |
| F | V | V | V |
| F | V | F | F |
| F | F | V | F |
| F | F | F | F |
                   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    DESCOMPOSICIÓN DE REGLAS LÓGICAS

                    Emanuel Alejandro Tavares Medina
                   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Table of Contents
─────────────────

1. Predicados:
.. 1. Un número es múltiplo de 6 si es divisible entre 2 y entre 3
..... 1. Regla general
..... 2. Reglas
..... 3. Tabla de verdad
.. 2. Una persona puede votar si tiene más de 18 años, tiene credencial para votar y está en la lista nominal
..... 1. Regla general
..... 2. Reglas
..... 3. Tabla de verdad
.. 3. Una computadora puede conectarse a internet si tiene wifi activado o cable ethernet conectado y además el módem funciona
..... 1. Regla general
..... 2. Reglas
..... 3. Tabla de verdad


1 Predicados:
═════════════
Resolver los siguientes predicados de la siguiente manera:

  • Reglas
  • Regla general
  • Tabla de verdad
  • Código de python


1.1 Un número es múltiplo de 6 si es divisible entre 2 y entre 3
────────────────────────────────────────────────────────────────

1.1.1 Regla general
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  Un número es múltiplo de 6 si y solo si R1 ∧ R2


1.1.2 Reglas
╌╌╌╌╌╌╌╌╌╌╌╌

  1. Divisible entre 2
  2. Divisible entre 3


1.1.3 Tabla de verdad
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ━━━━━━━━━━━
   R1  R2  S 
  ───────────
   V   V   V 
   V   F   F 
   F   V   F 
   F   F   F 
  ━━━━━━━━━━━


1.2 Una persona puede votar si tiene más de 18 años, tiene credencial para votar y está en la lista nominal
───────────────────────────────────────────────────────────────────────────────────────────────────────────

1.2.1 Regla general
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  Un persona puede votar si y sólo si R1 ∧ R2 ∧ R3


1.2.2 Reglas
╌╌╌╌╌╌╌╌╌╌╌╌

  1. Tiene más de 18 años
  2. Tiene credencial para votar
  3. Está en la lista nominal


1.2.3 Tabla de verdad
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ━━━━━━━━━━━━━━━
   R1  R2  R3  S 
  ───────────────
   V   V   V   V 
   V   V   F   F 
   V   F   V   F 
   V   F   F   F 
   F   V   V   F 
   F   V   F   F 
   F   F   V   F 
   F   F   F   F 
  ━━━━━━━━━━━━━━━


1.3 Una computadora puede conectarse a internet si tiene wifi activado o cable ethernet conectado y además el módem funciona
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

1.3.1 Regla general
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  Una computadora puede conectarse a internet si y sólo si R1 ∨ R2 ∧ R3


1.3.2 Reglas
╌╌╌╌╌╌╌╌╌╌╌╌

  1. Tiene wifi activado
  2. Tiene cable ethernet conectado
  3. Módem funciona


1.3.3 Tabla de verdad
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ━━━━━━━━━━━━━━━
   R1  R2  R3  S 
  ───────────────
   V   V   V   V 
   V   V   F   F 
   V   F   V   V 
   V   F   F   F 
   F   V   V   V 
   F   V   F   F 
   F   F   V   F 
   F   F   F   F 
  ━━━━━━━━━━━━━━━

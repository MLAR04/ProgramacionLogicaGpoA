# Diccionario base
profesores = { 
    "pedro": {
        "etica": ["Rogelio", "Alexis", "Manuel"]
    }, 
    "Angelica": {
        "contabilidad": ["Rogelio", "David", "Carlos", "Maria"]
    }
}
def main():
    
    # Consulta 1 ¿Esta David en la clase de Etica?
    if "David" in profesores["pedro"]["etica"]:
        print("¿Está David en clase de Ética? True")
    else:
        print("¿Está David en clase de Ética? False")

    # Consulta 2 ¿tiene la clase de contabilidad 4 alumnos?
    if len(profesores["Angelica"]["contabilidad"]) == 4:
        print("¿Tiene la clase de Contabilidad 4 alumnos? True")
    else:
        print("¿Tiene la clase de Contabilidad 4 alumnos? False")
    

if __name__ == "__main__":
    main()
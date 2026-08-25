def numero_par(numero):
    return numero%2==0

numero=int(input("Ingrese su numero: "))
print("El numero", numero, "es",numero_par(numero),"que es par")
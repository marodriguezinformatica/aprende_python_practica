"""De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que 
lea dichos datos del teclado y realice lo siguiente:
Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %.
Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %. 
Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios."""

sueldo = int(input("Introduce el sueldo del empleado\n"))
ant = int(input("Introduce los años de antiguedad\n"))

if sueldo < 500 and ant >= 10:
    sueldo += 0.2*sueldo
elif sueldo < 500 and ant <= 10:
    sueldo += 0.05*sueldo

print(f"El sueldo final del empleado es: {sueldo}")

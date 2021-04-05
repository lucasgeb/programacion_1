
#! ejercicio 5
#! Resuelva el ejercicio de 3 de la guía uno aplicando el filtro para los CV.

#! El área de RRHH de una empresa desea filtrar los CV de los postulantes para un puesto
#! vacante, el requisito mínimo es la edad, pero en los datos solo tienen la fecha de
#! nacimiento.

ano_actual = int(input("ingrese año actual "))
ano_nacimiento = int(input('ingrese año de nacimiento del postulante '))

ano_postulante = ano_actual - ano_nacimiento

if(ano_postulante >= 18):
    print('cumple con los requisitos de edad')
else:
    print('no comple con los requisitos de edad')
print('fin del algoritmo')
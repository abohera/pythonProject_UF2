import funcions

def main():
    alumnos = int(input("¿Cuantos alumnos vas a introducir?: "))
    student_id = list()
    first_name = list()
    last_name = list()
    subject = list()
    grade = list()
    for i in range(alumnos):
        print("\nNúmero de registo %u: " % (i+1))
        id = int(input("Introduce el id del alumno: "))
        student_id.append(id)
        while student_id[i] <= 0:
            student_id[i] = int(input("Introduce un número entero: "))
        nombre = input("Introduce el nombre del alumno: ")
        first_name.append(nombre)
        apellido = input("Introduce el apellido del alumno: ")
        last_name.append(apellido)
        asignatura = input("Introduce las siglas de la asignatura: ")
        subject.append(asignatura)
        nota = int(input("Introduce la nota de la asignatura: "))
        grade.append(nota)
        while grade[i] <= 0:
            grade[i] = int(input("Introduce un número entero: "))
    print("\n")
    print("TABLA ALUMNOS")
    for i in range(alumnos):
        print(student_id[i], end=" | ")
        print(first_name[i], end=" | ")
        print(last_name[i], end=" | ")
        print(subject[i], end=" | ")
        print(grade[i])

if __name__ == "__main__":
    main()
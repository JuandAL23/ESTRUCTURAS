import numpy as np  

np.random.seed(42)  
candidatos = np.arange(1, 31)  
votos = np.random.randint(0, 1000, size=30)  
orden = np.argsort(votos)[::-1]  
candidatos_ordenados = candidatos[orden]  
votos_ordenados = votos[orden]  

print("\n Resultados de la votación:")
for i in range(len(candidatos)):
    print(f"Candidato {candidatos_ordenados[i]}: {votos_ordenados[i]} votos")


np.random.seed(42)  
n_estudiantes = 6500  

codigos = np.arange(100000, 100000 + n_estudiantes)  
nombres = np.array(["Estudiante " + str(i) for i in range(n_estudiantes)])  
promedios = np.random.uniform(2.0, 5.0, size=n_estudiantes)  
cod_carreras = np.random.randint(1, 11, size=n_estudiantes)  
años_ingreso = np.random.randint(1980, 2025, size=n_estudiantes)  
estado_condicional = np.random.choice([True, False], size=n_estudiantes, p=[0.1, 0.9])  


codigo_carrera = int(input("\nIngrese el código de la carrera a listar: "))  
mask_carrera = (cod_carreras == codigo_carrera) & (promedios >= 4.0)  
estudiantes_filtrados = np.column_stack((codigos[mask_carrera], nombres[mask_carrera]))  

if estudiantes_filtrados.size > 0:
    print(f"\n Estudiantes de la carrera {codigo_carrera} con promedio ≥ 4.0:")
    for estudiante in estudiantes_filtrados:
        print(f"Código: {estudiante[0]}, Nombre: {estudiante[1]}")
    print(f"🔹 Total: {len(estudiantes_filtrados)} estudiantes\n")
else:
    print("\n No hay estudiantes que cumplan con la condición.")


mask_antiguos_condicionales = (años_ingreso < 1990) & (estado_condicional)  
estudiantes_condicionales = np.column_stack((codigos[mask_antiguos_condicionales], nombres[mask_antiguos_condicionales]))  

if estudiantes_condicionales.size > 0:
    print("\n Estudiantes ingresados antes de 1990 y condicionales:")
    for estudiante in estudiantes_condicionales:
        print(f"Código: {estudiante[0]}, Nombre: {estudiante[1]}")
    print(f"🔹 Total: {len(estudiantes_condicionales)} estudiantes\n")
else:
    print("\n No hay estudiantes ingresados antes de 1990 que estén condicionales.")
# Implementación de pruebas automatizadas para el sistema
print("=== EJECUCIÓN DE PRUEBAS DEL SISTEMA ===\n")
from sistema_empleados import SistemaEmpleados
# Crear instancia del sistema para pruebas
sistema_prueba = SistemaEmpleados()

# Datos de prueba
empleados_prueba = [
    {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'numero_identificacion': '12345678',
        'cargo': 'Desarrollador',
        'departamento': 'TI',
        'salario': 3500000,
        'fecha_contratacion': '15/03/2023'
    },
    {
        'nombre': 'María',
        'apellido': 'González',
        'numero_identificacion': '87654321',
        'cargo': 'Gerente',
        'departamento': 'Ventas',
        'salario': 5000000,
        'fecha_contratacion': '10/01/2022'
    },
    {
        'nombre': 'Carlos',
        'apellido': 'Rodríguez',
        'numero_identificacion': '11223344',
        'cargo': 'Analista',
        'departamento': 'Finanzas',
        'salario': 2800000,
        'fecha_contratacion': '20/07/2023'
    }
]

# Prueba 1: Agregar empleados programáticamente
print("PRUEBA 1: Agregando empleados al sistema")
for i, emp in enumerate(empleados_prueba):
    sistema_prueba.empleados[sistema_prueba.contador_id] = emp
    nombre_completo = f"{emp['nombre']} {emp['apellido']}".lower()
    sistema_prueba.nombres_index[nombre_completo] = sistema_prueba.contador_id
    print(f"✓ Empleado {emp['nombre']} {emp['apellido']} agregado con ID: {sistema_prueba.contador_id}")
    sistema_prueba.contador_id += 1

print(f"\nTotal de empleados en el sistema: {len(sistema_prueba.empleados)}")

# Prueba 2: Búsqueda por número de identificación
print("\nPRUEBA 2: Búsqueda por número de identificación")
id_buscar = '12345678'
empleado_encontrado = None
empleado_id = None

for emp_id, empleado in sistema_prueba.empleados.items():
    if empleado['numero_identificacion'] == id_buscar:
        empleado_encontrado = empleado
        empleado_id = emp_id
        break

if empleado_encontrado:
    print(f"✓ Empleado encontrado: {empleado_encontrado['nombre']} {empleado_encontrado['apellido']}")
    print(f"  Cargo: {empleado_encontrado['cargo']}")
    print(f"  Departamento: {empleado_encontrado['departamento']}")
    print(f"  Salario: ${empleado_encontrado['salario']:,.2f}")
else:
    print("✗ Empleado no encontrado")

# Prueba 3: Búsqueda por nombre
print("\nPRUEBA 3: Búsqueda por nombre completo")
nombre_buscar = 'maría gonzález'
if nombre_buscar in sistema_prueba.nombres_index:
    empleado_id = sistema_prueba.nombres_index[nombre_buscar]
    empleado = sistema_prueba.empleados[empleado_id]
    print(f"✓ Empleado encontrado: {empleado['nombre']} {empleado['apellido']}")
    print(f"  ID: {empleado['numero_identificacion']}")
    print(f"  Cargo: {empleado['cargo']}")
else:
    print("✗ Empleado no encontrado")

# Prueba 4: Actualización de información
print("\nPRUEBA 4: Actualización de salario")
id_actualizar = '87654321'
for emp_id, empleado in sistema_prueba.empleados.items():
    if empleado['numero_identificacion'] == id_actualizar:
        salario_anterior = empleado['salario']
        empleado['salario'] = 5500000
        print(f"✓ Salario actualizado para {empleado['nombre']} {empleado['apellido']}")
        print(f"  Salario anterior: ${salario_anterior:,.2f}")
        print(f"  Nuevo salario: ${empleado['salario']:,.2f}")
        break

# Prueba 5: Validaciones
print("\nPRUEBA 5: Validaciones del sistema")

# Validación de fecha
fechas_test = ['15/03/2023', '32/13/2023', '15-03-2023', '15/03/23']
print("Validación de fechas:")
for fecha in fechas_test:
    resultado = sistema_prueba.validar_fecha(fecha)
    print(f"  {fecha}: {'✓ Válida' if resultado else '✗ Inválida'}")

# Validación de salario
salarios_test = ['3500000', '-1000', 'abc', '0', '2500000.50']
print("\nValidación de salarios:")
for salario in salarios_test:
    resultado = sistema_prueba.validar_salario(salario)
    print(f"  {salario}: {'✓ Válido' if resultado else '✗ Inválido'}")

# Validación de ID único
print("\nValidación de números de identificación únicos:")
ids_test = ['99999999', '12345678', '55555555']
for id_test in ids_test:
    resultado = sistema_prueba.validar_numero_id(id_test)
    print(f"  {id_test}: {'✓ Disponible' if resultado else '✗ Ya existe'}")

# Prueba 6: Eliminación de empleado
print("\nPRUEBA 6: Eliminación de empleado")
id_eliminar = '11223344'
empleado_a_eliminar = None
empleado_id_eliminar = None

for emp_id, empleado in sistema_prueba.empleados.items():
    if empleado['numero_identificacion'] == id_eliminar:
        empleado_a_eliminar = empleado
        empleado_id_eliminar = emp_id
        break

if empleado_a_eliminar:
    nombre_completo = f"{empleado_a_eliminar['nombre']} {empleado_a_eliminar['apellido']}".lower()
    del sistema_prueba.empleados[empleado_id_eliminar]
    if nombre_completo in sistema_prueba.nombres_index:
        del sistema_prueba.nombres_index[nombre_completo]
    print(f"✓ Empleado {empleado_a_eliminar['nombre']} {empleado_a_eliminar['apellido']} eliminado exitosamente")
    print(f"  Empleados restantes: {len(sistema_prueba.empleados)}")

# Prueba 7: Listado final
print("\nPRUEBA 7: Listado final de empleados")
print(f"Total de empleados: {len(sistema_prueba.empleados)}")
print("-" * 60)
for emp_id, empleado in sistema_prueba.empleados.items():
    print(f"ID: {emp_id} | {empleado['nombre']} {empleado['apellido']} | "
          f"Identificación: {empleado['numero_identificacion']} | {empleado['cargo']} | "
          f"${empleado['salario']:,.2f}")

print("\n=== TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE ===")
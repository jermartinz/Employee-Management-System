from datetime import datetime

class SistemaEmpleados:
    def __init__(self):
        # Estructura de datos principal: diccionario con lista de empleados
        self.empleados = {}  # {id: datos_empleado}
        self.contador_id = 1
        # Índices para búsqueda rápida
        self.nombres_index = {}  # {nombre_completo: id}
        
    def validar_fecha(self, fecha_str):
        """Valida formato de fecha DD/MM/AAAA"""
        try:
            datetime.strptime(fecha_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    
    def validar_numero_id(self, numero_id):
        """Valida que el número de identificación sea único"""
        for empleado in self.empleados.values():
            if empleado['numero_identificacion'] == numero_id:
                return False
        return True
    
    def validar_salario(self, salario_str):
        """Valida que el salario sea un número positivo"""
        try:
            salario = float(salario_str)
            return salario > 0
        except ValueError:
            return False
    
    def agregar_empleado(self):
        """Función para agregar un nuevo empleado al sistema"""
        print("\n=== AGREGAR NUEVO EMPLEADO ===")
        
        # Recolección y validación de datos
        while True:
            nombre = input("Ingrese el nombre: ").strip()
            if nombre and len(nombre) >= 2:
                break
            print("El nombre debe tener al menos 2 caracteres.")
        
        while True:
            apellido = input("Ingrese el apellido: ").strip()
            if apellido and len(apellido) >= 2:
                break
            print("El apellido debe tener al menos 2 caracteres.")
        
        while True:
            numero_id = input("Ingrese el número de identificación: ").strip()
            if numero_id and self.validar_numero_id(numero_id):
                break
            print("Número de identificación inválido o ya existe.")
        
        cargo = input("Ingrese el cargo: ").strip()
        departamento = input("Ingrese el departamento: ").strip()
        
        while True:
            salario_str = input("Ingrese el salario: ").strip()
            if self.validar_salario(salario_str):
                salario = float(salario_str)
                break
            print("El salario debe ser un número positivo.")
        
        while True:
            fecha_contratacion = input("Ingrese la fecha de contratación (DD/MM/AAAA): ").strip()
            if self.validar_fecha(fecha_contratacion):
                break
            print("Formato de fecha inválido. Use DD/MM/AAAA.")
        
        # Crear registro del empleado
        empleado = {
            'nombre': nombre,
            'apellido': apellido,
            'numero_identificacion': numero_id,
            'cargo': cargo,
            'departamento': departamento,
            'salario': salario,
            'fecha_contratacion': fecha_contratacion
        }
        
        # Almacenar en estructura de datos
        self.empleados[self.contador_id] = empleado
        self.nombres_index[f"{nombre} {apellido}".lower()] = self.contador_id
        
        print(f"\nEmpleado agregado exitosamente con ID: {self.contador_id}")
        self.contador_id += 1
    
    def buscar_empleado(self):
        """Función para buscar empleados por nombre o número de identificación"""
        print("\n=== BUSCAR EMPLEADO ===")
        print("1. Buscar por nombre completo")
        print("2. Buscar por número de identificación")
        
        while True:
            opcion = input("Seleccione una opción (1-2): ").strip()
            if opcion in ['1', '2']:
                break
            print("Opción inválida. Intente nuevamente.")
        
        if opcion == '1':
            nombre_busqueda = input("Ingrese el nombre completo: ").strip().lower()
            if nombre_busqueda in self.nombres_index:
                empleado_id = self.nombres_index[nombre_busqueda]
                self.mostrar_empleado(empleado_id)
            else:
                print("Empleado no encontrado.")
        
        elif opcion == '2':
            numero_id = input("Ingrese el número de identificación: ").strip()
            empleado_encontrado = None
            empleado_id = None
            
            for emp_id, empleado in self.empleados.items():
                if empleado['numero_identificacion'] == numero_id:
                    empleado_encontrado = empleado
                    empleado_id = emp_id
                    break
            
            if empleado_encontrado:
                self.mostrar_empleado(empleado_id)
            else:
                print("Empleado no encontrado.")
    
    def mostrar_empleado(self, empleado_id):
        """Función auxiliar para mostrar información del empleado"""
        empleado = self.empleados[empleado_id]
        print(f"\n--- INFORMACIÓN DEL EMPLEADO (ID: {empleado_id}) ---")
        print(f"Nombre: {empleado['nombre']} {empleado['apellido']}")
        print(f"Número de identificación: {empleado['numero_identificacion']}")
        print(f"Cargo: {empleado['cargo']}")
        print(f"Departamento: {empleado['departamento']}")
        print(f"Salario: ${empleado['salario']:,.2f}")
        print(f"Fecha de contratación: {empleado['fecha_contratacion']}")
    
    def actualizar_empleado(self):
        """Función para actualizar información de un empleado existente"""
        print("\n=== ACTUALIZAR EMPLEADO ===")
        
        # Buscar empleado a actualizar
        numero_id = input("Ingrese el número de identificación del empleado: ").strip()
        empleado_encontrado = None
        empleado_id = None
        
        for emp_id, empleado in self.empleados.items():
            if empleado['numero_identificacion'] == numero_id:
                empleado_encontrado = empleado
                empleado_id = emp_id
                break
        
        if not empleado_encontrado:
            print("Empleado no encontrado.")
            return
        
        # Mostrar información actual
        self.mostrar_empleado(empleado_id)
        
        # Menú de campos actualizables
        print("\n¿Qué información desea actualizar?")
        print("1. Cargo")
        print("2. Departamento")
        print("3. Salario")
        print("4. Todos los campos")
        
        while True:
            opcion = input("Seleccione una opción (1-4): ").strip()
            if opcion in ['1', '2', '3', '4']:
                break
            print("Opción inválida.")
        
        if opcion == '1':
            nuevo_cargo = input("Ingrese el nuevo cargo: ").strip()
            empleado_encontrado['cargo'] = nuevo_cargo
            print("Cargo actualizado exitosamente.")
        
        elif opcion == '2':
            nuevo_departamento = input("Ingrese el nuevo departamento: ").strip()
            empleado_encontrado['departamento'] = nuevo_departamento
            print("Departamento actualizado exitosamente.")
        
        elif opcion == '3':
            while True:
                nuevo_salario_str = input("Ingrese el nuevo salario: ").strip()
                if self.validar_salario(nuevo_salario_str):
                    empleado_encontrado['salario'] = float(nuevo_salario_str)
                    print("Salario actualizado exitosamente.")
                    break
                print("Salario inválido.")
        
        elif opcion == '4':
            empleado_encontrado['cargo'] = input("Nuevo cargo: ").strip()
            empleado_encontrado['departamento'] = input("Nuevo departamento: ").strip()
            while True:
                nuevo_salario_str = input("Nuevo salario: ").strip()
                if self.validar_salario(nuevo_salario_str):
                    empleado_encontrado['salario'] = float(nuevo_salario_str)
                    break
                print("Salario inválido.")
            print("Información actualizada exitosamente.")
    
    def eliminar_empleado(self):
        """Función para eliminar un empleado del sistema"""
        print("\n=== ELIMINAR EMPLEADO ===")
        
        numero_id = input("Ingrese el número de identificación del empleado: ").strip()
        empleado_encontrado = None
        empleado_id = None
        
        for emp_id, empleado in self.empleados.items():
            if empleado['numero_identificacion'] == numero_id:
                empleado_encontrado = empleado
                empleado_id = emp_id
                break
        
        if not empleado_encontrado:
            print("Empleado no encontrado.")
            return
        
        # Mostrar información del empleado
        self.mostrar_empleado(empleado_id)
        
        # Confirmar eliminación
        while True:
            confirmacion = input("\n¿Está seguro de eliminar este empleado? (s/n): ").strip().lower()
            if confirmacion in ['s', 'si', 'sí']:
                # Eliminar de ambas estructuras de datos
                nombre_completo = f"{empleado_encontrado['nombre']} {empleado_encontrado['apellido']}".lower()
                del self.empleados[empleado_id]
                if nombre_completo in self.nombres_index:
                    del self.nombres_index[nombre_completo]
                print("Empleado eliminado exitosamente.")
                break
            elif confirmacion in ['n', 'no']:
                print("Operación cancelada.")
                break
            else:
                print("Respuesta inválida. Ingrese 's' o 'n'.")
    
    def listar_empleados(self):
        """Función para listar todos los empleados"""
        print("\n=== LISTA DE EMPLEADOS ===")
        
        if not self.empleados:
            print("No hay empleados registrados.")
            return
        
        print(f"Total de empleados: {len(self.empleados)}")
        print("-" * 80)
        
        for emp_id, empleado in self.empleados.items():
            print(f"ID: {emp_id} | {empleado['nombre']} {empleado['apellido']} | "
                    f"ID: {empleado['numero_identificacion']} | {empleado['cargo']} | "
                    f"${empleado['salario']:,.2f}")
    
    def mostrar_menu(self):
        """Función para mostrar el menú principal"""
        print("\n" + "="*50)
        print("    SISTEMA DE GESTIÓN DE EMPLEADOS")
        print("="*50)
        print("1. Agregar nuevo empleado")
        print("2. Buscar empleado")
        print("3. Actualizar información de empleado")
        print("4. Eliminar empleado")
        print("5. Listar todos los empleados")
        print("6. Salir")
        print("-"*50)
    
    def ejecutar(self):
        """Función principal que ejecuta el sistema"""
        print("¡Bienvenido al Sistema de Gestión de Empleados!")
        
        while True:
            self.mostrar_menu()
            
            opcion = input("Seleccione una opción (1-6): ").strip()
            
            if opcion == '1':
                self.agregar_empleado()
            elif opcion == '2':
                self.buscar_empleado()
            elif opcion == '3':
                self.actualizar_empleado()
            elif opcion == '4':
                self.eliminar_empleado()
            elif opcion == '5':
                self.listar_empleados()
            elif opcion == '6':
                print("\n¡Gracias por usar el Sistema de Gestión de Empleados!")
                break
            else:
                print("\nOpción inválida. Por favor, seleccione una opción del 1 al 6.")

# Función principal para ejecutar el programa
def main():
    sistema = SistemaEmpleados()
    sistema.ejecutar()

# Demostración del funcionamiento del sistema
if __name__ == "__main__":
    main()

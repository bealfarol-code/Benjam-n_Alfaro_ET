planes = {
    'F001' : ['Plan basico', ' mensual', 1, False, False, 'libre'],
    'F002' : ['Plan full', ' mensual', 1, True,True, 'libre'],
    'F003' : ['Plan estudiante', 'Trimestral', 3, False, True,'tarde'],
    'F004' : ['Plan senior', 'Trimestral', 3, True, False,'mañana'],
    'F005' : ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006' : ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [15990, 2],
    'F006': [18990, 15]
}

def Validar_codigos(codigo, planes, inscripciones):
    return codigo.strip()!= "" and codigo.upper() not in planes

def Validar_nombre(nombre):
    return nombre.strip()!= ""

def Validar_tipo(tipo):
    return tipo.lower() in ['mensual', 'trimestral', 'anual']

def Validar_entero_mayor_cero(valor):
    return isinstance(valor, int) and valor > 0

def Validar_entero_mayor_igual_cero(valor):
    return isinstance(valor, int) and valor >= 0

def Validar_sn(valor):
    return valor.lower() in ['s', 'n']

def Validar_horario(horario):
    return horario.stip()!= ""

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")

def cupos_tipo(tipo, planes, inscripciones):
    tipo = tipo.lower()
    total_cupos = 0
    for codigo, datos in planes.items():
        if datos[1].lower() == tipo:
            total_cupos += inscripciones[codigo][1]
    print(f"El total de cupos disponibles es: {total_cupos}")

def busqueda_precio(p_min, p_max, planes, inscripciones):
    resultado = []
    for codigo, datos in inscripciones.items():
        precio = datos[0]
        cupos = datos[1]
        if p_min <= precio <= p_max and cupos > 0:
            nombre = planes[codigo][0]
            resultado.append(f"{nombre}---{codigo}")
    
    if resultado:
        resultado.sort()
        print(f"Los planes encontrados son: {resultado}")
    else:
        print("No hay planes en ese rango de precios.")
def Buscar_codigo(codigo, inscripciones):
    return codigo.upper() in inscripciones

def Actualizar_precio(codigo, nuevo_precio, inscripciones):
    codigo = codigo.upper()
    if Buscar_codigo(codigo, inscripciones):
        inscripciones[codigo][0] = nuevo_precio
        return True
    return False

def Agregar_plan(codigo, nombre, tipo, duracion, acceso, clases, horario, precio, cupos, planes, inscripciones):
    codigo = codigo.upper()
    planes[codigo] = [nombre, tipo, duracion, acceso, horario]
    inscripciones[codigo] = [precio, cupos]
    return True

def eliminar_plan(codigo, planes, inscripciones):
    codigo = codigo.upper()
    if Buscar_codigo(codigo, inscripciones):
        del planes[codigo]
        del inscripciones[codigo]
        return True
    return False 

def main():
    while True:
        print("\n===========MENU PRINCIPAL==============")
        print("1. Cupos por tipo de plan")
        print("2. Busqueda de planes por rango")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar plan")
        print("6. Salir")
        print("=========================================")

        opcion = leer_opcion()

        if opcion == 1:
            tipo = input("Ingrese tipo de plan a consultar:")
            cupos_tipo(tipo, planes, inscripciones)
        
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max, planes, inscripciones)
                        break
                    else:
                        print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")
        elif opcion == 3:
            codigo = input("Ingree codigo del plan: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
            except ValueError:
                print("El precio debe ser un numero entero")
                continue

            if Actualizar_precio(codigo, nuevo_precio, inscripciones):
                print("Precio actualizado")
            else:
                print("El codigo no existe")
            
            resp = int(input("¿Desea actualizar otr precio (s/n)?"))
            while resp.lower() not in ['s', 'n']:
                resp = input("¿Desea actualizar otro precio (s/n)?")
            if resp.lower() == 's':
                continue
                
        elif opcion == 4:
            codigo = input("Ingrese codigo del plan: ")
            if not Validar_codigos(codigo, planes, inscripciones):
                print("El codigo ya existe")
                continue

            nombre = input("ingrese un nombre del plan: ")
            if not Validar_nombre(nombre):
                print("Nombre invalido")
                continue

            tipo = input("Ingrese tipo (mensual, trimestral, anual)")
            if not Validar_tipo(tipo):
                print("Tipo invalido")
                continue
            try:
                duracion = input("Ingrese la duracion (mes): ")
                if not Validar_entero_mayor_cero(duracion):
                    print("Duracion invalida")
                    continue
            except ValueError:
                print("Duracion invalida")
                continue
            acceso = input("¿Ingreso a la piscina (s/n)?: ")
            if not Validar_sn(acceso):
                print("Opcion invalida")
                continue
            acceso_bool = True if acceso.lower() == 's' else False

            clases = input("¿Incluye clase grupales (s/n)?: ")
            if not Validar_sn(clases):
                print("Opcion invalida")
                continue
            clases_bool = True if clases.lower() == 's' else False
            
            horario = input("Ingrese horario: ")
            if not Validar_horario(horario):
                print("Horario invalido")
                continue

            try:
                precio = int(input("Ingrese precio: "))
                if not Validar_entero_mayor_cero(precio):
                    print("Precio invalidos")
                    continue
            except ValueError:
                print("Precio invalidos")
                continue

            try:
                cupos = int(input("Ingrese cupos: "))
                if not Validar_entero_mayor_igual_cero(cupos):
                    print("Cupos invalidos")
                    continue
            except ValueError:
                print("Cupos invalidos")
                continue

            if Agregar_plan(codigo, nombre, tipo, duracion, acceso_bool, clases_bool, horario, precio, cupos, planes, inscripciones):
                print("Plan agregado")
        elif opcion == 5:
            codigo = input("Ingrese le codigo del plan a eliminar: ")
            if eliminar_plan(codigo, planes, inscripciones):
                print("Plan eliminado")
            else:
                print("El codigo no existe")
        elif opcion == 6:
            print("Programa finalizado.")
            break
if __name__ == "__main__":
    main()
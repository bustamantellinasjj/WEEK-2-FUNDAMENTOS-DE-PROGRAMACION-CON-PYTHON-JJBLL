# ============================================================
# SISTEMA DE INVENTARIO | CONTROL DE FLUJO Y LISTAS
# Gestiona productos mediante un menú interactivo.
# Usa listas, diccionarios, funciones, bucles y condicionales.
# ============================================================

# CREO LA LISTA DE INVENTARIO VACIA PARA ALMACENAR LOS PRODUCTOS.
# CADA PRODUCTO SERÁ UN DICCIONARIO CON NOMBRE, PRECIO Y CANTIDAD.
inventario = []

# ============================================================
# FUNCIÓN1: agregar_producto()
# SOLICITA AL USUARIO LOS DATOS DEL PRODUCTO CON VALIDACIÓN.
# CREA UN DICCIONARIO Y LO AGREGA A LA LISTA inventario.
# ============================================================
def agregar_producto():

    # BUCLE PARA PERMITIR AL USUARIO VOLVER A INGRESAR LOS DATOS SI COMETE UN ERROR.
    Volver_Preguntar = True
    while Volver_Preguntar:
        try:
            nombre_producto = input("\nINGRESE EL NOMBRE DEL PRODUCTO: ") # (DATO1) SOLICITA AL USUARIO EL NOMBRE DEL PRODUCTO.
            if len(nombre_producto) > 20: # VALIDACIÓN PARA QUE EL NOMBRE NO EXCEDA LOS 20 CARACTERES.
                print("\nNOMBRE INVALIDO. MAXIMO 20 CARACTERES.") # MENSAJE DE ERROR PARA EL USUARIO.
                continue # VUELVE A MOSTRAR EL MENÚ PARA QUE EL USUARIO PUEDA INGRESAR UN NOMBRE VÁLIDO.
            elif len(nombre_producto) == 0: # VALIDACIÓN PARA QUE EL NOMBRE NO ESTÉ VACÍO.
                print("\nNOMBRE INVALIDO. NO PUEDE ESTAR VACÍO.") # MENSAJE DE ERROR PARA EL USUARIO.
                continue # VUELVE A MOSTRAR EL MENÚ PARA QUE EL USUARIO PUEDA INGRESAR UN NOMBRE VÁLIDO.
            else:
                Volver_Preguntar = False # SI EL NOMBRE ES VÁLIDO, SALE DEL BUCLE Y CONTINUA CON LA SOLICITUD DE LOS DEMÁS DATOS DEL PRODUCTO.
        except (ValueError, EOFError, KeyboardInterrupt):  # SI EL USUARIO INTERRUMPE EL PROGRAMA CON CTRL+C, MUESTRA UN MENSAJE DE ERROR Y VUELVE A PREGUNTAR EL NOMBRE DEL PRODUCTO.
            print("\nINGRESA UN NOMBRE VALIDO.") # MENSAJE DE ERROR PARA EL USUARIO.
            continue # VUELVE A MOSTRAR EL MENÚ PARA QUE EL USUARIO PUEDA INGRESAR UN NOMBRE VÁLIDO.

    # BUCLE PARA PERMITIR AL USUARIO VOLVER A INGRESAR LOS DATOS SI COMETE UN ERROR.
    Volver_Preguntar = True
    while Volver_Preguntar:
        try:
            precio_producto = float(input("\nINGRESE EL PRECIO DEL PRODUCTO: ")) # (DATO2) SOLICITA AL USUARIO EL PRECIO DEL PRODUCTO.
            if precio_producto < 0: # VALIDACIÓN PARA QUE EL PRECIO NO SEA UN NUMERO NEGATIVO.
                print("\nPRECIO INVALIDO. NO PUEDE SER NEGATIVO.")  # MENSAJE DE ERROR PARA EL USUARIO.
                continue # VUELVE A MOSTRAR EL MENÚ PARA QUE EL USUARIO PUEDA INGRESAR UN PRECIO VÁLIDA.
            else: 
                Volver_Preguntar = False # SI EL PRECIO ES VÁLIDO, SALE DEL BUCLE Y CONTINUA CON LA SOLICITUD DE LOS DEMÁS DATOS DEL PRODUCTO.
        except (ValueError, EOFError, KeyboardInterrupt): # SI EL USUARIO INTERRUMPE EL PROGRAMA CON CTRL+C, MUESTRA UN MENSAJE DE ERROR Y VUELVE A PREGUNTAR EL PRECIO DEL PRODUCTO.
            print("\nINGRESA UN PRECIO VALIDO.") # MENSAJE DE ERROR PARA EL USUARIO.
            continue # VUELVE A MOSTRAR EL MENÚ PARA QUE EL USUARIO PUEDA INGRESAR UN NOMBRE VÁLIDO.

 # BUCLE PARA PERMITIR AL USUARIO VOLVER A INGRESAR LOS DATOS SI COMETE UN ERROR.
    Volver_Preguntar = True
    while Volver_Preguntar:
        try:
            cantidad_producto = int(input("\nINGRESE LA CANTIDAD DEL PRODUCTO: ")) # (DATO3) SOLICITA AL USUARIO LA CANTIDAD DEL PRODUCTO.
            if cantidad_producto < 0: # VALIDACIÓN PARA QUE LA CANTIDAD NO SEA UN NUMERO NEGATIVO.
                print("\nCANTIDAD INVALIDA. NO PUEDE SER NEGATIVA.") # MENSAJE DE ERROR PARA EL USUARIO.
                continue
            else:
                Volver_Preguntar = False  # SI LA CANTIDAD ES VÁLIDA, SALE DEL BUCLE.
        except (ValueError, EOFError, KeyboardInterrupt):  # SI EL USUARIO INTERRUMPE EL PROGRAMA CON CTRL+C, MUESTRA UN MENSAJE DE ERROR Y VUELVE A PREGUNTAR EL PRECIO DEL PRODUCTO.
            print("\nINGRESA UNA CANTIDAD VALIDA.") # MENSAJE DE ERROR PARA EL USUARIO.
            continue # VUELVE A MOSTRAR EL MENÚ PARA QUE EL USUARIO PUEDA INGRESAR UN NOMBRE VÁLIDO.

    # CREO UN DICCIONARIO PARA ALMACENAR LOS DETALLES DEL PRODUCTO Y LO AGREGO A LA LISTA inventario.
    producto = {
        "nombre"  : nombre_producto,
        "precio"  : precio_producto,
        "cantidad": cantidad_producto
    }
    inventario.append(producto)  # AGREGA EL PRODUCTO AL INVENTARIO.
    print(f"\nEL PRODUCTO '{nombre_producto}' FUE AGREGADO EXITOSAMENTE.") # MENSAJE DE CONFIRMACION PARA EL USUARIO.


# ============================================================
# FUNCIÓN2: mostrar_inventario()
# RECORRE LA LISTA inventario CON UN BUCLE for Y MUESTRA CADA PRODUCTO CON SU NOMBRE, PRECIO Y CANTIDAD.
# FORMATO: Producto: X | Precio: X | Cantidad: X
# SI EL INVENTARIO ESTÁ VACÍO, MUESTRA UN MENSAJE INDICÁNDOLO.
# ============================================================
def mostrar_inventario():
    if len(inventario) == 0:  # SI EL INVENTARIO ESTÁ VACÍO, MUESTRA UN MENSAJE AL USUARIO.
        print("\nEL INVENTARIO ESTÁ VACÍO.")  # MENSAJE PARA EL USUARIO.
    else:
        print("\n||||| INVENTARIO ACTUAL |||||") # ENCABEZADO PARA MOSTRAR EL INVENTARIO AL USUARIO.
        # RECORREMOS LA LISTA CON enumerate PARA NUMERAR CADA PRODUCTO.
        for i, producto in enumerate(inventario, start=1): # enumerate ME DA DOS COSAS A LA VEZ: EL ÍNDICE (i) Y EL ELEMENTO (producto) DE LA LISTA DE INVENTARIO, COMENZANDO EL ÍNDICE EN 1 (start=1).
            print(f"\nProducto {i}:") # MUESTRA EL NÚMERO DEL PRODUCTO EN EL INVENTARIO.
            print(f"  Producto: {producto['nombre']} | Precio: {producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
# PRIMERO: ACCEDE A LA LLAVE 'nombre' DEL DICCIONARIO.
# SEGUNDO: ACCEDE A LA LLAVE 'precio' Y LA FORMATEA A DOS DECIMALES CON :.2f.
# TERCERO: ACCEDE A LA LLAVE 'cantidad' DEL DICCIONARIO.

# ============================================================
# FUNCIÓN3: calcular_estadisticas()
# RECORRE EL INVENTARIO CALCULANDO:
#   - VALOR TOTAL: SUMA DE (precio × cantidad) DE CADA PRODUCTO.
#   - CANTIDAD TOTAL: SUMA TODAS LAS CANTIDADES DE LOS PRODUCTOS.
# ============================================================
def calcular_estadisticas():
    if len(inventario) == 0: # SI EL INVENTARIO ESTÁ VACÍO, MUESTRA UN MENSAJE AL USUARIO Y SALE DE LA FUNCIÓN.
        print("\nEL INVENTARIO ESTÁ VACÍO. NO HAY ESTADÍSTICAS QUE CALCULAR.") # MENSAJE PARA EL USUARIO.
        return # SALE DE LA FUNCION SI EL INVENTARIO ESTA VACIO.

    total = 0
    cantidad_total = 0

    # RECORREMOS CADA PRODUCTO Y ACUMULAMOS LOS TOTALES:
    for producto in inventario: # RECORRE CADA PRODUCTO EN EL INVENTARIO PARA CALCULAR EL VALOR TOTAL DEL INVENTARIO Y LA CANTIDAD TOTAL DE PRODUCTOS.
        total          += producto["precio"] * producto["cantidad"]  # CALCULA EL VALOR DE CADA PRODUCTO MULTIPLICANDO SU PRECIO POR SU CANTIDAD Y LO SUMA AL TOTAL. (SUBTOTAL DE CADA PRODUCTO)
        cantidad_total += producto["cantidad"]                       # SUMA LA CANTIDAD DE UNIDADES DE CADA PRODUCTO AL TOTAL DE CANTIDAD.
    print("\n||||| ESTADÍSTICAS DEL INVENTARIO |||||") # ENCABEZADO PARA MOSTRAR LAS ESTADÍSTICAS AL USUARIO.
    print(f"\nVALOR TOTAL DEL INVENTARIO: ${total:.2f}") # MUESTRA EL VALOR TOTAL DEL INVENTARIO FORMATEADO A 2 DECIMALES.
    print(f"CANTIDAD TOTAL DE PRODUCTOS: {cantidad_total} uds") # MUESTRA LA CANTIDAD TOTAL DE PRODUCTOS EN EL INVENTARIO.



# ============================================================
# MENÚ PRINCIPAL
# BUCLE PRINCIPAL QUE MUESTRA EL MENÚ HASTA QUE EL USUARIO DECIDA SALIR.
#  USAMOS if/elif/else PARA CADDA OPCIÓN DEL MENÚ, LLAMANDO A LA FUNCIÓN CORRESPONDIENTE.
# MANEJA OPCIONES INVALIDAS SIN CERRAR EL PROGRAMA, PERMITIENDO AL USUARIO VOLVER A INTENTAR.
# ============================================================
SeguirMostrandoMenu = True
while SeguirMostrandoMenu:

    print("\n||||| MENU DE INVENTARIO |||||") # ENCABEZADO PARA MOSTRAR EL MENÚ AL USUARIO.
    print("\n1. AGREGAR PRODUCTO.") 
    print("2. MOSTRAR INVENTARIO.")
    print("3. CALCULAR ESTADÍSTICAS.")
    print("4. SALIR.")

    # VALIDAMOS QUE LA OPCIÓN SEA UN NÚMERO ENTERO.
    try:
        opcion = int(input("\nSELECCIONE UNA OPCIÓN: "))
    except (ValueError, EOFError, KeyboardInterrupt):
        print("\nOPCIÓN INVÁLIDA. POR FAVOR, SELECCIONE UN NÚMERO DEL 1 AL 4.")
        continue

    # CONDICIONALES PARA PROCESAR LA OPCIÓN ELEGIDA.
    if opcion == 1:                 # SI EL USUARIO ELIGE 1, LLAMA A LA FUNCIÓN agregar_producto()
        agregar_producto()          # LLAMA LA FUNCIÓN PARA AGREGAR UN PRODUCTO.

    elif opcion == 2:               # SI EL USUARIO ELIGE 2, LLAMA A LA FUNCIÓN mostrar_inventario()
        mostrar_inventario()        # LLAMA LA FUNCIÓN PARA MOSTRAR EL INVENTARIO.

    elif opcion == 3:               # SI EL USUARIO ELIGE 3, LLAMA A LA FUNCIÓN calcular_estadisticas()
        calcular_estadisticas()     # LLAMA LA FUNCIÓN PARA CALCULAR LAS ESTADÍSTICAS DEL INVENTARIO.

    elif opcion == 4:
        print("\nGRACIAS POR USAR EL INVENTARIO. ¡HASTA PRONTO!") # MENSAJE DE DESPEDIDA PARA EL USUARIO.
        SeguirMostrandoMenu = False  # CAMBIO LA VARIABLE PARA SALIR DEL BUCLE Y TERMINAR EL PROGRAMA.

    else:
        print("\nOPCIÓN INVÁLIDA. POR FAVOR, SELECCIONE UN NÚMERO DEL 1 AL 4.") # MENSAJE DE ERROR PARA EL USUARIO.


# ============================================================
# RESUMEN DEL OBJETIVO DE LA SEMANA:
# EN ESTA SESIÓN SE APLICARON ESTRUCTURAS DE CONTROL DE FLUJO
# (if/elif/else y while) JUNTO CON ESTRUCTURAS DE DATOS (listas y diccionarios) 
# PARA CONTRUIR UN SISTEMA DE INVENTARIO MODULAR ACADA FUNCION FUE ENCAPSULADA EN UNA FUNCIÓN INDEPENDIENTE (AGREGAR, MOSTRAR, ESTADÍSTICAS), 
# Y EL MENÚ PRINCIPAL DELEGA EN ELLAS USANDO CONDICIONALES. 
# SE VALIDARON ENTRADAS CON TRY/EXCEPT PARA QUE NINGÚN ERROR DEL USUARIO CIERRE EL PROGRAMA ABRUPTAMENTE.
# ============================================================
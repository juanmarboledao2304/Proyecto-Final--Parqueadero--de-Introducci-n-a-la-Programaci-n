import json

def existePlaca (x, usuarios): # Función para validar si la placa se encuentra en el archivo de usuario
    existe = False
    n = 0
    while (n < len(usuarios)):
        if (placa == usuarios[n][3]):
            existe = True
        n += 1
    return existe
# Función que reinicia el dicccionario que contiene la ocupación de los estacionamientos para el correcto desarrollo del programa
def reiniciarParqueaderoDisponible ():
    parqueaderoDisponible = {
	"Piso1": [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]],
	"Piso2": [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]],
	"Piso3": [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]],
	"Piso4": [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]],
	"Piso5": [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]],
	"Piso6": [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
		["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]]
}
    return parqueaderoDisponible


archivoParqueadero = open("tiposParqueaderos.json", "r", encoding = "utf-8")
parqueadero = json.load(archivoParqueadero)
archivoParqueadero.close

parqueaderoDisponible = reiniciarParqueaderoDisponible()

archivoUsuarios = open("usuarios.json", "r", encoding = "utf-8")
usuarios = json.load(archivoUsuarios)
archivoUsuarios.close

piso1 = parqueadero["Piso1"] # Se define una variable para cada piso del archivo
piso2 = parqueadero["Piso2"] # Se define una variable para cada piso del archivo
piso3 = parqueadero["Piso3"] # Se define una variable para cada piso del archivo
piso4 = parqueadero["Piso4"] # Se define una variable para cada piso del archivo
piso5 = parqueadero["Piso5"] # Se define una variable para cada piso del archivo
piso6 = parqueadero["Piso6"] # Se define una variable para cada piso del archivo

disponibles1 = []  # Se crea una variable(lista) para guardar las filas y columnas dependiendo de cada vehiculo
disponibles2 = []  # Se crea una variable(lista) para guardar las filas y columnas dependiendo de cada vehiculo
disponibles3 = []  # Se crea una variable(lista) para guardar las filas y columnas dependiendo de cada vehiculo
disponibles4 = []  # Se crea una variable(lista) para guardar las filas y columnas dependiendo de cada vehiculo
p = 0
while (p < 6): # Se recorre piso por piso y se añaden las filas y las columnas correspondientes a cada lista
    if (p == 0):
        piso = "Piso1"
    elif (p == 1):
        piso = "Piso2"
    elif (p == 2):
        piso = "Piso3"
    elif (p == 3):
        piso = "Piso4"
    elif (p == 4):
        piso = "Piso5"
    elif (p == 5):
        piso = "Piso6"
    n = 0
    while (n < len(parqueadero[piso])):
        r = 0
        while (r < len(parqueadero[piso][n])):
            disponible1 = []
            disponible2 = []
            disponible3 = []
            disponible4 = []
            if (parqueadero[piso][n][r] == 1):
                disponible1.append(p)
                disponible1.append(n)
                disponible1.append(r)
                disponibles1.append(disponible1)
            elif (parqueadero[piso][n][r] == 2):
                disponible2.append(p)
                disponible2.append(n)
                disponible2.append(r)
                disponibles2.append(disponible2)
            elif (parqueadero[piso][n][r] == 3):
                disponible3.append(p)
                disponible3.append(n)
                disponible3.append(r)
                disponibles3.append(disponible3)
            elif (parqueadero[piso][n][r] == 4):
                disponible4.append(p)
                disponible4.append(n)
                disponible4.append(r)
                disponibles4.append(disponible4)
            r += 1
        n += 1
    p += 1
disponiblesTotal = [] # Se crea una lista que contenga todas las listas anteriores
# disponiblesTotal es una matriz en la cual se guardan listas que contienen el piso, fila y columna (en su respectivo orden) de las posiciones que se encuentran libres para parquear 
# Las posiciones libres se separan dependiendo de los tipos de vehículo 
disponiblesTotal.append(disponibles1) 
disponiblesTotal.append(disponibles2)
disponiblesTotal.append(disponibles3)
disponiblesTotal.append(disponibles4)

puestos = [] # Se crea una lista la cual indicara cuales puestos estan disponibles
# Se crean las variables que posteriormente nos ayudaran con las estadisticas deseadas
registrado = 2
vehiculosTipo1 = 0
vehiculosTipo2 = 0
vehiculosTipo3 = 0
vehiculosTipo4 = 0
vehiculosEstudiantes = 0
vehiculosProfesores = 0
vehiculosPAdministrativo = 0
vehiculosVisitantes = 0
vehiculosPiso1 = 0
vehiculosPiso2 = 0
vehiculosPiso3 = 0
vehiculosPiso4 = 0
vehiculosPiso5 = 0
vehiculosPiso6 = 0
continuar = 0
# Menú principal de la aplicacion
print("----------BUEN DÍA, BIENVENID@ A LA PONTIFICIA UNIVERSIDAD JAVERIANA DE CALI----------\n")
print("MENÚ DE OPCIONES:\n")
print("     [1] corresponde a REGISTRO.")
print("     [2] corresponde a INGRESO.")
print("     [3] corresponde a SALIDA.")
print("     [4] corresponde a GENERAR ESTADÍSTICAS.")
print("     [5] corresponde a CIERRE DE PARQUEADERO.")
continuar = eval(input("\nIngrese el número que corresponde a la acción que desea realizar: "))# variable que define la opción que realizara el usuario

while continuar < 5: # Se crea el ciclo principal del programa
    if continuar == 1: # Se crea el condicional correspondiente al registro del usuario 
        nombre = input("Ingrese sus nombres y apellidos: ")
        identificacion = eval(input("Ingrese su número de identificación: "))
        print("Para el tipo de usuario tenga en cuenta que:\n") # se imprime unas caracteristicas a tener en cuenta
        print("     [1] corresponde a ESTUDIANTE.")
        print("     [2] corresponde a PROFESOR.")
        print("     [3] corresponde a PERSONAL ADMINISTRATIVO.\n")
        n = 0
        while (n < len(usuarios["usuarios"])): # se valida si el usuario ya se encuentra registrado 
            if (identificacion == usuarios["usuarios"][n][1]):
                registrado = 1
                puesto = n
            n += 1
        if (registrado == 1): # si el usuario ya esta registrado se recorre este condicional
            print("Usted ya se encuentra registrado con el vehículo de placa " + usuarios["usuarios"][puesto][3] + ".")
        elif (registrado == 2): # si el usuario no esta registrado, se procede a finalizar el registro
            tipoUsuario = eval(input("Ingrese el número que corresponde al tipo de usuario que usted es: "))
            if (tipoUsuario == 1):
                tipoUsuario = "Estudiante"
            elif (tipoUsuario == 2):
                tipoUsuario = "Profesor"
            elif (tipoUsuario == 3):
                tipoUsuario = "Personal Administrativo"
            placa = input("Ingrese la placa de su vehículo: ")
            print("Para el tipo de vehículo tenga en cuenta que:\n")
            print("     [1] corresponde a AUTOMÓVIL.")
            print("     [2] corresponde a AUTOMÓVIL ELÉCTRICO.")
            print("     [3] corresponde a MOTOCICLETA.")
            print("     [4] corresponde a DISCAPACITADO.\n")
            # se pide los datos finales 
            tipoVehiculo = eval(input("Ingrese el número que corresponde al tipo de vehículo que será ubicado en el parqueadero: "))
            if (tipoVehiculo == 1):
                tipoVehiculo = "Automóvil"
            elif (tipoVehiculo == 2):
                tipoVehiculo = "Automóvil Eléctrico"
            elif (tipoVehiculo == 3):
                tipoVehiculo = "Motocicleta"
            elif (tipoVehiculo == 4):
                tipoVehiculo = "Discapacitado"
            print("Para el plan de pago tenga en cuenta que:\n")
            print("     [1] corresponde a MENSUALIDAD.")
            print("     [2] corresponde a DIARIO.\n")
            planPago = eval(input("Ingrese el número que corresponde al plan de pago que usará: "))
            if (planPago == 1):
                planPago = "Mensualidad"
            elif (planPago == 2):
                planPago = "Diario"
            usuarioNuevo = [nombre, identificacion, tipoUsuario, placa, tipoVehiculo, planPago]
            usuarios["usuarios"].append(usuarioNuevo)
            with open("usuarios.json", "w", encoding = "utf-8") as file: # Se abre el archivo json de usuarios en manera de escritura para editarlo y agregar un usuario nuevo
                json.dump(usuarios, file, indent = 4, ensure_ascii = False)
                file.close
            print("Usted fue registrado exitosamente.")
                
    elif(continuar == 2): # se crea el condicional correspondiente al ingreso
        placa = input("\nIngrese la placa del vehículo que desea ingresar: ")
        if (existePlaca(placa, usuarios["usuarios"]) == True): # se valida si la placa esta registrada 
            n = 0
            while (n < len(usuarios["usuarios"])): # se recorre el archivo usuarios para obtener informacion del usuario
                if placa == usuarios["usuarios"][n][3]:
                    dueño = usuarios["usuarios"][n]
                n += 1
            print("La placa " + placa + " se encuentra registrada en nuestro sistema a nombre de " + dueño[0] + ".")
            tipoUsuario = dueño[2] # se guarda si el usuario es estudiante, profesor, personal administrativo
            planPago = dueño[5] # Se define si el pago del usuario es mensual o diario
            # se define el tipo de vehiculo del usuario
            if (dueño[4] == "Automóvil"):
                tipoVehiculo = 1
            elif (dueño[4] == "Automóvil Eléctrico"):
                tipoVehiculo = 2
            elif (dueño[4] == "Motocicleta"):
                tipoVehiculo = 3
            elif (dueño[4] == "Discapacitado"):
                tipoVehiculo = 4
        elif (existePlaca(placa, usuarios["usuarios"]) == False): # si el usuario no esta registrado se valida como visitante y se le piden los datos obligatorios para el ingreso
            print("La placa " + placa + " no se encuentra registrada.")
            print("Por lo tanto, usted deberá ingresar como VISITANTE y tendrá un plan de pago DIARIO.")
            tipoUsuario = "Visitante"
            planPago = "Diario"
            print("Para el tipo de vehículo tenga en cuenta que:\n")
            print("     [1] corresponde a AUTOMÓVIL.")
            print("     [2] corresponde a AUTOMÓVIL ELÉCTRICO.")
            print("     [3] corresponde a MOTOCICLETA.")
            print("     [4] corresponde a DISCAPACITADO.\n")
            tipoVehiculo = eval(input("Ingrese el número que corresponde al tipo de vehículo que será ubicado en el parqueadero: "))
        # se crean las variables correspondiente a la cantidad de espacios disponibles de cada piso
        cantidad_disponiblesPiso1 = 0
        cantidad_disponiblesPiso2 = 0
        cantidad_disponiblesPiso3 = 0
        cantidad_disponiblesPiso4 = 0
        cantidad_disponiblesPiso5 = 0
        cantidad_disponiblesPiso6 = 0
        x = 0
        # Se recorre el tipo de vehiculo por cada piso y se agrega la cantidad a su variable correspondiente
        while x < len(disponiblesTotal[tipoVehiculo - 1]):
            if disponiblesTotal[tipoVehiculo - 1][x][0] == 0:
                cantidad_disponiblesPiso1 += 1
            elif disponiblesTotal[tipoVehiculo - 1][x][0] == 1:
                cantidad_disponiblesPiso2 += 1
            elif disponiblesTotal[tipoVehiculo - 1][x][0] == 2:
                cantidad_disponiblesPiso3 += 1
            elif disponiblesTotal[tipoVehiculo - 1][x][0] == 3:
                cantidad_disponiblesPiso4 += 1
            elif disponiblesTotal[tipoVehiculo - 1][x][0] == 4:
                cantidad_disponiblesPiso5 += 1
            elif disponiblesTotal[tipoVehiculo - 1][x][0] == 5:
                cantidad_disponiblesPiso6 += 1
            x += 1
        if tipoVehiculo == 2 or tipoVehiculo == 4:
            x = 0
            while x < len(disponiblesTotal[0]):
                if disponiblesTotal[0][x][0] == 0:
                    cantidad_disponiblesPiso1 += 1
                elif disponiblesTotal[0][x][0] == 1:
                    cantidad_disponiblesPiso2 += 1
                elif disponiblesTotal[0][x][0] == 2:
                    cantidad_disponiblesPiso3 += 1
                elif disponiblesTotal[0][x][0] == 3:
                    cantidad_disponiblesPiso4 += 1
                elif disponiblesTotal[0][x][0] == 4:
                    cantidad_disponiblesPiso5 += 1
                elif disponiblesTotal[0][x][0] == 5:
                    cantidad_disponiblesPiso6 += 1
                x += 1
        # Se imprime los datos obtenidos de las variables correspondientes a cada piso
        print("La cantidad de puestos disponibles para su tipo vehículo es: ")
        print("     En el PISO 1: " + str(cantidad_disponiblesPiso1))
        print("     En el PISO 2: " + str(cantidad_disponiblesPiso2))
        print("     En el PISO 3: " + str(cantidad_disponiblesPiso3))
        print("     En el PISO 4: " + str(cantidad_disponiblesPiso4))
        print("     En el PISO 5: " + str(cantidad_disponiblesPiso5))
        print("     En el PISO 6: " + str(cantidad_disponiblesPiso6))
        # Se pide al usuario en que piso desea parquear
        pisoDeseado = eval(input("Ingrese el PISO, en la cual usted desea parquear su vehículo: "))
        # Se valida el piso escogido por el usuario en los siguientes condicionales
        if (tipoVehiculo == 1):
            tipo = 0
            print("Para el tipo de vehículo AUTOMÓVIL, se encuentran disponibles las posiciones: ")
        elif (tipoVehiculo == 2):
            tipo = 1
            print("Para el tipo de vehículo AUTOMÓVIL ELÉCTRICO, se encuentran disponibles las posiciones: ")
        elif (tipoVehiculo == 3):
            tipo = 2
            print("Para el tipo de vehículo MOTOCICLETA, se encuentran disponibles las posiciones: ")
        elif (tipoVehiculo == 4):
            tipo = 3
            print("Para el tipo de vehículo DISCAPACITADO, se encuentran disponibles las posiciones: ")
        print("     En el PISO " + str(pisoDeseado) + ":")
        # Se otorga el piso correspondiente a pisoDeseado en la variable piso
        if (pisoDeseado == 1):
            piso = "Piso1"
        elif (pisoDeseado == 2):
            piso = "Piso2"
        elif (pisoDeseado == 3):
            piso = "Piso3"
        elif (pisoDeseado == 4):
            piso = "Piso4"
        elif (pisoDeseado == 5):
            piso = "Piso5"
        elif (pisoDeseado == 6):
            piso = "Piso6"
        x = 0
        # Se recorre la lista(disponiblesTotal) y se indica los lugares disponible donde el usuario podrá parquear
        while x < len(disponiblesTotal[tipo]):
            if disponiblesTotal[tipo][x][0] + 1 == pisoDeseado: # Se evalúan todas las posiciones libres según el piso en el cual se desea parquear
                filaDisponible = disponiblesTotal[tipo][x][1] # Se guarda la coordenada de la fila disponible
                columnaDisponible = disponiblesTotal[tipo][x][2] # Se guarda la columna de la fila disponible
                del parqueaderoDisponible[piso][filaDisponible][columnaDisponible] # se elimina las "X" en las que el usuario si puede parquear
                parqueaderoDisponible[piso][filaDisponible].insert(columnaDisponible, "O") # Son reemplazadas por una "O", que significa que podran parquear en esa posición
                if tipo == 1 or tipo == 3: # En caso de ser el tipo de vehículo "Automóvil Eléctrico" o "Discapacitado", se evalúa las posiciones disponibles en las que puede parquear del tipo de vehículo "Automóvil"
                    if disponiblesTotal[0][x][0] + 1 == pisoDeseado:
                        filaDisponible = disponiblesTotal[0][x][1]
                        columnaDisponible = disponiblesTotal[0][x][2]
                        del parqueaderoDisponible[piso][filaDisponible][columnaDisponible]
                        parqueaderoDisponible[piso][filaDisponible].insert(columnaDisponible, "O")
            x += 1
        n = 0
        # Se recorren los espacios disponibles segun el piso escogido por el usuario
        while n < len(parqueaderoDisponible[piso]):
            print("         " + str(parqueaderoDisponible[piso][n]))
            n += 1
        preguntar = True
        # Se le pregunta al usuario en que puesto quiere parquear
        while preguntar == True:
            filaDeseada = eval(input("\nIngrese la FILA, en la cual desea parquear del PISO " + str(pisoDeseado) + ": "))
            puestoDeseado = eval(input("Ingrese el puesto de la FILA " + str(filaDeseada) + ", en el cual desea parquear: "))
            puestoTipo = 3
            n = 0
            # Se evalúa si la posición en la cual desea el usuario parquear, está vacía y si es adecuada para su tipo de vehículo
            while n < len(disponiblesTotal[tipo]):
                if disponiblesTotal[tipo][n][0] == pisoDeseado - 1 and disponiblesTotal[tipo][n][1] == filaDeseada - 1 and disponiblesTotal[tipo][n][2] == puestoDeseado - 1:
                    puestoTipo = 1
                n += 1
            n = 0
            while n < len(disponiblesTotal[0]):
                if disponiblesTotal[0][n][0] == pisoDeseado - 1 and disponiblesTotal[0][n][1] == filaDeseada - 1 and disponiblesTotal[0][n][2] == puestoDeseado - 1:
                    puestoTipo = 2
                n += 1
            # Si el vehículo fue parqueado en un puesto perteneciente a su mismo tipo de vehículo se toma el camino del primer if, en caso de ser parqueadp en un puesto perteneciente al tipo de vehículo "Automóvil" (en caso de ser "Automóvil Elétrico" o "Discapacitado"). Si el espacio elegido no está disponible, se le pide al usuario que escoja otra posición
            if puestoTipo == 1:
                disponiblesTotal[tipo].remove([pisoDeseado - 1, filaDeseada - 1, puestoDeseado -1])
                preguntar = False  
            elif puestoTipo == 2:
                disponiblesTotal[0].remove([pisoDeseado - 1, filaDeseada - 1, puestoDeseado -1])
                preguntar = False
            else:
                print("\nEste puesto no se encuentra disponible, por favor ingrese uno diferente.")
        # Se imprime en la posición en la cual se parqueara el vehículo
        print("\nEl PUESTO " + str(puestoDeseado) + ", de la FILA " + str(filaDeseada) + ", del PISO " + str(pisoDeseado) + ", será ocupado por usted.")
        puesto = [placa, pisoDeseado - 1, filaDeseada - 1, puestoDeseado - 1, tipo, tipoUsuario, planPago, puestoTipo] # Se agregan todos los datos del vehículo a una lista 
        puestos.append(puesto) # Se agrega esta lista a una matriz que almacena todos los vehículos parqueados
        parqueaderoDisponible = reiniciarParqueaderoDisponible() # Se reinicia el diccionario parqueadero disponible para realizar todo este proceso de nuevo con un próximo vehículo
        # Se agrega uno según el tipo de vehículo para las estadísticas 
        if tipoVehiculo == 1: 
            vehiculosTipo1  += 1
        elif tipoVehiculo == 2:
            vehiculosTipo2 += 1
        elif tipoVehiculo == 3:
            vehiculosTipo3 += 1
        elif tipoVehiculo == 4:
            vehiculosTipo4 += 1
        # Se agrega uno según el tipo de usuario para las estadísticas
        if tipoUsuario == "Estudiante":
            vehiculosEstudiantes += 1
        elif tipoUsuario == "Profesor":
            vehiculosProfesores += 1
        elif tipoUsuario == "Personal Administrativo":
            vehiculosPAdministrativo += 1
        elif tipoUsuario == "Visitante":
            vehiculosVisitantes += 1
        if pisoDeseado == 1:
            vehiculosPiso1 += 1
        elif pisoDeseado == 2:
            vehiculosPiso2 += 1
        elif pisoDeseado == 3:
            vehiculosPiso3 += 1
        elif pisoDeseado == 4:
            vehiculosPiso4 += 1
        elif pisoDeseado == 5:
            vehiculosPiso5 += 1
        elif pisoDeseado == 6:
            vehiculosPiso6 += 1
    # Se pide la placa del vehículo para luego hacer su respectivo cobro 
    elif continuar == 3:
        parqueado = False
        while parqueado == False:
            placa = input("\nIngrese la placa del vehículo que será retirado del parqueadero: ")
            n = 0
            while n < len(puestos):
                if puestos[n][0] == placa:
                    parqueado = True
                    lugar = n
                n += 1
            if parqueado == False:
                print("\nEl vehículo de placa " + placa + ", NO se encuentra registrado dentro del parqueadero. Por favor, intente de nuevo.")
        # se pide las horas que ha estado el vehículo en el parqueadero
        horas = eval(input("Ingrese la cantidad de horas que permaneció el vehículo de placa " + placa + " estacionado en el parqueadero (Recuerde incluir el decimal que representa los minutos): "))
        # Se valida el piso en el cual estaba el vehículo
        piso = puestos[lugar][1]
        # Se valida la fila en el cual estaba el vehículo
        fila = puestos[lugar][2]
        # Se valida el puesto en el cual estaba el vehículo
        puesto = puestos[lugar][3]
        # Se valida el tipo de vehículo del usuario
        tipoVehiculo = puestos[lugar][4]
        # Se valida el tipo de usuario 
        tipoUsuario = puestos[lugar][5]
        # Se valida el plan de pago del usuario
        planPago = puestos[lugar][6]
        # Se utiliza para saber a las posiciones de qué tipo de vehículo se debe agregar el nuevo espacio libre
        puestoTipo = puestos[lugar][7]
        if puestoTipo == 1:
            disponiblesTotal[tipoVehiculo].append([piso, fila, puesto])
        elif puestoTipo == 2:
            disponiblesTotal[0].append([piso, fila, puesto])
        # Se crea la variable correspondiente al cobro que se le hará al usuario
        tiempoCobrar = horas 
        # Se valida el tipo de usuario para que el sistema haga la cuenta basado en eso
        if horas - (horas // 1) != 0:
            tiempoCobrar = (horas // 1) + 1
        if planPago == "Diario":
            if tipoUsuario == "Estudiante":
                cobro = 1000 * tiempoCobrar
            elif tipoUsuario == "Profesor":
                cobro = 2000 * tiempoCobrar
            elif tipoUsuario == "Personal Administrativo":
                cobro = 1500 * tiempoCobrar
            elif tipoUsuario == "Visitante":
                cobro = 3000 * tiempoCobrar
            print("El valor a pagar por el tiempo de parqueo de su vehículo, es de " + str(cobro) + " COP.")
        # Si el plan de pago del usuario es mensual, no se le debe cobrar nada
        else:
            print("Usted posee un plan de pago mensual, por lo tanto, no debe realizar pago alguno para salir.")
        # se elimina el puesto correspondiente al vehículo que ha salido
        puestos.remove([placa, piso, fila, puesto, tipoVehiculo, tipoUsuario, planPago, puestoTipo])
        # Se resta el tipo de vehículo que ha salido a la variable correspondiente
        if tipoVehiculo == 0:
            vehiculosTipo1  -= 1
        elif tipoVehiculo == 1:
            vehiculosTipo2 -= 1
        elif tipoVehiculo == 2:
            vehiculosTipo3 -= 1
        elif tipoVehiculo == 3:
            vehiculosTipo4 -= 1
        if tipoUsuario == "Estudiante":
            vehiculosEstudiantes -= 1
        elif tipoUsuario == "Profesor":
            vehiculosProfesores -= 1
        elif tipoUsuario == "Personal Administrativo":
            vehiculosPAdministrativo -= 1
        elif tipoUsuario == "Visitante":
            vehiculosVisitantes -= 1
        if pisoDeseado == 1:
            vehiculosPiso1 -= 1
        elif pisoDeseado == 2:
            vehiculosPiso2 -= 1
        elif pisoDeseado == 3:
            vehiculosPiso3 -= 1
        elif pisoDeseado == 4:
            vehiculosPiso4 -= 1
        elif pisoDeseado == 5:
            vehiculosPiso5 -= 1
        elif pisoDeseado == 6:
            vehiculosPiso6 -= 1
    # Se crea el archivo .txt correspondiente a los vehículos parqueados según el tipo de usuario
    elif continuar == 4:
        reporteUsuario = open("reporteUsuario.txt", "w") 
        reporteUsuario.writelines("CANTIDAD DE VEHÍCULOS PARQUEADOS SEGÚN TIPO DE USUARIO.\n\n")
        reporteUsuario.writelines("La cantidad de vehículos parqueados según el tipo de usuario ESTUDIANTE es: ")
        reporteUsuario.writelines(str(vehiculosEstudiantes))
        reporteUsuario.writelines("\n")
        reporteUsuario.writelines("La cantidad de vehículos parqueados según el tipo de usuario PROFESOR es: ")
        reporteUsuario.writelines(str(vehiculosProfesores))
        reporteUsuario.writelines("\n")
        reporteUsuario.writelines("La cantidad de vehículos parqueados según el tipo de usuario PERSONAL ADMINISTRATIVO es: ")
        reporteUsuario.writelines(str(vehiculosPAdministrativo))
        reporteUsuario.writelines("\n")
        reporteUsuario.writelines("La cantidad de vehículos parqueados según el tipo de usuario VISITANTE es: ")
        reporteUsuario.writelines(str(vehiculosVisitantes))
        reporteUsuario.close
    # Se crea el archivo .txt correspondiente a los vehículos parqueados según el tipo de vehículos
        reporteVehiculo = open("reporteVehiculo.txt", "w") 
        reporteVehiculo.writelines("CANTIDAD DE VEHÍCULOS PARQUEADOS SEGÚN TIPO DE VEHÍCULO.\n\n")
        reporteVehiculo.writelines("La cantidad de vehículos parqueados según el tipo de vehículo AUTOMÓVIL es: ")
        reporteVehiculo.writelines(str(vehiculosTipo1))
        reporteVehiculo.writelines("\n")
        reporteVehiculo.writelines("La cantidad de vehículos parqueados según el tipo de vehículo AUTOMÓVIL ELÉCTRICO es: ")
        reporteVehiculo.writelines(str(vehiculosTipo2))
        reporteVehiculo.writelines("\n")
        reporteVehiculo.writelines("La cantidad de vehículos parqueados según el tipo de vehículo MOTOCICLETA es: ")
        reporteVehiculo.writelines(str(vehiculosTipo3))
        reporteVehiculo.writelines("\n")
        reporteVehiculo.writelines("La cantidad de vehículos parqueados según el tipo de vehículo DISCAPACITADO es: ")
        reporteVehiculo.writelines(str(vehiculosTipo4))
        reporteVehiculo.close
    # Se crea el archivo .txt correspondiente a los porcentajes de los vehículos ingresados según el piso y tambien el porcentaje total sumando la cantidad de vehículos que ingresaron a cada piso
        vehiculosGlobal = vehiculosPiso1 + vehiculosPiso2 + vehiculosPiso3 + vehiculosPiso4 + vehiculosPiso5 + vehiculosPiso6
        porcentajeGlobal = (vehiculosGlobal / 550) * 100
        porcentajePiso1 = (vehiculosPiso1 / 100) * 100
        porcentajePiso2 = (vehiculosPiso2 / 100) * 100
        porcentajePiso3 = (vehiculosPiso3 / 100) * 100
        porcentajePiso4 = (vehiculosPiso4 / 100) * 100
        porcentajePiso5 = (vehiculosPiso5 / 100) * 100
        porcentajePiso6 = (vehiculosPiso6 / 50) * 100
        reporteOcupacion = open("reporteOcupacion.txt", "w") 
        reporteOcupacion.writelines("PORCENTAJE DE OCUPACIÓN DEL PARQUEADERO.\n\n")
        reporteOcupacion.writelines("El porcentaje de ocupación GLOGAL es: ")
        reporteOcupacion.writelines(str(porcentajeGlobal))
        reporteOcupacion.writelines("%")
        reporteOcupacion.writelines("\n")
        reporteOcupacion.writelines("El porcentaje de ocupación del PISO 1 es: ")
        reporteOcupacion.writelines(str(porcentajePiso1))
        reporteOcupacion.writelines("%")
        reporteOcupacion.writelines("\n")
        reporteOcupacion.writelines("El porcentaje de ocupación del PISO 2 es: ")
        reporteOcupacion.writelines(str(porcentajePiso2))
        reporteOcupacion.writelines("%")
        reporteOcupacion.writelines("\n")
        reporteOcupacion.writelines("El porcentaje de ocupación del PISO 3 es: ")
        reporteOcupacion.writelines(str(porcentajePiso3))
        reporteOcupacion.writelines("%")
        reporteOcupacion.writelines("\n")
        reporteOcupacion.writelines("El porcentaje de ocupación del PISO 4 es: ")
        reporteOcupacion.writelines(str(porcentajePiso4))
        reporteOcupacion.writelines("%")
        reporteOcupacion.writelines("\n")
        reporteOcupacion.writelines("El porcentaje de ocupación del PISO 5 es: ")
        reporteOcupacion.writelines(str(porcentajePiso5))
        reporteOcupacion.writelines("%")
        reporteOcupacion.writelines("\n")
        reporteOcupacion.writelines("El porcentaje de ocupación del PISO 6 es: ")
        reporteOcupacion.writelines(str(porcentajePiso6))
        reporteOcupacion.writelines("%")
        reporteOcupacion.writelines("\n")
        reporteOcupacion.close
        print("\nLos reportes serán guardados en archivos con extensión '.txt' cuando se cierre el programa.")
        print("IMPORTANTE: El programa generará el último reporte solicitado, al cerrar el programa mediante la opción [5].")
    # Se imprime nuevamente el menú principal del programa
    print("\nMENÚ DE OPCIONES:\n")
    print("     [1] corresponde a REGISTRO.")
    print("     [2] corresponde a INGRESO.")
    print("     [3] corresponde a SALIDA.")
    print("     [4] corresponde a GENERAR ESTADÍSTICAS.")
    print("     [5] corresponde a CIERRE DE PARQUEADERO.")
    # El programa solamente podrá ser cerrado si el parqueadero se encuentra vacío, puesto que si el programa es cerrado al empezarlo de nuevo, no quedarán registrados los vehículos que quedaron estacionados con anterioridad
    finalizar = False
    while finalizar == False:
        continuar = eval(input("\nIngrese el número que corresponde a la acción que desea realizar: "))
        if puestos == [] and continuar == 5:
            finalizar = True
        elif puestos != [] and continuar == 5:
            print("\nAún quedan vehículos dentro del parqueadero, por lo tanto, no se puede realizar el cierre del parqueadero.")
        elif continuar != 5:
            finalizar = True
            
print("\nHasta luego.")



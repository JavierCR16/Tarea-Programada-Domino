##****************************************************************##
##              Instituto Tecnológico de Costa Rica               ##
##                                                                ##
##  Tarea Programada # 4                                          ##
##                                                                ##
##  Autores : Sebastián Salas García      (2015183511)            ##
##            Javier Contreras Muñoz      (2016093730)            ##
##            Melissa Villalobos Madrigal (2016082553)            ##
##            Fabricio Alvarado Esquivel  (2016089643)            ##
##                                                                ##
##  Fecha   : 21 de Noviembre del 2017                            ##
##                                                                ##
##  El programa es un juego de domino que analiza el patrón de    ##
##  pips en una cuadricula de 7x8                                 ##
##                                                                ##
##  Entradas:                                                     ##
##        Archivos de texto con los casos                         ##
##  Salidas:                                                      ##
##        Se muestra el caso con el problema y le sigue           ##
##  Restricciones:                                                ##
##        No hay restricciones.                                   ##
##                                                                ##
##****************************************************************##

class Archivos:
    """ Permite leer un archivo con los problemas.
    """
    # Variables de clase.
    entero                 = 0
    número                 = 1

    def __init__(self, nombreArchivo):
        """ Crea una instancia asociada al archivo.
            Si el archivo existe lo abre y el atributo
            eof es True, en caso contrario el atributo
            eof es False.
        """
        try:
            self.archivo = open(nombreArchivo, "rt")
        except:
            self.eof = True # Si el archivo esta vacío o no existe retorna True.
        else:
            self.eof = False # Si el archivo existe retorna False ya que no es el final del mismo.


    @staticmethod
    def extraiga(tipo, linea):
        """ Verifica que el tipo indicado venga al inicio de la línea.
            Omite todos los espacios en blanco.
            Retorna una tupla con el valor esperado y el resto de la línea.
            Si el valor esperado no viene al inicio de la línea retorna
            (None, linea).
        """
        i = 0
        while i < len(linea) and linea[i] == " ":
            i += 1  # Salta los espacios en blanco

        if tipo in (Archivos.entero, Archivos.número):
            # Procesa la parte entera.
            j = i
            while j < len(linea) and linea[j] in "0123456789":
                j += 1

            if i == j: # No encontró un número
                return None, linea

            if tipo == Archivos.entero:
                # Retorna un entero
                return int(linea[i:j]), linea[j:]

        

    @staticmethod
    def salte(tira, linea):
        """ Sin considerar los espacios en blanco, retorna el resto
            de línea a partir del punto en que aparece tira.
            Si tira no aparece al inicio de línea, retorna la línea
            original.
        """
        # Omite blancos
        i = 0
        while i < len(linea) and linea[i] == " ":
            i += 1

        # Compara si tira ocurre al inicio de linea
        j = 0
        while i < len(linea) and j < len(tira) and linea[i] == tira[j]:
            i += 1
            j += 1

        if j == len(tira):
            # Se encontró una ocurrencia de tira al inicio de línea
            return linea[i:]

        # No se encontró una ocurrencia de tira al inicio de linea.
        return linea

    def leaLinea(self):
        """Retorna una tupla con la información de la siguiente línea
            del archivo como una tupla de la forma:
            (num1, num2, num3, num4, num5, num6, num7, num8)
            En caso de que el archivo no contenga una línea con el formato
            adecuado retorna None.
        """
        if not self.eof: # Si el archivo no ha llegado a su final ejecuta lo siguiente.
            linea = self.archivo.readline() # Guarda la linea de archivo con el método .readline().
            # Analisa la linea segun lo que tenga.
            if not linea:
                self.eof = True
                return None
            else:
                # Si la estructura es correcta retorna una tupla con la inf. de la linea.
                num1, linea = Archivos.extraiga(Archivos.entero, linea) # Obtiene primer num.
                linea = Archivos.salte(" ", linea) # Se salta el espacio de la linea
                num2, linea = Archivos.extraiga(Archivos.entero, linea) # Obtiene segundo num.
                linea = Archivos.salte(" ", linea) # Se salta el espacio de la linea
                num3, linea = Archivos.extraiga(Archivos.entero, linea) # Obtiene tercer num.
                linea = Archivos.salte(" ", linea) # Se salta el espacio de la linea
                num4, linea = Archivos.extraiga(Archivos.entero, linea) # Obtiene cuarto num.
                linea = Archivos.salte(" ", linea) # Se salta el espacio de la linea
                num5, linea = Archivos.extraiga(Archivos.entero, linea) # Obtiene quinto num.
                linea = Archivos.salte(" ", linea) # Se salta el espacio de la linea
                num6, linea = Archivos.extraiga(Archivos.entero, linea) # Obtiene sexto num.
                linea = Archivos.salte(" ", linea) # Se salta el espacio de la linea
                num7, linea = Archivos.extraiga(Archivos.entero, linea) # Obtiene setimo num.
                linea = Archivos.salte(" ", linea) # Se salta el espacio de la linea
                num8, linea = Archivos.extraiga(Archivos.entero, linea) # Obtiene octavo num.
                linea = Archivos.salte(" ", linea) # Se salta el espacio de la linea
                # Retorna tupla con la informacion de la linea de ser correcta su estructura.
                tupla = [num1,num2,num3,num4,num5,num6,num7,num8]
                if all([x != None for x in tupla]):
                        return tupla
                else:
                    return None
        else: # El archivo llego al final.
            return None

class Fichas():

    def __init__(self):
        """
            Diccionario con las fichas posibles del juego
        """
        self.fichas = {1:(0,0),2:(0,1),3:(0,2),4:(0,3),5:(0,4),6:(0,5),7:(0,6),8:(1,1),9:(1,2),10:(1,3),
                      11:(1,4),12:(1,5),13:(1,6),14:(2,2),15:(2,3),16:(2,4),17:(2,5),18:(2,6),19:(3,3),
                      20:(3,4),21:(3,5),22:(3,6),23:(4,4),24:(4,5),25:(4,6),26:(5,5),27:(5,6),28:(6,6)}
        self.fichaDisponible = []
        for x in range(28):
             self.fichaDisponible.append(False)

    def reverse(self,ficha):
        """
            Girar la pieza
        """
        self.fichas[ficha] = (self.fichas[ficha][1],self.fichas[ficha][0])
        print(self.fichas[ficha])
        

class BaseDatosCasos(Archivos):
    
    def __init__(self, archivo):
        """ Crea una BD a partir de un archivo de texto.
            Las líneas del archivo de texto tienen alguna de las
            siguientes estructuras:
            (num1, num2, num3, num4, num5, num6, num7, num8)
        """
        self.casos = {} # Diccionario que funciona como base de datos para todos los geo-referencias.
        # Se abre el archivo para guarda la informacion en la base de datos.
        self.Archivo = archivo
        f = Archivos(archivo)
        r = f.leaLinea()        
        self.lista = []
        self.lista.append(r)
        while not f.eof: # Hasta que la linea vacío guarda información.
            # Valida que la linea este bien y que no sea repetida la información.
            if r != None and r[0] not in self.casos:
                self.casos[r[0]] = (r[1], r[2])
            
            r = f.leaLinea()
            if (r != None):
                self.lista.append(r)

def producirMapas():
    pass
    
                
def particionCasos(BaseDatosCasos):
    """
    """
    listaNumeros = BaseDatosCasos.lista
    listaCasos = []
    listaAux = []
    acum = 0
    while (listaNumeros != []):
        for linea in listaNumeros:
            if acum == 7:
                acum = 0
                listaCasos.append(listaAux)
                listaAux = []            
            listaAux.append(linea)
            acum = acum + 1
        for x in range(0,7):
            listaNumeros.pop(0)
    return listaCasos

def printearMatriz(matriz):
    """
        Método queimprime la matriz tabulada.
    """
    s = ""
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            s = s + str(matriz[x][y])+"  "
        print(s)
        s = ""
        
def inicio():
    """
        Función main del programa donde se ejecutan las instrucciones.
    """
    # Base de datos
    cantsoluciones = 0
    BDCasos = BaseDatosCasos("casoPrueba1.txt")
    listaCasos = particionCasos(BDCasos)
    ficha = Fichas()
    for x in range(len(listaCasos)):
        print(" Conjunto #%d"% (x+1)+":")
        printearMatriz(listaCasos[x])
        print("\n")
        print(" Mapas Resultantes del Conjunto #%d"% (x+1)+":")
        cantsoluciones = producirMapas()
        print("\n")
        print("Hay %d" % 0 + " solución(es) para el conjunto #%d" % (x+1))
        print("\n")
    
inicio()

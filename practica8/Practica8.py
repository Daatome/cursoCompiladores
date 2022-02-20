# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:49:27 2021

@author: daniel
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os



class ALEX(QtWidgets.QMainWindow):

    
        def __init__(self):
            super(ALEX, self).__init__()
            self.setGeometry(50,50,900,800)
            self.openfile= QtWidgets.QAction(QtGui.QIcon("imagenes/abrir-documento.png"),"&Abrir Archivo", self)
            self.openfile.setStatusTip("Abrir Archivo")
            self.openfile.triggered.connect(self.abrir_archivo)
    
            self.EventoSalir= QtWidgets.QAction(QtGui.QIcon("imagenes/salida.png"),"salir", self)
            self.EventoSalir.setShortcut("Ctrl+Q")
            self.EventoSalir.setStatusTip("salir de la aplicacion")
            self.EventoSalir.triggered.connect(self.cierra_aplicacion)
    
            self.menuPrincipal= self.menuBar()
            self.menuArchivo=self.menuPrincipal.addMenu("&Archivo")
            self.menuArchivo.addAction(self.openfile)
            self.menuArchivo.addSeparator()
            self.menuArchivo.addAction(self.EventoSalir)
            self.vOpenfilename="variable para archivotxt"
            self.tokensInt=0
            self.tokensFloat=0
            self.tokensBoolean=0
            self.tokensChar=0
            self.tokensString=0
            self.home()
            #uami= UAMI()
            self.nombreArchivo=""
        
        
        def home(self):
            self.bandera_abrir= False
            self.Resultados=QtWidgets.QTextEdit(self)

            eventoAbrirLocal = QtWidgets.QAction(QtGui.QIcon("imagenes/abrir-documento.png"), "Abrir un archivo",self)
            eventoAbrirLocal.triggered.connect(self.abrir_archivo)
            self.barraDeOpciones=self.addToolBar("Archivo")
            self.barraDeOpciones.addAction(eventoAbrirLocal)
            
            self.compilar= QtWidgets.QAction(QtGui.QIcon("imagenes/boton-de-play"),"Compilar" , self)
            self.compilar.triggered.connect(self.compilaArchivo)
            self.barraDeOpciones.addAction(self.compilar)
            
            
            
            self.eventoSalirLocal= QtWidgets.QAction(QtGui.QIcon("imagenes/salida.png"),"Salir",self)
            self.eventoSalirLocal.triggered.connect(self.cierra_aplicacion)
            self.barraDeOpciones.addAction(self.eventoSalirLocal)

            
            
            self.eventoGuardar= QtWidgets.QAction(QtGui.QIcon("imagenes/guardar.png"),"GuardarCambios",self)
            self.eventoGuardar.triggered.connect(self.guardaCambios)
            self.barraDeOpciones.addAction(self.eventoGuardar)
            
            

            #creacion de boton y campos de texto
            self.lblContenidoDelArchivo= QtWidgets.QLabel("Contenido del archivo Fuente: ",self)
            self.lblContenidoArchivoTupla= QtWidgets.QLabel("Resultado de la Compilacion: ",self)
            self.txtResultados=QtWidgets.QTextEdit(self)
            self.lblcontenidoArchivoError= QtWidgets.QLabel("Contenido del archivo error: ",self)
            self.lblResultados= QtWidgets.QLabel("Contenido Del archivo Tupla: ",self)
            self.txtArchivoError=QtWidgets.QTextEdit(self)
            self.txtArchivoTupla=QtWidgets.QTextEdit(self)
            
            
            self.lblContenidoDelArchivo.move(10, 60)
            self.lblContenidoDelArchivo.adjustSize()
            self.lblResultados.adjustSize()
            self.lblResultados.move(450, 350)
            
            
            #caja de texto para el resultado de compilar
            self.txtResultados.resize(400, 200)
            self.txtResultados.move(450,380)
            
            #'caja de resultados para ver el archivo que se seleccionó'
            self.Resultados.resize(400,200)
            self.Resultados.move(10,90)
            
            #Caja archivo tupla
            self.lblContenidoArchivoTupla.adjustSize()
            self.lblContenidoArchivoTupla.move(450, 60)
            self.txtArchivoTupla.resize(400, 200)
            self.txtArchivoTupla.move(450, 90)
            #caja archivo Error
            self.lblcontenidoArchivoError.adjustSize()
            self.lblcontenidoArchivoError.move(10,350)
            self.txtArchivoError.resize(400, 200)
            self.txtArchivoError.move(10,380)
            

            self.show()
            
        def abrir_archivo(self):
            uami= UAMI()
            #tiene dos self porque en uno se está mandando la ventana como parametro
            self.nombreArchivo=uami.abrir_archivo(self, self.vOpenfilename, self.Resultados,self.bandera_abrir)
        
        def cierra_aplicacion(self):
            opcion= QtWidgets.QMessageBox.question(self, "salir de la aplicacion","¿seguro?",QtWidgets.QMessageBox.question.Yes | QtWidgets,QtWidgets.QMessageBox.question.No)
            
            
            if opcion==QtWidgets.QMessageBox.question.Yes:
                sys.exit()
            else:
                pass
            
            
        def compilaArchivo(self):
            uami= UAMI()
            uami.compilaArchivo(self.txtResultados, self.Resultados.toPlainText(),self.nombreArchivo,self.txtArchivoError,self.txtArchivoTupla)
           
        def guardaCambios(self):
            f=open(self.nombreArchivo, "w")
            #Eliminamos el contenido del archivo
            f.truncate(0)
            f.write(self.Resultados.toPlainText())
            f.close()
            
            
class UAMI():
   
    contador=0
    contadorLineas=1 
    tokens=[]
    
    
    def abrir_archivo(self,window, vOpenfilename, Resultados, bandera_abrir):
        vOpenfilename= QtWidgets.QFileDialog.getOpenFileName(window,"Open File",filter="*.fte")[0]

        if vOpenfilename=="":
            return
        f=open(vOpenfilename, "r")
        vTextstring=f.read()
        Resultados.setText(vTextstring)
        f.close()
        bandera_abrir=True
        return vOpenfilename
    
    
    def compilaArchivo(self, txtResultados, texto, nombreArchivo,txtArchivoError,txtResultadoComp):
        
        
        ale= ALEX_Final()
        sintactico= Parse()
       
        textoNuevo=""
        consultaTabla= TablaSimbolos()
        sintactico.inicio(texto)
        
        #print (tokens)
        #print("lineas analizadas:" + str(UAMI.contadorLineas))
        if len(self.tokens)>=1:
            archivotpl= open(nombreArchivo+".tpl", "w")
            for x in self.tokens:
                if x!=-1:
                    
                    textoNuevo=textoNuevo +"Lexema: "+ consultaTabla.obtenerLexema(x)+" Token: "+consultaTabla.obtenerToken(x) +"\n"
                    archivotpl.write("Lexema: "+ consultaTabla.obtenerLexema(x)+" Token: "+consultaTabla.obtenerToken(x)+"\n")
                
            
            archivotpl.close()
            txtResultados.setText(textoNuevo)
            archivoErr= open(nombreArchivo+".err","w")
            textoError=""
        for x in consultaTabla.tablaDeErrores:
            archivoErr.write("Error: "+str(x[0])+"\tLinea: "+str(x[1])+"\n")
            textoError=textoError + "Error: "+str(x[0])+"\tLinea: "+str(x[1])+"\n"
        txtArchivoError.setText(textoError)
        archivoErr.close()
        if len(consultaTabla.tablaDeErrores)>0:
            txtResultadoComp.setText("Errores de compilacion \nLineas analizadas: "+str(UAMI.contadorLineas))
        else:
            txtResultadoComp.setText("Compilacion exitosa \nLineas analizadas: "+str(UAMI.contadorLineas))
            
        UAMI.contador=0
        UAMI.contadorLineas=1
        consultaTabla.vaciaErrores()
       
        
    
    
class ALEX_Final():
    
    diccionarioChar={
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"
        }
    
    def compila(self, palabra):
        tabla= TablaSimbolos()
        
        
        while UAMI.contador<len(palabra):
            
            #if por si el caracter es un número
            if palabra[UAMI.contador].isdigit() and  palabra[UAMI.contador]!='0' :
                
                lexbuf=""
                while UAMI.contador<len(palabra) and palabra[UAMI.contador].isdigit() :
                    lexbuf=lexbuf + palabra[UAMI.contador]
                    UAMI.contador+=1
                    
                #return "linea:"+str(UAMI.contadorLineas)+" lexema: "+lexbuf + " token: Entero"
                guarda=tabla.buscaSimbolo(lexbuf)
                if guarda==-1:
                    guarda=tabla.insertaSimbolo(lexbuf, "Entero")
                return guarda
            
            #si el número inicia con cero lo termina de leer y reporta el error
            elif palabra[UAMI.contador]=='0':
                lexbuf=palabra[UAMI.contador]
                UAMI.contador+=1
                while UAMI.contador<len(palabra) and palabra[UAMI.contador].isdigit() :
                    lexbuf=lexbuf + palabra[UAMI.contador]
                    UAMI.contador+=1
                if len(lexbuf)>1:
                    '''tabla.insertaError(lexbuf, "numero con inicio 0 linea: "+str(UAMI.contadorLineas))'''
                    return -1
                guarda= tabla.insertaSimbolo(lexbuf, "Entero")
                return guarda
                    
            #token de multiplicación    
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="*":
                
                UAMI.contador+=1
                #return "linea: "+str(UAMI.contadorLineas)+ " Lexema: *  Token: Producto"
                guarda=tabla.buscaSimbolo("*")
                return guarda
                
            #token de suma o incremento     
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="+":
                lexbuf="+"
                UAMI.contador+=1
                if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="+":
                    lexbuf=lexbuf +"+"
                    UAMI.contador+=1
                    #return "linea: "+ str(UAMI.contadorLineas)+" lexema: "+lexbuf +" token: Incremento"
                guarda= tabla.buscaSimbolo(lexbuf)
                return guarda
                
                    
            #Decremento 
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="-":
            
             lexbuf="-"
             UAMI.contador+=1
             if palabra[UAMI.contador]=="-":
                 lexbuf=lexbuf +"-"
                 UAMI.contador+=1
                 #return "linea: "+ str(UAMI.contadorLineas)+" lexema: "+lexbuf +" token: Decremento"
                
             guarda=tabla.buscaSimbolo(lexbuf)
             return guarda
            
                 
            if palabra[UAMI.contador]==" ":
                UAMI.contador+=1
               
                return -1
            if palabra[UAMI.contador]=="\n":
                UAMI.contadorLineas+=1
                UAMI.contador+=1
                
                return -1
            if palabra[UAMI.contador]=="\t":
                UAMI.contador+=1
                
            #reconoce palabras
            if self.diccionarioChar.__contains__(palabra[UAMI.contador]):
                lexbuf=palabra[UAMI.contador]
                UAMI.contador+=1
                while  UAMI.contador<len(palabra) and palabra[UAMI.contador]!=";" and palabra[UAMI.contador]!="=" :
                    if palabra[UAMI.contador]!=" " and  palabra[UAMI.contador]!="\n" :
                        lexbuf=lexbuf+palabra[UAMI.contador]
                        UAMI.contador+=1
                    else:
                        guarda= tabla.buscaSimbolo(lexbuf)
                        if palabra[UAMI.contador]=="\n" :
                            UAMI.contadorLineas+=1
                        UAMI.contador+=1
                        if guarda==-1:
                            guarda= tabla.insertaSimbolo(lexbuf, "Identificador")
                    
                        return guarda
                guarda= tabla.buscaSimbolo(lexbuf)
                if guarda==-1:
                    guarda= tabla.insertaSimbolo(lexbuf, "Identificador")
                
                return guarda
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="\"":
                UAMI.contador+=1#crece porque no vamos a leer las comillas
                lexbuf=""
                while UAMI.contador<len(palabra):
                    if palabra[UAMI.contador]=="\n" or palabra[UAMI.contador]=="":
                        UAMI.contador+=1
                        '''tabla.insertaError("Comillas incompletas", UAMI.contadorLineas)'''
                        UAMI.contadorLineas+=1
                        return -1 #Hay que reportar el error
                    if palabra[UAMI.contador]!="\"":
                        lexbuf=lexbuf+palabra[UAMI.contador]
                        UAMI.contador+=1
                        
                    else:#Si el caracter es una comilla que cierra
                        UAMI.contador+=1
                        guarda= tabla.insertaSimbolo(lexbuf, "String")
                        guarda= tabla.buscaSimbolo(lexbuf)
                        return guarda
                '''tabla.insertaError("Error en el String", UAMI.contadorLineas)'''
                return -1  
            
            #operadores relacionales
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="<" :
                lexbuf=palabra[UAMI.contador]
                UAMI.contador+=1
                if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="=":
                    lexbuf=lexbuf+palabra[UAMI.contador]
                    UAMI.contador+=1
                guarda= tabla.buscaSimbolo(lexbuf)
                return guarda
            
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]==">" :
                lexbuf=palabra[UAMI.contador]
                UAMI.contador+=1
                if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="=":
                    lexbuf=lexbuf+palabra[UAMI.contador]
                    UAMI.contador+=1
                guarda= tabla.buscaSimbolo(lexbuf)
                return guarda
               
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="=" :
                lexbuf=palabra[UAMI.contador]
                UAMI.contador+=1
                if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="=":
                    lexbuf=lexbuf+palabra[UAMI.contador]
                    UAMI.contador+=1
                guarda = tabla.buscaSimbolo(lexbuf)
                return guarda  
            
            #Parentesis
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="(" :
                lexbuf= palabra[UAMI.contador]
                guarda= tabla.buscaSimbolo(lexbuf)
                UAMI.contador+=1
                return guarda
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]==")" :
                lexbuf= palabra[UAMI.contador]
                guarda= tabla.buscaSimbolo(lexbuf)
                UAMI.contador+=1
                return guarda
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]==";" :
                lexbuf= palabra[UAMI.contador]
                guarda= tabla.buscaSimbolo(lexbuf)
                UAMI.contador+=1
                return guarda
            if UAMI.contador<len(palabra) and palabra[UAMI.contador]=="," :
                lexbuf= palabra[UAMI.contador]
                guarda= tabla.buscaSimbolo(lexbuf)
                UAMI.contador+=1
                return guarda
            
            
            return -1
                
        
        
        
        
class TablaSimbolos():
    
    tablaDeSimbolos=[["programa","Palabra Reservada"],["si","Palabra Reservada"],["entonces","Palabra Reservada"],["otro","Palabra Reservada"],
                     ["haz","Palabra Reservada"],["mientras","Palabra Reservada"],["comienza","Palabra Reservada"],["termina","Palabra Reservada"],
                     ["imprime","Palabra Reservada"],["repite","Palabra Reservada"],["hasta","Palabra Reservada"],["para","Palabra Reservada"],
                     ["a","Palabra Reservada"],["<","Operador Relacional"],[">","Operador Relacional"],["<=","Operador Relacional"],
                     [">=","Operador Relacional"],["+","Operador Aritmetico"],["-","Operador Aritmetico"],["=","Operador Aritmetico"],
                     ["*","Operador Aritmetico"],["/","Operador Aritmetico"],["++","Incremento"],["--","Decremento"],[";","Resto del Mundo"],
                     ["==","Operador Logico"],["||","Operador Logico"],["&&","Operador Logico"],["!=","Operador Logico"],["(","Resto del Mundo"],
                     [")","Resto del Mundo"],[";","Resto del Mundo"],[",","Resto del Mundo"]]
    
    tablaDeErrores=[]
    def buscaSimbolo(self,simbolo):
        i=0
        while i<len(self.tablaDeSimbolos):
            guarda=self.tablaDeSimbolos[i]
            if simbolo==guarda[0]:
                return i
            i+=1 
        return -1
    
    def insertaSimbolo(self,simbolo,token):
        self.tablaDeSimbolos.append([simbolo,token])
        return self.buscaSimbolo(simbolo)
    
    def obtenerLexema(self,posicion):
        guarda= self.tablaDeSimbolos[posicion]
        return guarda[0]
    
    def obtenerToken(self,posicion):
        guarda= self.tablaDeSimbolos[posicion]
        return guarda[1]
    
    def imprimirTabla(self):
        for x in self.tablaDeSimbolos:
            print("Lexema: "+x[0]+"\tToken: "+x[1])
    
    def insertaError(self,simbolo,linea):
        self.tablaDeErrores.append([simbolo,linea])
    def vaciaErrores(self):
        self.tablaDeErrores.clear()
    


                
        

class Parse():
    
    preAnalisis = [0 for x in range(2)]
    preAnalisis[0]=""
    preAnalisis[1]=""
    lexico= ALEX_Final()
    tabla= TablaSimbolos()
    textos=""
    guardauam=UAMI()
    
    
    def inicio(self, texto):
       
       pos=self.lexico.compila(texto)
       self.guardauam.tokens.append(pos)
       if pos!=-1:
           self.preAnalisis[0]= self.tabla.obtenerLexema(pos)
           self.preAnalisis[1]=self.tabla.obtenerToken(pos)
           self.textos=texto
           self.encabezado()
           self.secuencia()
           self.parea("HECHO")
    
       
    def encabezado(self):
        print("entro a encabezado")
        self.parea("programa")
        self.parea("Identificador")
        self.parea(";")
    
    def parea(self,seEspera):
        if self.preAnalisis[0]==seEspera or self.preAnalisis[1]==seEspera:
            if self.preAnalisis[0]=="HECHO":
                return True
            pos=self.lexico.compila(self.textos)
            if pos!=-1 and pos!=None:
                self.guardauam.tokens.append(pos)
                self.preAnalisis[0]=self.tabla.obtenerLexema(pos)
                self.preAnalisis[1]=self.tabla.obtenerToken(pos)
                
            else:#se hace este while ya que mi metodo para compilar regresa -1 cuando hay algo no reconocido
                while pos==-1 or pos==None:
                    pos=self.lexico.compila(self.textos)
                self.guardauam.tokens.append(pos)
                self.preAnalisis[0]=self.tabla.obtenerLexema(pos)
                self.preAnalisis[1]=self.tabla.obtenerToken(pos)
            print(self.preAnalisis)
                
            return True
            
        else:
            self.tabla.insertaError("error en  linea:"+ str(self.guardauam.contadorLineas) , "Se esperaba: "+ seEspera)
            return False
        
        
    def secuencia(self):
        
        
        self.parea("comienza")
        while self.preAnalisis[0]!="termina" :
            self.asignacion()
        
        self.parea("termina")
        
    def asignacion(self):
               
        self.parea("Identificador")
        self.parea("Operador Aritmetico")
        self.parea("Entero")
        self.parea(";")
        
            
        
        
    
    
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI=ALEX()
    
    sys.exit(app.exec_())

main()
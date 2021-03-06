# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:49:27 2021

@author: daniel
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class ALEX_01(QtWidgets.QMainWindow):

    
        def __init__(self):
            super(ALEX_01, self).__init__()
            self.setGeometry(50,50,800,600)
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
            
            

            #creacion de boton y campos de texto
            self.lblContenidoDelArchivo= QtWidgets.QLabel("Contenido del \narchivo Fuente: ",self)
            self.lblResultados= QtWidgets.QLabel("Resultado de la \ncompilacion: ",self)
            self.txtResultados=QtWidgets.QTextEdit(self)
            
            
            self.lblContenidoDelArchivo.move(10, 100)
            self.lblContenidoDelArchivo.adjustSize()
            self.lblResultados.adjustSize()
            self.lblResultados.move(10, 300)
            
            self.txtResultados.resize(500, 200)
            self.txtResultados.move(250,300)
            
            self.Resultados.resize(500,200)
            self.Resultados.move(250,65)

            

            self.show()
            
        def abrir_archivo(self):
            uami= UAMI()
            #tiene dos self porque en uno se est?? mandando la ventana como parametro
            self.nombreArchivo=uami.abrir_archivo(self, self.vOpenfilename, self.Resultados,self.bandera_abrir)
        
        def cierra_aplicacion(self):
            opcion= QtWidgets.QMessageBox.question(self, "salir de la aplicacion","??seguro?",QtWidgets.QMessageBox.question.Yes | QtWidgets,QtWidgets.QMessageBox.question.No)
            
            if opcion==QtWidgets.QMessageBox.question.Yes:
                sys.exit()
            else:
                pass
            
        def compilaArchivo(self):
            uami= UAMI()
            uami.compilaArchivo(self.txtResultados, self.Resultados.toPlainText(),self.nombreArchivo)
           
            
class UAMI():
   
    contador=0
    contadorLineas=1
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
    
    
    def compilaArchivo(self, txtResultados, texto, nombreArchivo):
        
        
        ale= ALEX()
        tokens=[]
        textoNuevo=""
        
        while UAMI.contador< len(texto):
            print (str(UAMI.contador))
            
            tokens.append(ale.compila(texto))
            
        tokens.append("Lineas analizadas: " + str(UAMI.contadorLineas))    
        if len(tokens)>1:
            archivotpl= open(nombreArchivo+".tpl", "w")
            for x in tokens:
                if x!=None:
                    textoNuevo=textoNuevo + "\n"+str(x) +"\n"
                    archivotpl.write(str(x)+"\n")
                
            
            archivotpl.close()
            txtResultados.setText(textoNuevo)
        else:
            archivoErr= open(nombreArchivo+".err","w")
            archivoErr.write(tokens[0])
            archivoErr.close()
            txtResultados.setText(tokens[0])
        UAMI.contador=0
        UAMI.contadorLineas=1
       
        
    
    
class ALEX():
    def compila(self, palabra):
        
        
        
        while UAMI.contador<len(palabra):
            
            if palabra[UAMI.contador].isdigit():
                print("digito")
                lexbuf=""
                while UAMI.contador<len(palabra) and palabra[UAMI.contador].isdigit() :
                    lexbuf=lexbuf + palabra[UAMI.contador]
                    UAMI.contador+=1
                    
                return "linea:"+str(UAMI.contadorLineas)+" lexema: "+lexbuf + " token: Entero"
            elif UAMI.contador<len(palabra) and palabra[UAMI.contador]=="*":
                print("producto  ")
                UAMI.contador+=1
                return "linea: "+str(UAMI.contadorLineas)+ " Lexema: *  Token: Producto"
                
                
            elif UAMI.contador<len(palabra) and palabra[UAMI.contador]=="+":
                print("Suma o incremento")
                lexbuf="+"
                UAMI.contador+=1
                if palabra[UAMI.contador]=="+":
                    lexbuf=lexbuf +"+"
                    UAMI.contador+=1
                    return "linea: "+ str(UAMI.contadorLineas)+" lexema: "+lexbuf +" token: Incremento"
                else:
                    return "linea: "+str(UAMI.contadorLineas)+"lexema: "+lexbuf + " token: Suma"
                    #UAMI.contador-=1
            elif palabra[UAMI.contador]==" ":
                UAMI.contador+=1
                print("Elif de espacio")
                return
            elif palabra[UAMI.contador]=="\n":
                UAMI.contadorLineas+=1
                UAMI.contador+=1
                print("Elif de salto")
                return
            else:
               
                nuevaLista=[ "Error en el archivo fuente:  " + palabra]
                UAMI.contador= len(palabra)
                return nuevaLista
        
        
        
        

                
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI=ALEX_01()
    
    sys.exit(app.exec_())

main()
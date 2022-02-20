# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:10:07 2022

@author: danie
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super(ventana, self).__init__()
        self.setGeometry(50,50,800,650)
        self.openfile= QtWidgets.QAction(QtGui.QIcon("imagenes/abrir-documento.png"),"&Abrir Archivo", self)
        self.openfile.setStatusTip("Abrir Archivo")
        self.openfile.triggered.connect(self.abrir_archivo)
        
        self.menuPrincipal= self.menuBar()
        self.menuArchivo=self.menuPrincipal.addMenu("&Archivo")
        self.menuArchivo.addAction(self.openfile)
        self.menuArchivo.addSeparator()
        
        self.vOpenfilename="variable para archivotxt"
        self.tokensInt=0
        self.tokensFloat=0
        self.tokensBoolean=0
        self.tokensChar=0
        self.tokensString=0
        self.home()
        self.nombreArchivo=""
        
        
    def home(self):
        self.bandera_abrir= False
        

        eventoAbrirLocal = QtWidgets.QAction(QtGui.QIcon("imagenes/abrir-documento.png"), "Abrir un archivo",self)
        eventoAbrirLocal.triggered.connect(self.abrir_archivo)
        self.barraDeOpciones=self.addToolBar("Archivo")
        self.barraDeOpciones.addAction(eventoAbrirLocal)
            
            
        self.eventoSalirLocal= QtWidgets.QAction(QtGui.QIcon("imagenes/salida.png"),"Salir",self)
        self.eventoSalirLocal.triggered.connect(self.cierra_aplicacion)
        self.barraDeOpciones.addAction(self.eventoSalirLocal)

            
            
        self.eventoGuardar= QtWidgets.QAction(QtGui.QIcon("imagenes/guardar.png"),"GuardarCambios",self)
        self.eventoGuardar.triggered.connect(self.guardaCambios)
        self.barraDeOpciones.addAction(self.eventoGuardar)
        
        
        #Creacion campos
        self.lblReglas=QtWidgets.QLabel("Reglas presentes en la gramática: ",self)
        self.txtResultados= QtWidgets.QTextEdit(self)
        self.lblReglas.adjustSize()
        self.lblReglas.move(10,80)
        self.txtResultados.resize(400, 300)
        self.txtResultados.move(10,100)
        
        self.lblCadenaDerivar=QtWidgets.QLabel("Cadena a Derivar",self)
        self.txtCadenaDerivar= QtWidgets.QTextEdit(self)
        self.lblCadenaDerivar.adjustSize()
        self.lblCadenaDerivar.move(450,100)
        self.txtCadenaDerivar.resize(300,25)
        self.txtCadenaDerivar.move(450,120)
        
        
        self.lblMetodo= QtWidgets.QLabel("Metodo de Derivacion",self)
        self.lblMetodo.adjustSize()
        self.lblMetodo.move(450, 200)
        self.btnDerecha= QtWidgets.QRadioButton("Derivacion Derecha",self)
        self.btnDerecha.adjustSize()
        self.btnDerecha.move(450, 220)
        self.lblMetodo.move(450, 200)
        self.btnIzq= QtWidgets.QRadioButton("Derivacion Izquierda",self)
        self.btnIzq.adjustSize()
        self.btnIzq.move(450, 240)
        
        
        self.btnIniciar= QtWidgets.QPushButton("Iniciar Derivacion",self)
        self.btnIniciar.move(450, 280)
        self.btnIniciar.clicked.connect(self.iniciaDerivacion)
        
        self.lblResultadosDeriv= QtWidgets.QLabel("Resultados de la Derivacion",self)
        self.lblResultadosDeriv.adjustSize()
        self.lblResultadosDeriv.move(10,420)
        self.txtDerivaciones=QtWidgets.QTextEdit(self)
        self.txtDerivaciones.resize(780, 200)
        self.txtDerivaciones.move(10, 440)
        
        
        
        
        

        
        self.show()
        
    def iniciaDerivacion(self):
       
       deriv= derivaciones()
       deriv.llenatabla(self.nombreArchivo,self.txtCadenaDerivar.toPlainText())
       primerCaracter= self.txtResultados.toPlainText()
       
       if self.btnDerecha.isChecked():
           deriv.derivacionDerecha(primerCaracter[0], 0,"")
           if deriv.reconocida>1:
               self.txtDerivaciones.setText("\n"+deriv.resultados+"\nDerivaciones por la derecha: "+str(deriv.reconocida)+
                                            "\nLa cadena: "+self.txtCadenaDerivar.toPlainText()+" es ambigua")
           else:
               self.txtDerivaciones.setText("\n"+deriv.resultados+"\nDerivaciones por la derecha: "+str(deriv.reconocida)+
                                            "\nLa cadena: "+self.txtCadenaDerivar.toPlainText()+" no es ambigua")
           
           
       elif self.btnIzq.isChecked():
            
            deriv.derivacionIzquierda(primerCaracter[0], 0,"")
            if deriv.reconocida>1:
                self.txtDerivaciones.setText("\n"+deriv.resultados+"\nDerivaciones por la izquierda: "+str(deriv.reconocida)+
                                             "\nLa cadena: "+self.txtCadenaDerivar.toPlainText()+" es ambigua")
            else:
                self.txtDerivaciones.setText("\n"+deriv.resultados+"\nDerivaciones por la izquierda: "+str(deriv.reconocida)+
                                             "\nLa cadena: "+self.txtCadenaDerivar.toPlainText()+" no es ambigua")
           
       else:
            self.txtDerivaciones.setText("Selecciona una opcion de derivacion")
           
       
       deriv.limpiaTabla()   
       deriv.resultados="" 
       deriv.reconocida=0
       deriv.derivaciones=0
       
           
            
           
       
    def cierra_aplicacion(self):
        opcion= QtWidgets.QMessageBox.question(self, "salir de la aplicacion","¿seguro?",QtWidgets.QMessageBox.question.Yes | QtWidgets,QtWidgets.QMessageBox.question.No)
        
            
        if opcion==QtWidgets.QMessageBox.question.Yes:
            sys.exit()
        else:
            pass
        
        
        
        
    def abrir_archivo(self):
        deriv=derivaciones()
        #tiene dos self porque en uno se está mandando la ventana como parametro
        self.nombreArchivo=deriv.abrir_archivo(self, self.vOpenfilename, self.txtResultados,self.bandera_abrir)
        
            
    def guardaCambios(self):
       f=open(self.nombreArchivo, "w")
       #Eliminamos el contenido del archivo
       f.truncate(0)
       f.write(self.Resultados.toPlainText())
       f.close()
            
       
        
            
class derivaciones():
    
    tabla=[]
    cadenaDePrueba=""
    resultados=""
    derivaciones=0
    reconocida=0
    
    def abrir_archivo(self,window, vOpenfilename, Resultados, bandera_abrir):
        vOpenfilename= QtWidgets.QFileDialog.getOpenFileName(window,"Open File",filter="*.txt")[0]

        if vOpenfilename=="":
            return
        f=open(vOpenfilename, "r")
        vTextstring=f.read()
        Resultados.setText(vTextstring)
        f.close()
        bandera_abrir=True
        return vOpenfilename
    
    def derivacionIzquierda(self,cabezaActual,noChar,MensajeDeDerivacion):
        if noChar<= len(self.cadenaDePrueba):
            i=0
            while i< len(cabezaActual):
                if cabezaActual[i].isupper():#Revisa que sea mayuscula
                    break
                i+=1#Si no es mayuscula busca en el siguiente caracter
            if i<len(cabezaActual):
                j=0
                while j < len(self.tabla):
                    regla=self.tabla[j]#guardamos la regla en la variable
                    if regla[0]== cabezaActual[i]:#Si la cabeza de la regla es igual a la cabeza actual entra
                        mensajeDeriv=MensajeDeDerivacion+""
                        parteIzq=cabezaActual[0:i]#Separamos la cadena
                        parteDer=cabezaActual[i+1:len(cabezaActual)]
                        nueva = parteIzq+ regla[1]+parteDer#relga[1] corresponde al cuerpo de la regla
                        if regla[1]=="e":
                            nueva = parteIzq+parteDer
                        
                        mensajeDeriv=mensajeDeriv+"->("+cabezaActual+","+str(j)+")"#j es el numero de regla
                        print(mensajeDeriv)
                        self.derivacionIzquierda(nueva, len(nueva), mensajeDeriv)
                    j+=1
                
        if cabezaActual==self.cadenaDePrueba:
            self.resultados=self.resultados + MensajeDeDerivacion+"->("+ cabezaActual+")\n"
            self.derivaciones+=1
            self.reconocida+=1
        
            
        
        
        
    def derivacionDerecha(self,cabezaActual,noChar,MensajeDeDerivacion):
        if noChar <= len(self.cadenaDePrueba):
            i=len(cabezaActual)-1
            while i >=0:
                if cabezaActual[i].isupper():#Revisa que sea mayuscula
                    break
                i-=1#Si no es mayuscula busca en el siguiente caracter
            if i<len(cabezaActual):
                j=0
                while j < len(self.tabla):
                    regla=self.tabla[j]#guardamos la regla en la variable
                    if regla[0]== cabezaActual[i]:#Si la cabeza de la regla es igual a la cabeza actual entra
                        mensajeDeriv=MensajeDeDerivacion+""
                        parteIzq=cabezaActual[0:i]#Separamos la cadena
                        parteDer=cabezaActual[i+1:len(cabezaActual)]
                        nueva = parteIzq+ regla[1]+parteDer#relga[1] corresponde al cuerpo de la regla
                        mensajeDeriv=mensajeDeriv+"->("+cabezaActual+","+str(j)+")"#j es el numero de regla
                        self.derivacionDerecha(nueva, len(nueva), mensajeDeriv)
                    j+=1
                
        if cabezaActual==self.cadenaDePrueba:
            self.resultados=self.resultados + MensajeDeDerivacion+"->("+ cabezaActual+")\n"
            self.derivaciones+=1
            self.reconocida+=1
        
        
        
    def llenatabla(self,nombreArchivo,cadenaPrueba):
        #abrimos el archivo
        archivo=open(nombreArchivo,"r")
        lineas=archivo.readlines()#Guardamos en una lista el contenido de cada linea
        archivo.close()
        for x in lineas :
            
                
            self.tabla.append([x[0],x[3:len(x)-1]])#llenamos la tabla con el contenido de cada linea omitiendo los "->"
        
        self.cadenaDePrueba=cadenaPrueba
        print(str(self.tabla) + self.cadenaDePrueba)
        
    def limpiaTabla(self):
        self.tabla.clear()
        
    
 
def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI=ventana()
    
    sys.exit(app.exec_())

main()
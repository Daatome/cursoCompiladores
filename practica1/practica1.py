



import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ventana(QtWidgets.QMainWindow):

    
    def __init__(self):
        super(Ventana, self).__init__()
        self.setGeometry(50,50,600,500)
        
        self.openfile= QtWidgets.QAction("&Abrir Archivo", self)
        self.openfile.setStatusTip("Abrir Archivo")
        self.openfile.triggered.connect(self.abrir_archivo)

        self.EventoSalir= QtWidgets.QAction(QtGui.QIcon("/PythonGrafico/ejemplo1/iconos/exit.png"),"salir", self)
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

    def home(self):
        self.bandera_abrir= False
        self.Resultados=QtWidgets.QTextEdit(self)

        eventoAbrirLocal = QtWidgets.QAction(QtGui.QIcon("/practica1/imagenes/iconos/share.png"), "Abrir un archivo",self)
        eventoAbrirLocal.triggered.connect(self.abrir_archivo)
        self.barraDeOpciones=self.addToolBar("Archivo")
        self.barraDeOpciones.addAction(eventoAbrirLocal)

        self.eventoSalirLocal= QtWidgets.QAction(QtGui.QIcon("/practica1/imagenes/iconos/exit.png"),"Salir",self)
        self.eventoSalirLocal.triggered.connect(self.cierra_aplicacion)
        self.barraDeOpciones.addAction(self.eventoSalirLocal)

        #creacion de boton y campos de texto
        self.btnContarTokens = QtWidgets.QPushButton("Contar Tokens",self)
        self.lblTokenTipoInt= QtWidgets.QLabel(" tokens tipo int",self)
        self.txtTokenTipoInt= QtWidgets.QLineEdit(self)
        self.lblTokenTipoFloat= QtWidgets.QLabel(" tokens tipo float",self)
        self.txtTokenTipoFloat= QtWidgets.QLineEdit(self)
        self.lblTokenTipoBoolean= QtWidgets.QLabel("tokens tipo Boolean",self)
        self.txtTokenTipoBoolean= QtWidgets.QLineEdit(self)
        self.lblTokenTipoChar= QtWidgets.QLabel(" tokens tipo char",self)
        self.txtTokenTipoChar= QtWidgets.QLineEdit(self)
        self.lblTokenTipoString= QtWidgets.QLabel(" tokens tipo String",self)
        self.txtTokenTipoString= QtWidgets.QLineEdit(self)

        #agregamos los componentes a la ventana
        self.btnContarTokens.move(450,70)
        
        self.lblTokenTipoInt.move(450,100)
        self.txtTokenTipoInt.resize(100,30)
        self.txtTokenTipoInt.move(450,125)

        self.lblTokenTipoFloat.move(450,175)
        self.txtTokenTipoFloat.resize(100,30)
        self.txtTokenTipoFloat.move(450,200)

        self.lblTokenTipoBoolean.move(450,250)
        self.txtTokenTipoBoolean.resize(100,30)
        self.txtTokenTipoBoolean.move(450,275)

        self.lblTokenTipoChar.move(450,325)
        self.txtTokenTipoChar.resize(100,30)
        self.txtTokenTipoChar.move(450,350)

        self.lblTokenTipoString.move(450,400)
        self.txtTokenTipoString.resize(100,30)
        self.txtTokenTipoString.move(450,425)
        #conectamos el boton con el metodo
        self.btnContarTokens.clicked.connect(self.cuenta_tokens)





        self.Resultados.resize(400,420)
        self.Resultados.move(10,65)

        self.show()
    
    def abrir_archivo(self):
        self.vOpenfilename= QtWidgets.QFileDialog.getOpenFileName(self,"Open File",filter="*.txt")[0]

        if self.vOpenfilename=="":
            return
        f=open(self.vOpenfilename, "r")
        vTextstring=f.read()
        self.Resultados.setText(vTextstring)
        f.close()
        self.bandera_abrir=True
    
    def cierra_aplicacion(self):
        opcion= QtWidgets.QMessageBox.question(self, "salir de la aplicacion","¿seguro?",QtWidgets.QMessageBox.question.Yes | QtWidgets,QtWidgets.QMessageBox.question.No)
        
        if opcion==QtWidgets.QMessageBox.question.Yes:
            sys.exit()
        else:
            pass

    #este metodo se lanza al presionar el boton de cuenta tokens, lee el documento con ayuda de otro metodo
    def cuenta_tokens(self):
        self.txtTokenTipoInt.setText("implementando metodo")
        
        palabra=""
        if self.vOpenfilename=="":
            return
        f=open(self.vOpenfilename, "r")
        vTextstring=f.read()
        for line in vTextstring:
            if line ==" " or line=="\n":
                self.busca_palabra(palabra)
                palabra=""
            else:
                palabra=palabra+line
        self.busca_palabra(palabra)
        palabra="" 
        self.reiniciaTokens()  
            
        

    #este metodo se encarga de buscar la palabra pasada en un diccionario, si no se encuentra es un token
    #de tipo String 
    def busca_palabra(self,palabra):
        
        diccionarioChar={
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",
            "#","$","%","&","/","(",")","=","?","¡","¿",":",",","-","_",";","{","}","+"

        }
        diccionarioBoolean={"True","False"}
        if diccionarioBoolean.__contains__(palabra):
            self.tokensBoolean+=1
        else:   
            #este else if es para las cadenas de un caracter
            if(diccionarioChar.__contains__(palabra) and len(palabra)==1 ):
               self.tokensChar+=1
            elif len(palabra)==1:#si tiene longitud 1 y no es un simbolo entonces es un numero
                self.tokensInt+=1
        
            if len(palabra)> 1 :
                guardaPalabra = list(palabra)
                
                bandera = False
                for caracter in guardaPalabra:
                    if diccionarioChar.__contains__(caracter):
                        bandera=True
                if bandera==True:
                    self.tokensString+=1
                    
                
                if bandera==False:
                    bandera2=False
                    for caracter in guardaPalabra:
                        if caracter==".":
                            bandera2=True
                    if bandera2== True:
                        self.tokensFloat+=1
                        
                    else:
                        self.tokensInt+=1

               
                        


        self.txtTokenTipoChar.setText(str(self.tokensChar))
        self.txtTokenTipoString.setText(str(self.tokensString))
        self.txtTokenTipoInt.setText(str(self.tokensInt))
        self.txtTokenTipoBoolean.setText(str(self.tokensBoolean))
        self.txtTokenTipoFloat.setText(str(self.tokensFloat))
        

    def reiniciaTokens(self):
        self.tokensBoolean=0
        self.tokensChar=0
        self.tokensFloat=0
        self.tokensInt=0
        self.tokensString=0
        
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI=Ventana()
    
    sys.exit(app.exec_())

main()









    
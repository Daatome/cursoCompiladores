import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Automata_FD

class Ventana(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ventana, self).__init__()
        self.setGeometry(50,50,600,500)
        
        
        self.AFD=QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap("/practica2/imgAutomata/Captura.png")
        
        
        self.home()
        
    def home(self):
        #se asigna el pixmap a la etiqueta y se mueve a una posicion en la ventana
        #Etiqueta para la imagen de fondo
        pixmap = QtGui.QPixmap("Captura.png")
        ancho = pixmap.height()
        largo = pixmap.width()
        print (ancho, largo)
        self.AFD.setPixmap(pixmap)
        self.AFD.resize(largo, ancho)
        self.AFD.move(200, 120)    

        
    
        
        #creacion de etiquetas y campos de texto
        self.lblAbecedario= QtWidgets.QLabel("Lenguaje Sigma{1, 0}  ",self)
        self.lblAbecedario.adjustSize()
        self.lblProporcionaCadena= QtWidgets.QLabel("Proporcione la cadena a evaluar: ",self)
        self.lblProporcionaCadena.adjustSize()
        self.txtCadena= QtWidgets.QLineEdit(self)
        self.btnComenzar= QtWidgets.QPushButton("Comenzar",self)
        self.lblResultado= QtWidgets.QLabel("Resultado de la evaluacion: ",self)
        self.lblResultado.adjustSize()
        self.txtResultado= QtWidgets.QLineEdit(self)
        self.btnLimpiar= QtWidgets.QPushButton("Limpiar",self)

        #Se colocan los elementos en la ventana
        self.lblAbecedario.move(10,250)
        self.lblProporcionaCadena.move(10,350)
        self.txtCadena.move(200,340)

        self.lblResultado.move(10,400)
        self.txtResultado.move(200,390)
        self.btnComenzar.move(100,300)
        self.btnLimpiar.move(200,300)
        self.txtResultado.setEnabled(False)
        self.txtResultado.adjustSize()
        self.txtCadena.adjustSize()

        #aqui vamos a conectar el boton con el método
        self.btnComenzar.clicked.connect(self.leeCadena)
        self.btnLimpiar.clicked.connect(self.limpiaCampos)


        self.show()

        #se encarga de recuperar la cadena escrita y manda a llamar al estado 0
    def leeCadena(self):
        cadena= self.txtCadena.text()
        cont=0

        resultado=Automata_FD.estado0(cadena,cont)
        
        if resultado==True:
            self.txtResultado.setText("La cadena  es reconocida")
        
        elif resultado==False:
            self.txtResultado.setText("La cadena no es reconocida")

        #si el resultado es distinto de un booleano significa que el usuario introdujo caracteres no permitidos    
        elif resultado=="na":
            dialogo = QtWidgets.QDialog()
            texto= QtWidgets.QLabel("La cadena solo recibe 1 y 0", dialogo)
            
            dialogo.setGeometry(50,50,300,100)
            dialogo.move(200,200)
            dialogo.setWindowTitle("Cadena incorrecta")

            dialogo.exec_()
    
    def limpiaCampos(self):
        self.txtCadena.setText("")
        self.txtResultado.setText("")
        
      


def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI=Ventana()
    sys.exit(app.exec_())

main()

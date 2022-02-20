#importacion de la libreria qtgui y el metodo sys para darle salida a la aplicacion grafica
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

#Declaracion de la clase ventana que hereda atributos y metodos de la clase de qtWidgets.QMainWindow
class Ventana(QtWidgets.QMainWindow):
    
    def __init__(self):
        #Constructor de la clase mediante el comando super, indico que cargue todo lo de su clase padre
        super(Ventana, self).__init__()
        self.setGeometry(50,50,500,300)
        #self.windowTitle("Segunda Ventana de prueba")
        
        EventoSalir= QtWidgets.QAction(QtGui.QIcon("/PythonGrafico/ejemplo1/iconos/exit.png"),"salir", self)
        EventoSalir.setShortcut("Ctrl+Q")
        EventoSalir.setStatusTip("salir de la aplicacion")
        EventoSalir.triggered.connect(self.cierra_aplicacion)

        menuPrincipal= self.menuBar()
        menuArchivo = menuPrincipal.addMenu("&Archivo")
        menuArchivo.addAction(EventoSalir)
        self.home()

    def home(self):

        self.btnSalir= QtWidgets.QPushButton("Salir",self)
        self.btnSaludo = QtWidgets.QPushButton("Despliega Nombre", self)

        self.entradaTexto= QtWidgets.QLineEdit(self)
        self.salidaTexto= QtWidgets.QLineEdit(self)
        self.solicitaLbl= QtWidgets.QLabel("ingresa tu nombre:", self)
        self.resultadoLbl=QtWidgets.QLabel("Resultado:",self)

        self.entradaTexto.resize(200,30)
        self.entradaTexto.move(200,50)
        self.solicitaLbl.move(105,50)
        self.resultadoLbl.move(145,145)
        self.salidaTexto.resize(200,30)
        self.salidaTexto.move(200,150)


        self.btnSalir.clicked.connect(self.cierra_aplicacion)
        self.btnSaludo.clicked.connect(self.despliega)

        self.btnSaludo.resize(100,40)
        self.btnSaludo.move(200,100)
        self.btnSalir.resize(100,40)
        self.btnSalir.move(200,200)

        self.show()

    def despliega(self):

        mensaje="Hola a python grafico "+ self.entradaTexto.text()
        self.salidaTexto.setText(mensaje)

    def cierra_aplicacion(self):
        sys.exit()

def main():
    app= QtWidgets.QApplication(sys.argv)

    GUI =Ventana()
    sys.exit(app.exec_())

main()
    






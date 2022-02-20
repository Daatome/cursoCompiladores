class Vehiculo:#declaracion de un objeto
    #declaracion del constructor
    def __init__(self, marca,subMarca,color,placas,anio,numeroCilindros,numeroPasajeros):
        #no es necesario crear los atributos antes, al referirnos con self. ya los estamos creando
        self.marca= marca
        self.subMarca= subMarca
        self.color=color
        self.placas=placas
        self.anio=anio
        self.numeroCilindros= numeroCilindros
        self.numeroPasajeros= numeroPasajeros
   #fin constructor

    def getMarca(self):
        print("Marca: ",self.marca)
    #fin metodo marca

def main():
    carro1= Vehiculo("Volkswagen","Jetta","Rojo","mm15-35",2020,4,5)
    carro1.getMarca()

main()#llamada al main


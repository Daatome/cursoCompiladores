#comentario de una sola linea
'''Comentario de mas lineas'''
def leeMensaje():
    try:
        numero=  int(input("introduce tu edad"))
        print("tu edad es : ", numero," años")
    except:
        print("Debes introducir un numero entero")




def main():
    f=lambda x: x**2
    print(f(7))
    leeMensaje()
main()

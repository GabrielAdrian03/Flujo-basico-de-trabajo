#Trabajo de Adrian Gonzales y Martínez Mauro
import os
import msvcrt

def clear():
    #Una funcion para limpiar pantalla
    if os.name == "nt":
        #En este caso, se usa en Windows y llama el comando 'cls'
        os.system("cls")
    else:
        #Este otro caso, se usa en Linux y llama el comando 'clear'
        os.system("clear")

def f_formaDePago(precioDescTonelada,formaDePago):
    #Esta función Calcula el porcentaje a pagar para el precio final
    if formaDePago == 1:
        descuento = -0.05
        cosa = "Efectivo"
        otro = "descuento de 5%"
    elif formaDePago == 2:
        descuento = 0.10
        cosa = "Tarjeta"
        otro = "recargo de 10%"
    elif formaDePago == 3:
        descuento = 0.15
        cosa = "Pagaré"
        otro = "recargo de 15%"
    descontando = precioDescTonelada * descuento
    #Con 'return' los valores llamados anteriormente
    return descontando, descuento, cosa, otro

def f_descuentoTonelada(subTotal,peso):
    #Esta función calcula en base al peso solicitado
    if peso > 1:
        descTonelada = 0.10
        prTonelada = "10%"
    elif peso > 2:
        descTonelada = 0.20
        prTonelada = "20%"
    elif peso > 5:
        descTonelada = 0.35
        prTonelada = "35%"
    else:
        descTonelada = 0.0
        prTonelada = "0%"
    descTotal = subTotal * peso
    #Retorna el Valor solicitado anteriormente
    return descTotal * descTonelada, prTonelada
        
def f_envio(kilometros):
    #Esta función se utiliza para calcular el precio por cada 100 Kilometros
    if kilometros <100:
        kilometros=50000
        return kilometros
    else:
        return (kilometros // 100) * 50000

hojaVerde = 36830
canchada = 139954
producto = " "
precioConDescton = 0
precioPago = 0

while True:
    try:
        #--------------------Inicio--------------------#
        print("***************************************")
        print("=Calculadora del Precio de la Yerba Mate=")
        print("***************************************\n")

        #Definiendo tipos y asignando precio para mas adelante
        while True:
            tipo = int(input("=Ingrese el tipo de Yerba Mate que quiera=\n[1] Yerba Mate tipo Hoja verde\n[2] Yerba Mate tipo Canchada\n>>> "))
            if tipo == 1:
                producto = "Hoja Verde"
                print("=Usted Selecciono tipo de Yerba Mate Hoja Verde=")
                total = hojaVerde
                break
            elif tipo==2:
                producto = "Canchada"
                print("=Usted Selecciono tipo de Yerba Mate Canchada=")
                total = canchada
                break
            else:
                print("=Valor no valido=")
                print("=Vuelva a intentarlo=")

        #Ingresando cantidad por toneladas para despues hacer los calculos
        while True:
            peso = float(input("=Ingrese el peso en toneladas de la Yerba Mate=\n>>> "))
            if peso >=1:
                subTotal = total * peso
                descTonelada, porcentajeTonelada = f_descuentoTonelada(total,peso)
                precioDescTonelada = subTotal - descTonelada
                print(f"=Usted comprara {peso} toneladas=")
                break
            else:
                print("=Valor incorrecto, Intente de Nuevo=")


        #Definiendo formas de pago para calcular los descuentos
        while True:
            print("=Ingrese la forma de pago hecha=")
            print("[1] Efectivo (Recibe un 5% de descuento)")
            print("[2] Tarjeta  (Recibe un 10% de recargo)")
            formaDePago = int(input("[3] Pagaré   (Recibe un 15% de recargo)\n>>> "))
            if formaDePago >=1 and formaDePago <4:
                precioDescuento, elDescuento, metodoPago, parte = f_formaDePago(precioDescTonelada,formaDePago)
                #Final es con todo el resto incluido
                precioPago = precioDescTonelada + precioDescuento
                break
            else:
                print("=Incorrecto, Intente de nuevo=")
        #Seccion de envios
        while True:
            envio = str(input("=¿Desea que le enviemos su producto?= [S] o [N]\n>>> "))
            envio = envio.upper()
            if envio == "S":
                while True:
                    kilometros = float(input("=Ingrese a cuantos KM se encuentra del punto de venta=\n>>> "))
                    if kilometros > 0:
                        distancia = f_envio(kilometros)
                        precioFinal = precioPago + distancia
                        break
                    else:
                        print("=Incorrecto, Intente de Nuevo=")
        
            #Impresion por pantalla de los resultados
            print(f"\n=Su producto es Yerba Mate tipo {producto} con un precio unitario por tonelada de ${total}=")
            print(f"=Llevando {peso} tonelada/s el precio es de ${subTotal}=")
            print(f"=Como lleva {peso} tonelada/s de Yerba Mate, tiene un {porcentajeTonelada} de descuento, para un total de ${precioDescTonelada}=")
            print(f"=Tiene un {parte} pagando en {metodoPago}=")
            print(f"=El subtotal es de ${precioPago} =")
            if envio == "S":
                print(f"=El recargo por {kilometros} KM de envio es de ${distancia}=")
                print(f"=Por lo que se le adicionara a un total de ${precioFinal}=")
                break
            elif envio == "N":
                print("=No solicito un envio=")
                print(f"=Por lo que su precio total es ${precioPago}=")
                break
            else:
                print("=Ingrese [S] o [N] segun corresponda=")
                
    except ValueError:
        print("=Error, Ingrese los datos correctamente=")
        

    opcion = str(input("=¿Desea Continuar en el Sistema?= [S] o [N]\n>>> ")).upper()
    if opcion == "S":
        pass
    elif opcion == "N":
        break
    else:
        print("=Opcion Invalida=")
        print("=Intente de Nuevo=")
    clear()
print("=Gracias por elegir nuestros servicios=")
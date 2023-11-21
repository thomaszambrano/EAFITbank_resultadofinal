from Seguridad import Seguridad
seguridad = Seguridad()
class PrestamosGrupos:

    def prestar_dinero_grupo(self, lista_grupos, movimientos):
        grupo = seguridad.Login_grupos(lista_grupos)
        if grupo is not None:
            prestamo = int(input("Ingrese el dinero que desea pedir prestado: "))
            plazo = int(input("Ingrese el tiempo que desea pedir prestado el dinero: "))
            if grupo.obtener_cuenta() > prestamo + grupo.obtener_prestamo() and plazo >= 2:
                print(f"El préstamo del dinero al grupo {grupo.obtener_nombre_grupo()} ha sido autorizado")
                grupo.cuenta += prestamo
                grupo.prestamo += prestamo
                grupo.meses += plazo

                saldo_inicial = grupo.obtener_cuenta() - prestamo
                saldo_final = grupo.obtener_cuenta()
                tipo_movimiento = "Préstamo al grupo de ahorro"
                movimientos.registrar_movimiento_grupo(grupo, tipo_movimiento, prestamo, saldo_inicial, saldo_final)
            else:
                print("El préstamo que se pide es mayor a la cantidad de dinero que tienen en la cuenta o el plazo es menor a dos meses")
        else:
            print("El grupo que ingresa no existe, vuelva a intentarlo de nuevo")

    def prestamo_otro_grupo(self):
        pass
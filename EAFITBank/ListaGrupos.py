class ListaGrupos:
    def __init__(self):
        self.lista_grupos = []

    def agregar_grupo(self, usuario):
        self.lista_grupos.append(usuario)

    def eliminar_grupo(self):
        pass

    def imprimir_grupos(self):
        print("Lista de todos los grupos registrados en EAFITBank: ")
        print(25*"")
        for grupo in self.lista_grupos:
            datos_personales = grupo.obtener_datos_personales_grupo()
            nombre_grupo = grupo.obtener_nombre_grupo()
            cuenta_grupo = grupo.obtener_cuenta()
            prestamo_grupo = grupo.obtener_prestamo()
            meses_grupo = grupo.obtener_meses()
            print(f"Nombres de los usuarios del grupo: {datos_personales[0]}")
            print(f"Correo: {datos_personales[1]}")
            print(f"Nombre del grupo: {nombre_grupo}")
            print(f"Cuenta del grupo: {cuenta_grupo}")
            print(f"Prestamo del grupo: {prestamo_grupo} y plazo que tienen {meses_grupo} meses")
            print(25 * "-")

import imp


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito']={}
        #else:
        self.carrito = carrito

    def agregar(self, articulo):
        if (str(articulo.id) not in self.carrito.keys()):
            self.carrito[articulo.id]={"articulo_id" : articulo.id, "nombre" : articulo.nombre, "precio" : str(articulo.precio), "cantidad" : 1, "imagen" : articulo.imagen.url}
        else:
            for key, value in self.carrito.items():
                if key == str(articulo.id):
                    value['cantidad']=value['cantidad']+1
                    value['precio']=float(value['precio'])+articulo.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, articulo):
        articulo.id = str(articulo.id)
        if articulo.id in self.carrito:
            del self.carrito[articulo.id]
            self.guardar_carrito()

    def quitar_articulo(self, articulo):
        for key, value in self.carrito.items():
            if key == str(articulo.id):
                value['cantidad']=value['cantidad']-1
                value['precio']=float(value['precio'])-articulo.precio
                if value['cantidad'] <1:
                    self.eliminar(articulo)
                break
        self.guardar_carrito()

    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True


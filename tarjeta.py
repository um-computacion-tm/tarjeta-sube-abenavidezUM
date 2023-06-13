class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"
PRECIO_TICKET = 50

ACTIVADO = "activado"
DESACTIVADO = "desactivado"

class Sube:
    def __init__(self):
        self.saldo = 1000
        self.grupo_beneficiario = None
        self.estado = ACTIVADO

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == PRIMARIO:
            return 35
        return PRECIO_TICKET

    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("El usuario se encuentra desactivado.")
        precio_ticket = self.obtener_precio_ticket()
        if self.saldo < precio_ticket:
            raise NoHaySaldoException("No hay saldo suficiente para pagar el pasaje.")
        self.saldo -= precio_ticket

    def cambiar_estado(self, estado):
        if estado == ACTIVADO or estado == DESACTIVADO:
            self.estado = estado
        else:
            raise EstadoNoExistenteException("El estado especificado no existe.")

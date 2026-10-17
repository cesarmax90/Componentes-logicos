"""
Agregados principales del Bounded Context: Operación de Renta.
"""

class Reservacion:
    def __init__(self, folio, cliente_id, categoria_id, sucursal_id):
        self.folio = folio
        self.cliente_id = cliente_id
        self.categoria_id = categoria_id
        self.sucursal_id = sucursal_id
        self.estado = "Creada"

    def cancelar(self, politica_cancelacion, fecha_actual):
        pass

    def liberar_por_no_show(self, politica_cancelacion, fecha_actual):
        pass

class ContratoRenta:
    def __init__(self, folio, vehiculo_id, cliente_id):
        self.folio = folio
        self.vehiculo_id = vehiculo_id
        self.estado = "Abierto"

    def registrar_devolucion(self, fecha_hora):
        # Emite evento: VehiculoDevuelto
        pass

class Liquidacion:
    def __init__(self, contrato_id, deposito_ref):
        self.contrato_id = contrato_id
        self.deposito_ref = deposito_ref
        self.cargos = []

    def calcular_cargos(self, diferencias, condiciones, politica_cargos, ahora):
        # Valida reglas paramétricas de negocio sin depender de la BD
        pass

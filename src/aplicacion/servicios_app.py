"""
Service Layer (Application Services).
Orquestan los casos de uso coordinando transacciones, repositorios y eventos.
NO contienen reglas de negocio (sin ifs de dominio).
"""

class ContratoAppService:
    def __init__(self, unidad_de_trabajo, repositorios, permisos, bus_eventos, reloj):
        self.uow = unidad_de_trabajo
        self.contratos = repositorios['contratos']
        self.permisos = permisos
        self.bus = bus_eventos
        self.reloj = reloj

    def procesar_devolucion(self, contrato_id, actor):
        self.permisos.exigir(actor, "procesar_devolucion")
        
        with self.uow: # Inicia transacción
            contrato = self.contratos.obtener(contrato_id)
            contrato.registrar_devolucion(self.reloj.ahora())
            
            self.contratos.guardar(contrato)
            self.bus.publicar(contrato.eventos)

class LiquidacionAppService:
    def __init__(self, unidad_de_trabajo, repositorios, politica_cargos, reloj, bus_eventos):
        self.uow = unidad_de_trabajo
        self.repositorios = repositorios
        self.politica_cargos = politica_cargos
        self.reloj = reloj
        self.bus = bus_eventos

    def calcular_cargos(self, evento_vehiculo_devuelto):
        # Handler del evento VehiculoDevuelto
        with self.uow:
            contrato = self.repositorios['contratos'].obtener(evento_vehiculo_devuelto.contrato_id)
            entrega = self.repositorios['inspecciones'].entrega_de(evento_vehiculo_devuelto.contrato_id)
            devolucion = self.repositorios['inspecciones'].devolucion_de(evento_vehiculo_devuelto.contrato_id)
            liq = self.repositorios['liquidaciones'].por_contrato(evento_vehiculo_devuelto.contrato_id)
            
            # Delega la evaluación de las reglas al dominio
            liq.calcular_cargos(
                devolucion.comparar_contra(entrega),
                contrato.condiciones(),
                self.politica_cargos,
                self.reloj.ahora()
            )
            
            self.repositorios['liquidaciones'].guardar(liq)
            self.bus.publicar(liq.eventos)

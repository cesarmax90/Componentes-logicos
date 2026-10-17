"""
Interfaces de Repositorios (Adaptadores).
En un proyecto real, aquí irían las consultas SQL o el uso de un ORM.
"""

class RepositorioContratos:
    def obtener(self, contrato_id):
        # Simulación: SELECT * FROM contratos WHERE id = contrato_id
        pass
        
    def guardar(self, contrato):
        # Simulación: INSERT o UPDATE en la tabla contratos
        pass

class RepositorioLiquidaciones:
    def por_contrato(self, contrato_id):
        pass
        
    def guardar(self, liquidacion):
        pass

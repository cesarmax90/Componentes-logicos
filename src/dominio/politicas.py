"""
Domain Services y Policies.
Contienen las reglas de negocio que pueden cambiar frecuentemente.
"""

class PoliticaCargos:
    def calcular_cargo_retraso(self, minutos_retraso):
        # Regla: Tolerancia de 29 min, tope de 1 día
        pass

    def calcular_cargo_kilometraje(self, km_excedente):
        # Regla: $3 MXN por km extra sobre los 200 km/día
        pass

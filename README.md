# ACT-F03-NovaRent
# Diseño Arquitectural del Sistema - NovaRent

Bienvenido al repositorio del proyecto **NovaRent**, correspondiente a la Actividad 3 de la unidad de diseño arquitectural para el curso de Componentes Lógica de Negocio.

## Equipo de Trabajo

* **Arturo Sebastian Pérez Zapata** - 2142942
* **Cesar Maximiliano Peña Mendoza** - 2144135
* **Diego Alberto Sierra Mendoza** - 2143733

**Profesor:** Miguel Ángel Gómez Marroquín  
**Módulo Netacad:** 3  
**Fecha:** 15/10/2026

## Empresa y Alcance

**Empresa Asignada:** NovaRent

**Contexto Delimitado (Bounded Context):** Operación de Renta.

La arquitectura del sistema está enfocada en gestionar integralmente el proceso principal de renta de vehículos. El alcance se divide en los siguientes subdominios:

* **Core:** Reservación, Contrato, Inspección, Liquidación.
* **Soporte:** Flota, Limpieza, Catálogo (Categoría, Sucursal, Empleado).
* **Genérico:** Pagos y Notificaciones.

**Patrón de Lógica de Negocio Seleccionado:** **Domain Model + Service Layer**.  
Las políticas de negocio complejas y cambiantes (tolerancias de tiempo, cobros por kilometraje, reglas de upgrade) se encapsulan en *Aggregates* y *Policies* puros, mientras que la *Service Layer* coordina las transacciones sin absorber reglas del dominio. Se aplicó CQRS básico para optimizar la generación de reportes analíticos.

## Estructura del Repositorio y Enlaces a Entregables

El repositorio está organizado según los estándares requeridos para facilitar su revisión. A continuación, los enlaces a los entregables principales:

* [**Informe de Arquitectura Completo**](./docs/ACT-F03_Diseno_Arquitectural_NovaRent1.pdf)  
  *Nota: Puedes consultar el documento principal en la carpeta `/docs`. Este archivo contiene la justificación del patrón, mapa de dominio completo, definición de la Service Layer, separación de Command/Queries, ADRs, revisión SOLID, matriz de trazabilidad y bitácora de IA.*

* [**Diagramas UML y de Secuencia**](./diagrams/)  
  *Archivos fuente y exportaciones (Dominio, Clases, Secuencia de Entrega y Devolución).*

* [**Código Base**](./src/)  
  *Estructura de carpetas y código que refleja el Bounded Context, Aggregates, Application Services e interfaces de repositorios propuestos.*

## Instrucciones de Revisión

Para evaluar esta entrega, se sugiere el siguiente flujo de revisión:

1. **Revisión de Decisiones Arquitecturales (ADRs):** Consultar el documento PDF (Sección 4.3) para comprender el contexto y justificación de usar *Domain Model + Service Layer* y aislar las consultas de reportes (ADR-001 y ADR-002).
2. **Mapa de Dominio y Lenguaje Ubicuo:** Revisar la Sección 2 del documento. El código en la carpeta `/src/` utiliza estrictamente los términos definidos en español (ej. `Vehiculo`, `Reservacion`, `ContratoRenta`).
3. **Coordinación vs Lógica:** Evaluar la *Service Layer* (Sección 3). Notará que clases como `LiquidacionAppService` solo orquestan, mientras que las reglas duras viven en objetos como `PoliticaCargos`.
4. **Flujos de Secuencia:** Abrir la carpeta `/diagrams/` para contrastar el diseño estático con el comportamiento dinámico (ej. Flujo automatizado de Devolución y Liquidación mediante *Domain Events*).
5. **Uso de IA:** La bitácora detallando cómo se utilizó la IA como copiloto, los errores detectados y las correcciones humanas se encuentra al final del documento principal PDF.

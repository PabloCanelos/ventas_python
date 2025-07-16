# ventas_python
programa_ventas_python
 <!-- Estructura general del programa de ventas
1. Diseña el menú principal
- Opciones: vender producto, ver stock, ver ventas del día, ver total acumulado, ingresar nuevo producto, salir.
- Usa un loop para mantener el menú activo hasta que el usuario decida salir.
- Asegúrate de validar entradas numéricas y opciones inválidas.
2. Define las estructuras de datos
- Usa una lista de diccionarios para el stock. Cada diccionario representa un producto con claves como: nombre, precio, cantidad.
- Otra lista de diccionarios para registrar las ventas: cada venta tiene producto, cantidad vendida, total, hora.
3. Función para ingresar productos al stock
- Solicita nombre, precio y cantidad.
- Valida que no haya nombres duplicados.
- Agrega al stock o actualiza si ya existe.
4. Función para mostrar stock disponible
- Recorre la lista de productos y muestra nombre, cantidad y precio.
- Ordena si quieres por nombre o por cantidad.
5. Función para realizar una venta
- Solicita nombre del producto y cantidad.
- Verifica si el producto existe y hay suficiente cantidad.
- Calcula total, descuenta del stock, y agrega la venta a la lista.
- Muestra resumen de la venta.
6. Función para ver ventas del día
- Muestra todas las ventas realizadas, con datos individuales: producto, cantidad, total.
- Puedes agregar un filtro por hora si te interesa llevar control más detallado.
7. Función para calcular total acumulado
- Recorre la lista de ventas y suma todos los total.
- Muestra el total vendido hasta el momento.

🔁 Modularidad
Cada uno de estos pasos debería convertirse en funciones separadas. Así mantienes limpio tu código y puedes reutilizar lógica si decides expandirlo más adelante.

¿Quieres que te ayude a diseñar el esqueleto modular del programa o armar un pseudocódigo de ejemplo? Esto tiene potencial para practicar validaciones elegantes y una experiencia de usuario amigable, ¡tu especialidad! 😄 -->


# Metodo
Este programa simula el funcionamiento basico de un sistema de biblioteca, donde
los usuarios pueden pedir prestados libros. Antes de permitir un prestamo, el
sistema verifica que el usuario este autorizado y que el libro este disponible. Si todo
esta en orden, registra que el prestamo se ha realizado correctamente.
Ademas, el programa incluye pruebas automaticas que revisan que estas reglas se
cumplan correctamente en diferentes situaciones, como cuando un usuario no esta
autorizado, cuando un libro no esta disponible o cuando se hacen varios prestamos
seguidos. Estas pruebas ayudan a asegurarse de que el sistema funcione bien y sin
errores.

## Ventajas y Analisis del Codigo
Los resultados indican que todas las pruebas automatizadas del archivo
test_top_down.py se ejecutaron correctamente, sin errores ni fallos. Cada prueba
verifica un aspecto diferente del sistema de prestamo de libros: Desde un prestamo
exitoso, hasta casos donde el usuario no esta autorizado, el libro no esta disponible
o no existe, y finalmente la simulacion de varios prestamos seguidos. El porcentaje
al lado de cada prueba muestra el progreso del conjunto de tests, y PASSED
confirma que el sistema respondio como se esperaba en cada caso.
En cuanto a los cambios realizados en los tests, se amplio la cobertura para
contemplar mas situaciones reales que pueden ocurrir en el sistema. Agregando
pruebas para verificar que el sistema maneje correctamente libros que no existen y
que no permita prestamos cuando el libro no esta disponible. Ademas de un test que
simula multiples prestamos para asegurarnos que el sistema si registra bien cada
operacion. Por ultimo, se agregaron validaciones para comprobar que el registro de
prestamos en la base de datos simulada (stub) se actualice solo cuando el prestamo
es exitoso, ayudando a asegurar la robustez y confiabilidad del sistema.
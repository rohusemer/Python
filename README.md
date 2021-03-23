# Python
## Analizador de plagio
Se necesita construir un compilador para que, en primera instancia, poder analizar el código del proyecto y después poder comparar los árboles sintácticos generados. Por lo que:
  1. Se construye un analizador léxico usando la librería ply.lex de Python.
  2. Se construye un analizador sintáctico usando la librería ply.yacc de Python.
  3. Se genera un árbol sintáctico del código ingresado.
  4. Se usa una estructura de control para hacer la comparación de los árboles.
## DESCRIPCION DEL PROTOTIPO
El prototipo que presentamos dispone de una interfaz gráfica que se trata de una pantalla donde el usuario tiene la opción de introducir los códigos fuentes en leguaje de Python y un botón de comparar código en donde el programa realizará un análisis léxico y sintáctico y obtendrá los árboles sintácticos para almacenar los en tupla para que después se realice una comparación de las dos tuplas y devuelva la cantidad de parecido entre los dos códigos.

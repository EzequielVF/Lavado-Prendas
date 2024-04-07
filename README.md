# Lavado-Prendas

Enunciado #1
Una lavandería tiene que lavar prendas, algunas pueden ir juntas y otras no (destiñen).
El tiempo de cada lavado es el tiempo que lleva lavar la prenda más sucia de ese lavado.
Formato del archivo del problema
Cada línea comienza con un caracter que indica el contenido de la misma

"c": comentario formato: c Comentario ej: "c esto es un comentario"
"p": definición del problema formato: p c n m "c" es un comentario, "n" es la cantidad de prendas y "m" la cantidad de incompatibilidades ej: "p edges 10 30"
"e": incompatibilidad formato: e n1 n2 "n1" y "n2" son los números de prenda incompatibles entre ellas ej: "e 1 2"
"n": tiempo de lavado formato: n n1 c1 "n1" es el número de prenda y "c1" el tiempo de lavado ej: "n 5 3"
Formato del archivo de la solución
Cada renglón tiene dos valores separados por un espacio, el primero es el número de prenda, el según el número de lavado asignado. ej: "1 5" Esto sería lavar la prenda "1" en el lavado "5"
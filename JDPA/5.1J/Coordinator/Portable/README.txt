↑ Activa ajuste de linea en formato (la primera opcion).

Bienvenido a Coordinator.
Coordinator fue escrito con el propósito de facilitar la búsqueda de coordenadas de determinados establecimientos y su respectiva ubicación en un plano.
Para lograr esto, Coordinator obtiene los datos de ubicación de los diversos establecimientos de un archivo, realiza una búsqueda en Google Maps y en caso exitoso obtiene las coordenadas del lugar y una fotografía del plano con el lugar señalado.


====================== [GUIA RAPIDA] ========================

***Aparentemente Excel en versiones Espanolas en archivos csv se separan los valores con ; cuando debrian de ser con , 
Requerimientos:
	Windows 7/8/10
	Firefox 54 o superior instalado en el directorio por default del instalador

Al iniciar Coordinator por primera vez, se crearán carpetas dentro de Documentos. Es dentro de la carpeta /Documentos/Coordinator/Input donde deberá colocarse el archivo .csv que contenga todos los establecimientos a indexar con los siguientes lineamientos AL PIE DE LA LETRA:

	1) El nombre del archivo deberá de ser “data” sin comillas.
	2) Un establecimiento por fila.
	3) En caso de que un dato no exista, dejar la celda vacía.
	4) El archivo no deberá tener filas en blanco entre entradas.
	5) La columna (A) deberá llevar un numero escrito con digito, cada entrada debe tener un numero sucesivo al anterior.
	6)La columna (B) deberá llevar el nombre del establecimiento a buscar. *
	7)La columna (C) deberá llevar la sucursal*.
	8)La columna (D) deberá llevar la calle donde se encuentra el establecimiento(cuidado con carreteras).
	8)La columna (E) deberá llevar el número del establecimiento. En caso de no tener número, dejar la celda vacía.
	9)La columna (F) deberá llevar el estado.


Se pedirá el tipo de conexión a internet del usuario. (Consultable en fast.com)

Buena (1) para conexiones de 3 o más Mbps. 
Regular (2) para conexiones de 1 a 2 Mbps.
Mala (3) para velocidades menores a 1 Mbps. 


Al terminar de ejecutarse, los resultados de las búsquedas se encontrarán en /Documentos/Coordinator/Output. El archivo coordinates.csv contendrá todas las coordenadas, exceptions.txt contendrá los establecimientos que se hayan omitido e Images contendrá las imágenes del plano del establecimiento respectivo.

Los datos proporcionados en “data.csv” serán buscados en Google Maps, Google Maps está diseñado para buscar direcciones escritas por humanos. Por ejemplo, buscar “Banco Nacional de México S.A. de C.V.” no arrojara resultados, pero buscar “banamex” sí. Esto aplica para todos los demás rubros.



========================[MANUAL]===========================



Requerimientos:

	Windows 7/8/10
	Firefox 54 o superior

Coordinator no posee interfaz gráfica. Todos los comandos deben de ser escritos en la ventana que salta y presionar Enter al terminar de escribir. En cada pregunta, existen valores dentro de un paréntesis. Estos son las opciones que deberán ser introducidas i.e.

	¿Continuar? (Y/N)
	Y 
	*Presionar Enter*

Es preferible no tener otros programas abiertos a la hora de ejecutar Coordinator para acelerar el proceso de búsqueda. No obstante, es posible seguir trabajando en otras aplicaciones sin ningún problema.

Aunque no es necesario se recomienda trabajar con 100 a 1000 entradas a la vez. Trabajar un archivo .csv por empresa también ayuda a ordenar los resultados. 

Es necesario ejecutar Coordinator con permisos de administrador. 

El tipo de archivo donde se ubican los datos es del formato .csv. Este formato es, como su nombre en inglés lo dice, un archivo de Valores Separados por Comas. Al abrir este tipo de archivos con un programa como Excel (Windows), Numbers (iOS) y Calc (OpenOffice) se observa una tabla como cualquier otra. 
Con estos programas se puede convertir cualquier tipo de hoja de cálculo en un archivo .csv. Es en este archivo donde los establecimientos a buscar deben de colocarse siguiendo el siguiente formato AL PIE DE LA LETRA:

	1) El nombre del archivo deberá de ser “data” sin comillas.
	2) Un establecimiento por fila.
	3) En caso de que un dato no exista, dejar la celda vacía.
	4) El archivo no deberá tener filas en blanco entre entradas.
	5) La columna (A) deberá llevar un numero escrito con digito, cada entrada debe tener un numero sucesivo al anterior.
	6)La columna (B) deberá llevar el nombre del establecimiento a buscar. *
	7)La columna (C) deberá llevar la calle o domicilio del establecimiento.
	8)La columna (D) deberá llevar el número del establecimiento. En caso de no tener número, dejar la celda vacía.
	9)La columna (E) deberá llevar el estado.

Al ejecutar el programa por primera vez, se creará una carpeta dentro de Documentos llamada Coordinator, dentro de esta se encontrarán otras dos carpetas, Input y Output. El archivo “data.csv” deberá de ser colocado dentro de la carpeta Input. 

Al volver a ejecutar el programa y seleccionar empezar, se pedirá el número de la fila hasta el cual deberá de trabajar Coordinator. 

Después se pedirá el tipo de conexión a internet del usuario. 

	Buena (1) para conexiones de 3 o más Mbps. 
	Regular (2) para conexiones de 1 a 2 Mbps.
	Mala (3) para velocidades menores a 1 Mbps. 

La velocidad verdadera (no la provista por el ISP) puede ser comprobada fácilmente en fast.com Es preferible hacer una prueba de conexión antes de empezar para evitar errores y disminuir tiempos de espera.

Si todos los requerimientos anteriores se han cumplido, Coordinator empezara a trabajar. En la terminal de Coordinator se puede observar el estado del programa y las entradas restantes para terminar.

Al terminar de indexar los resultados, Coordinator esperará la respuesta del usuario, al obtenerla, Coordinator abrirá la carpeta Output en la que se encontraran los resultados. En esta carpeta habrá 3 elementos. 

	La subcarpeta Images en la cual se encontrarán las capturas de pantalla de los planos.
	El archivo coordinates.csv en el cual se encontrarán las coordenadas de los establecimientos.
	El archivo exceptions.txt en el cual se encontrarán los establecimientos que no pudieron ser encontrados.

Coordinator usa Google Maps para obtener las coordenadas y las capturas de los planos, esto significa que algunas veces, pueden existir excepciones debido a diversos errores. Para tener resultados más seguros, Coordinator no indexara los siguientes resultados:

	Cuando no existan resultados para la determinada búsqueda
	Cuando existan más de 10 resultados para una búsqueda

En dado caso, se omitirá el resultado y se indexará la excepción en exceptions.txt. Estas entradas deberán ser corregidas o buscadas manualmente.

*IMPORTANTE!

Los datos proporcionados en “data.csv” serán buscados en Google Maps, Google Maps está diseñado para buscar direcciones escritas por humanos. Por ejemplo, buscar “Banco Nacional de México S.A. de C.V.” no arrojara resultados, pero buscar “banamex” sí. e.g.

	'Suc. Andenes' --> 'Andenes' 
	'Santa Fe Edif./'--> 'Santa Fe'
	'Estado Libre y Soberano de Aguascalientes'--> 'Aguascalientes'
	Sin Numero --> “” (Dejar campo vacío)

(!) Es importante mencionar que las razones sociales no arrojan resultados
	'DEFA, S.A. de C.V.'--> 'Farmacias YZA'

La mayoría de las razones sociales y sus respectivas razones comerciales se encuentran en la página siem.gob.mx (para resultados en México)

Cuando la dirección de un establecimiento tenga el siguiente formato:

	Av. Melchor Ocampo esquina con Leibniz

La entrada deberá de ser omitida y buscada manualmente.

Finalmente, la razón social 'Controladora de Negocios Comerciales, S.A. de C.V.' es demasiado amplia.
Sólo será necesario borrar el contenido de esta columna para obtener resultados.

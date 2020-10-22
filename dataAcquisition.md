# Adquisicion de datos

## Apache Hadoop

Big data == 5V == **Volumen** (cantidad de datos), **Velocidad** (generacion y movimiento), **Variedad** (tipos), **Veracidad** (grado de confianza) y **Valor** (dificultad de explotacion).
Surge por los problemas de indexacion de la web expuesto por google. Se propone el ecosistema Hadoop que permite escalabilidad, tolerancia a fallos, gestion de diferentes tipos de datos, entorno compartido y aportar valor. Mediante un esquma de capas (desde el almacenamiento hasta niveles de abstaraccion para el manejo en alto nivel.) 

```
Hive Framework infraestrucruera de almacenamiento - Pig Plataforma apps distribuidas sobre MapReduce  

    || Spark - Storm  
    || Acceso a datos (Cassandra NoSQL, MongoDB, HBase)  
 -++++ MapReduce Modelo de computo/programación  
 -+++ YARN gestor de recursos  
 -++ HDSF sistema de fichero  
 -+ Hardware (básico) nodos de almacenamiento de computo (comodity hardware)  

Flume / Scoop Mover los datos e incorporarlos en el procesamiento  
```

## Modelo Map Reduce

Modelo Master Worker : Splitting, particionar datos para generar resultados parciales para luego ser combinados y obtener resultados finales.  
Map reduce permite procesar en paralelo y ser explotados con dos fases fundamentales, una de distribucion de los datos [ Procesos *Mappers* (número de mappers generados por el framework, clave valor) ejecutados en los nodos en los que se encuentran los datos que van a procesar ] y una fase de reduccion de información (recibe los pares clave valor para hacer el ordenamiento y reducción).

-- casaGatoLoro.img
```
# Contador de palabras

Map(String docid, String text):
  for each word w in text:
    Emit(w, 1);
    
Reduce(String term, Iterator <Int> values):
  int sum = 0;
  for each v in values:
    sum+= v;
  Emit(term, sum);
```

-- matrizVector.img

Nota del Mapper: **Emit(i, a<sub>ij</sub> * b<sub>j</sub>);**

```
# Multiplicación Matriz-Vector

Map(Matriz a, Vector b):
  foreach position i in b:
    Emit(i, aij * bj);
    
Reduce(String term, Iterator <Int> values):
  int sum = 0;
  for each v in values:
    sum += v;
  Emit(term, sum);
```

## HDFS - Hadoop Distributed File System

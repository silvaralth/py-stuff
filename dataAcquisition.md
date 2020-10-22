# Adquisicion de datos

## Apache Hadoop

Big data == 5V == **Volumen** (cantidad de datos), **Velocidad** (generacion y movimiento), **Variedad** (tipos), **Veracidad** (grado de confianza) y **Valor** (dificultad de explotacion).
Surge por los problemas de indexacion de la web expuesto por google. Se propone el ecosistema Hadoop que permite escalabilidad, tolerancia a fallos, gestion de diferentes tipos de datos, entorno compartido y aportar valor. Mediante un esquma de capas (desde el almacenamiento hasta niveles de abstaraccion para el manejo en alto nivel.) 

```
Hive Framework infraestrucruera de almacenamiento - Pig Plataforma apps distribuidas sobre MapReduce  

    || Spark - Storm  
    || Acceso a datos (Cassandra NoSQL, MongoDB, HBase)  
 -+++ MapReduce Modelo de computo/programación  
 -++ YARN gestor de recursos  
 -+ HDSF sistema de fichero  
 -- Hardware (básico) nodos de almacenamiento de computo (*commodity hardware*)  

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

Diseñado para sistemas de bajo coste, adecuado para aplicaciones de grandes de volumenes de datos. Puede consistir en miles de nodos. Proporciona alto ancho de banda. Al existir gran numero de nodos, existe alta probabilidad de fallo y por ende de nodos caidos, asi que es diseñado con deteccion de fallos y capacidad de recuperacion. Acceso a datos en Streaming, ha sido diseñado mas para procesamiento batch, el objetivo principal es conseguir un alto rendimiento (*"throughtput"*) mas que una baja latencia. Modelo de coherencia simple (una sola escritura y multiple lectura == *"write-once-read-many"*). El computo se ejecutan lo mas proximo posible a los datos, asi que proporciona interfaces para que se muevan las aplicaciones. Tambien es portable para moverlo a distintas plataformas.

### Arquitectura

NameNode: Gestor de todos los metadatos del sistema de ficheros y actua cono repositorio de los mismos.  
DataNode: Uno por cada Nodo, gestiona los Datos de cada cluster.

Ambos estan programados en JAVA y se ejecutan en maquinas comunes con sistema operativo basado eb GNU Linux.

Los clientes se realizan operaciones de escritura o lectura se dirigen al DataNode, nunca al NameNode a menos que se solicite una replicacion, esta si es gestionada por el NameNode. El control de datos es por las señales de *Heartbeat* con la lista de bloques desde el datanode, en el caso que el namenode detecta que no llega el heartbeat, entiende que el nodo esta caido y va a enviar peticiones a nodos de replica para soportar este nodo. Se puede acceder mediante un API Java o mediante un wrapper desde C. Tambien tiene una linea de comandos FS Shell.

## YARN - Yet Another Resource Negotiator

Sistema de gestor de recursos y planificación y monitorización de tareas.

Resource Manager: Scheduler y Application Manager (Gestion del sistema)
Node Manager: Es el worker, controla recursos locales del nodo y recibe las asignaciones del resourceManager, controla la gestion local.
Aplication Master: Nodo encargado de la asignacion de un aplicacion y el que se comunica con el usuario para mostrarle cosas
Container: Recurso a utilizar para ejecutar una tarea, conjunto de cores del sistema y memoria (recursos)

```
$ hadoop version
$ hdfs dfsadmin -report

$ hdfs dfs -mkdir -p /user/hadoop
$ hdfs dfs -put Desktop/vaca.txt /user/hadoop
$ hdfs dfs -rm /user/hadoop/vaca.tx

$ hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar teragen 1000 /user/hadoop/terainput
$ hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar terasort /user/hadoop/terainput /user/hadoop/teraoutput

$ hdfs dfs -ls /user/hadoop/teraoutput
Found 3 items
-rw-r--r--   1 cloudera supergroup          0 2020-10-22 03:39 /user/hadoop/teraoutput/_SUCCESS
-rw-r--r--  10 cloudera supergroup          0 2020-10-22 03:39 /user/hadoop/teraoutput/_partition.lst
-rw-r--r--   1 cloudera supergroup     100000 2020-10-22 03:39 /user/hadoop/teraoutput/part-r-00000

$ hdfs dfs -rm -r -skipTrash /user/hadoop/tera*
Deleted /user/hadoop/terainput
Deleted /user/hadoop/teraoutput

# Practica 1

$ hdfs dfs -mkdir -p /user/hadoop/txtinput
$ hdfs dfs -put Downloads/texto.txt /user/hadoop/txtinput

# Contar palabras con wordcount
# hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount <carpeta HDFS de entrada> <nueva carpeta HDFS de salida>

$ hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount /user/hadoop/txtinput /user/hadoop/txtoutput

# Cuantas veces aparece "vaca" en part-r-00000
$ hdfs dfs -cat /user/hadoop/txtoutput/part-r-00000
# 5




```

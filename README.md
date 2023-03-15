# Proyecto_final_CAMP
Código para buscar coordenadas genéticas asociadas a enfermedades de depósito lisosomal.

# 1. Instalación: dejá escritos todos los paquetes requeridos para ejecutar tu código
* El software y datos usados.

Para el correcto funcionamiento del código que se desglosará y explicará a continuación es necesario:
* Instalar la biblioteca pandas ejecutando el siguiente comando: pip3 install pandas
* La Biblioteca sys que hace parte del core de python, por lo cual ya se debería encontrar instalda, verificar ejecuntado el siguiente comando: import sys

# 2. Corrida: dejá explicitado con ejemplos cómo se debe ejecutar tu código, qué archivos entrada y de salida genera y dónde se pueden encontrar. El código que proporciones deberá ser reproducible, en caso de usar software y/o hardware específico, debes incluirlo en la documentación del código.

# 3. Finalidad del proyecto

Este proyecto tiene por objetivo compilar una base de datos donde se encuentren diferentes mutaciones asociadas a enfermedades de depóstiso lisosomal como Fabry, Pompe, Gaucher, Tay-Sachs, Mucopolisacaridosis, Sindrome de Sanfilippo, entre otras. En la actualidad el diagnóstico de este tipo de enfermedades se efectúa por NGS (secuenciación de siguiente generación) por alineamiento de las secuencias generadas con un genoma de referencia (hg38, hg37),  en donde se efectúa una comparación y mapeamiento de las variantes encontradas en los individuos.

Para el análisis de Resultados y caracterización de la variantes se deben considerar varios aspectos:
 1. Frecuencia Poblacional - de acuerdo con el patrón de herencia y la gravedad del fenotipo,
 2. Si previamente ha sido descrito en la literatura médica,
 3. El tipo de variante y mecanismo molecular, y por último,
 4. El uso de algunas herramientas como:

  - IGV Browser, que permite la visualización de la secuenciación y de posibles CNVs y breakpoints.
  - Ensembl! Browser, que suministra información detallada sobre genes, transcritos, proteínas, SNVs y SNPs, etc. y herramientas como BLAT/BLAST, VEP.
  - UniProt, que proporciona información sobre la estructura terciaria de las proteínas, sobre los diferentes dominios proteicos, entre otros.

Existen diferentes bases de datos de Mutaciones y Repositorios utilizadas:

* The Human Gene Mutation Database - HGMD R – todas las variantes ya reportadas en la literatura médica. No curada.
* Genomenom Mastermind R – Todas las variantes reportadas en la literatura, incluyendo en el material complementario.
* ClinVar – Variantes sometidas por grupos académicos y privados, y consorcios de todo el mundo, ya sea a partir de la literatura o identificadas en la práctica del día a día.
* Leiden Open Variation Database (LOVD) – Variantes presentadas por los grupos de estudio y literatura, algunas curadas, generalmente realizado por los propios investigadores.
* Bases de datos de enfermedades específicas.

La clasificación de las variantes y su significancia clínica está alineada bajo las ecomendaciones del ACMG, la cuál está categorizada de la siguiente manera:

- Benigna
- Probablemente benigna
- VUS
- Probablemente patogénica
- Patogénica

Es por esto que se construyó una base  que consigne algunas de las principales mutaciones asociadas a enfermedades de depósito lisosomal.

4. Pasos

# En primera instancia se debe importar la biblioteca pandas
import pandas as pd 

# cargar archivo CSV con la información:
# el archivo ('enfermedades.csv) fue construido por datos obtenidos de NCBI de algunas de las principales enfermedades de depósito lisosomal documentadas hasta el momento, entre ellas Fabry, Pompe, Gaucher, Tay-Sachs, Mucopolisacaridosis, Sindrome de Sanfilippo). La tabla está constutida por cuatro columnas: Coordenada genética, Gen, Enfermedad Asociada y Significancía clínica)
# En este código, la función pd.read_csv es utilizada para leer la base de datos que se construyó sobre diferentes mutaciones  asociadas a enfermedades de depósito lisosomal en formato CSV y al mismo tiempo almacenarla en un DataFrame de pandas llamado df. 
df = pd.read_csv('enfermedades.csv', sep=';') 
 
# solicitar al usuario la coordenada genética 
# La función input de la biblioteca sys es utilizada para solicitar al usuario que ingrese la coordenada genética de interés.
coordenada = input('Introduzca la coordenada genética (GRCh37): ') 
 
# buscar la coordenada en el archivo 
# La línea df.loc[df["Coordenada"] == coordenada] busca todas las filas en la base de datos df que contengan la coordenada genética que fue insertada por el usuario y las almacena en una variable llamada mutacion. Si no se encuentra ninguna mutación asociada a una enfermedad de depósito lisosomal, la variable mutacion será un DataFrame vacío.
resultado = df.loc[df['Coordenada_genetica'] == coordenada] 
 
# imprimir resultados si se encontró alguna entrada 
# Por último, el código imprime el resultado utilizando la función print. Si se encuentra una mutación asociada a una enfermedad de depósito lisosomal, el código imprime la fila de la base de datos correspondiente a la mutación. Sipor el contrario, no se encuentra ninguna mutación asociada a una enfermedad de depósito lisosomal, el código imprime un mensaje indicando que no se encontraron mutaciones asociadas con la coordenada ingresada por el usuario.
if not resultado.empty: 
    gen = resultado['Gen'].values[0] 
    print(gen)
    significancia = resultado['Significancia_clinica'].values[0] 
    enfermedad = resultado['Enfermedad_asociada'].values[0] 
    print(f'La coordenada genética {coordenada} está relacionada con la enfermedad {enfermedad},causada por el gen {gen} con una significancia clínica de {significancia}.') 
else: 
    print(f'La coordenada genética {coordenada} no está relacionada con ninguna enfermedad de depósito lisosomal.')
    
  # Si la coordenada genética se encuentra en el archivo arrojará a cuál enfermedad está asoaciada la coordenada y su significancia clínica.

depósito lisosomal


5. Conclusiones y resultados.


Es importante tener en cuenta que una limitante de esta aproximación es que es ecesario contar con una base de datos que se esté actualizando de manera permanentede las mutaciones asociadas con enfermedades de depóstivo lisisosomal para obtener resultados precisos, ya que se han descrito innumerables.



    - Finalidad que persigue tu proyecto o el problema que quieres resolver.
    - Describir los pasos para solucionar el problema (código y comentarios).
    - Indicar el software y bases de datos específicos del área utilizados y por qué.
    - Resume los resultados que obtuviste explicando si tu aproximación fue adecuada o no. En esta sección de la documentación que incluya las conclusiones y observaciones que pudiste hacer gracias a este análisis
    - 
6. El código que proporciones deberá contar con una licencia de tipo Creative Commons Zero de modo que tu código, si bien es abierto, está protegido y cuentas con atribución intelectual.
7. 
8. Usa datos públicos, disponibles en bases de datos abiertas como GenBank, SRA, UniProt, etc. Es indispensable que indiques en el código o en la documentación los números de acceso de los datos que empleaste. Alternativamente, puedes usar datos que estén depositados en repositorios como FigShare, indicando el Digital Object Identifier en tu código o en la documentación.




















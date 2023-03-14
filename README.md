# Proyecto_final_CAMP
Código para buscar coordenadas genéticas asociadas a enfermedades de depósito lisosomal

print (f'La coordenada genética (coordenada) está relacionada con la enfermedad (ent



# el archivo (enfermedades.csv) fue construido por datos obtenidos de NCBI de al momento, entre ellas: Fabry, Pompe, Gaucher, Tay-Sachs, Mucopolysaccharidosis, San

Enfermedad Asociada y Significancía clínica)

df = pd.read_csv('enfermedades.csv', sep=';')

# solicitar al usuario la coordenada genética

coordenada = input('Introduzca la coordenada genética (GRCh37): ')

#buscar la coordenada en el archivo

=resultado= df.loc[df['Coordenada genetica'] == coordenada]

#imprimir resultados si se encontró alguna entrada

if not resultado.empty:

gen = resultado['Gen'].values[0] print(gen)

significancia resultadol Significancia clinica).values[0]

enfermedad = resultado "Enfermedad asociada').values[0]

(significancia).")

else:

print("La coordenada genética (coordenada) no está relacionada con ninguna enfermed

Si la coordenada genética se encuentra en el archivo arrojará a cuál enfermedad está a

depósito lisosomal

Finalidad que persigue tu proyecto o el problema que quieres resolver.

Describir los pasos para solucionar el problema (código y comentarios).

Indicar el software y bases de datos especificos del area utilizados y por qué.
Resume los resultados que obtuviste explicando si tu aproximación fue adecuada o no. En

que pudiste hacer gracias a este analisis




proporciones deberá ser reproducible, en caso de usar software y/o hardware especifico, debes incluirlo en la documentación del código.

3. Finalidad del proyecto

Este proyecto tiene por objetivo compilar una base de datos donde se encuentren diferentes mutaciones asociadas a enfermedades de depóstiso lisosomal como Fabry, Pompe, Gaucher, Tay-Sachs, Mucopolisacaridosis, Sindrome de Sanfilippo, entre otras. En la actualidad el diagnóstico de este tipo de enfermedades se efectúa por NGS (secuenciación de siguiente generación) por alineamiento de las secuencias generadas con un genoma de referencia (ng37, en donde se efectúa una comparación y mapeamiento de las variantes encontradas en los individuos.

4. Pasos

En primera instancia se debe importar la biblioteca pandas.

import pandas as pd


# cargar archivo CSV con la información:

# el archivo ('enfermedades.csv) fue construido por datos obtenidos de NCBI de algunas de las principales enfermedades de depósito lisosomal documentadas hasta el momento, entre ellas Fabry, Pompe, Gaucher, Tay-Sachs, Mucopolisacaridosis, Sindrome de Sanfilippo)



mapeamiento de las variantes encontradas en los individuos. Para el análisis de resultados y caracterización de las variantes

1. La frecuencia poblacional - de acuerdo con el patrón de herencia, la gravedad del fenotipo,

2. Si previamente ha sido descrito en la literatura médica,

3. El tipo de variante y mecanismo molecular, y por último,

4. El uso de algunas herramientas como:

- IGV Browser (Visualización de la secuenciación y de posibles CNVs y breakpoints), 
- Ensembl! Browser (Información detallada sobre genes, transcritos, proteínas, SNVs y SNPs, etc. y herramientas como BLAT/BLAST,
UniProt (Información sobre la estructura terciaria de las proteinas, sobre los diferentes dominios proteicos, entre otros.

La clasificación de la variantes alineados a las recomendaciones del ACMG para la clasificación de variantes se divide en:

Benigna

Probablemente benigna

VUS

Probablemente patogénica

Patogénica

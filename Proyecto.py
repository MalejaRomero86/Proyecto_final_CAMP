
import pandas as pd

# cargar archivo CSV con la información
df = pd.read_csv('enfermedades.csv', sep=';')

# pedir al usuario la coordenada genética
coordenada = input('Introduzca la coordenada genética (GRCh37): ')

# buscar la coordenada en el archivo
resultado = df.loc[df['Coordenada_genetica'] == coordenada]

# imprimir resultados si se encontró alguna entrada
if not resultado.empty:
    gen = resultado['Gen'].values[0]
    print(gen)
    significancia = resultado['Significancia_clinica'].values[0]
    enfermedad = resultado['Enfermedad_asociada'].values[0]
    print(f'La coordenada genética {coordenada} está relacionada con la enfermedad {enfermedad}, causada por alteraciones en el gen {gen} y su significancia clínica es {significancia}.')
else:
    print(f'La coordenada genética {coordenada} no está relacionada con ninguna enfermedad de depósito lisosomal.')
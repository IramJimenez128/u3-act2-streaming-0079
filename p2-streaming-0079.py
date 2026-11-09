import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Iram Jimenez NC = 0079
# Creamos nuestra tabla de plataformas de streaming
# Tenemos 5 listas con 4 elementos por lista
nfx = ['Netflix', 260, False, 2007]
dis = ['Disney+', 150, False, 2019]
spn = ['Spotify', 602, True, 2008]
ytb = ['YouTube Premium', 100, True, 2014]
hbo = ['Max', 95, False, 2020]

# Creamos la lista de listas (Conformando tabla)
lista_streaming = [nfx, dis, spn, ytb, hbo]

# Utilizar pandas para organizar la tabla (DataFrame)
df_streaming = pd.DataFrame(lista_streaming,
                            columns = ["Plataforma", "Suscriptores_Millones", "Opcion_Gratis", "Lanzamiento"])
print(df_streaming)

# Creamos el archivo CSV y lo guardamos
df_streaming.to_csv("streaming.csv", index=False)

# 1. Crear gráfica de líneas
plt.plot(df_streaming["Plataforma"], df_streaming["Suscriptores_Millones"])
plt.title("Gráfica Plataformas de Streaming")
plt.xlabel("Plataforma")
plt.ylabel("Suscriptores (Millones)")
plt.show()

# 2. Creamos una gráfica de puntos (Scatter)
plt.scatter(df_streaming["Plataforma"], df_streaming["Suscriptores_Millones"])
plt.title("Dispersión de Suscriptores")
plt.xlabel("Plataforma")
plt.ylabel("Suscriptores (Millones)")
plt.show()

# 3. Gráfica de barras
plt.bar(df_streaming["Plataforma"], df_streaming["Suscriptores_Millones"])
plt.title("Distribución de Suscriptores por Plataforma")
plt.xlabel("Plataforma")
plt.ylabel("Número de Suscriptores (Millones)")
plt.show()

# 4. Ordenar gráfica de barras de manera descendente
df_str_ordenar = df_streaming.sort_values("Suscriptores_Millones", ascending=False)
plt.bar(df_str_ordenar["Plataforma"], df_str_ordenar["Suscriptores_Millones"])
plt.title("Suscriptores por Plataforma (Orden Descendente)")
plt.xlabel("Plataforma")
plt.ylabel("Número de Suscriptores (Millones)")
plt.show()

# 5. Coloreando la gráfica de barras
plt.bar(df_str_ordenar["Plataforma"], df_str_ordenar["Suscriptores_Millones"],
        color=["b", "g", "c", "m", "y"])
plt.title("Suscriptores por Plataforma (Con Color)")
plt.xlabel("Plataforma")
plt.ylabel("Número de Suscriptores (Millones)")
plt.show()

# 6. Gráfica de pastel
plt.pie(df_streaming["Suscriptores_Millones"], labels=df_streaming["Plataforma"], autopct='%1.1f%%')
plt.title("Porcentaje de Suscriptores por Plataforma")
plt.show()
print("Iram Jimenez NC = 0079")
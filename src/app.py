#Paso 3: Variables de entorno
import os
from dotenv import load_dotenv
import spotipy
from spotipy import SpotifyClientCredentials
import matplotlib.pyplot as plt


load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")


# Paso 4: Inicializar la biblioteca Spotipy
# Configurar las credenciales del cliente de Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#Paso 5: Realizar solicitudes a la API
# Buscar el ID del artista
artist_id = '3pGly9FAB9GLVX1wkNTXoP'

# Obtener el top 10 de canciones del artista
results = sp.artist_top_tracks(artist_id)
#print(results)


# Extraer información relevante de las canciones
songs = []
for track in results['tracks'][:3]:
    song = {
        'Nombre': track['name'],
        'Popularidad': track['popularity'],
        'Duración (minutos)': track['duration_ms'] / 60000
    }
    songs.append(song)


#Paso 6: Transformar a Pandas DataFrame
import pandas as pd

df = pd.DataFrame(songs)

# Ordenar las canciones por popularidad creciente
df = df.sort_values('Popularidad', ascending = False)

# Mostrar el top 3
top_3 = df.head(3)
print(top_3)


# Paso 7: Analizar relación estadística
import seaborn as sns

sns.scatterplot(data=df, x='Duración (minutos)', y='Popularidad', color='green')
plt.title('Relación entre duración y popularidad de las canciones')

# Save the scatter plot as an image
plt.savefig('/workspaces/012-PROYECTO1-interacting-with-the-twitter-api-project-tutorial/assets/scatter_plot_sinkope.png')


''''''


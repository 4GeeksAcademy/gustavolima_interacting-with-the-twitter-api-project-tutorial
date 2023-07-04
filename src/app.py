import os
from dotenv import load_dotenv
import pandas as pd
import spotipy

# Connect to Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Load the .env
load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

# Establish connection to Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = client_id,
                                                              client_secret = client_secret))


# Query into Spotify
# Select an Artist
artist_id = '4RNK7DL34RKDzb24yksnGJ'

# Query and save results to a variable
query = sp.artist_top_tracks(artist_id)
top_tracks = query['tracks']

# Create a list to store the track information
track_info = []

# Iterate over the top tracks and extract the desired information
for track in top_tracks:
    track_name = track['name']
    track_popularity = track['popularity']
    track_duration_ms = track['duration_ms']
    track_duration_min = round(track_duration_ms / 60000, 2) 
    track_info.append({
        'name': track_name,
        'popularity': track_popularity,
        'duration_min': track_duration_min
    })

# Transform the Data

# Convert the tracks_info Dict to a DF
tracksdf = pd.DataFrame.from_records(track_info)

# Sort by Popularity
tracksdf.sort_values(['popularity'], inplace=True)

# Print the top 3
tracksdf.head(3)

# Plot a scatter with Seaborn to check relations
import seaborn as sns
import matplotlib.pyplot as plt

# Create a scatter plot using seaborn
sns.scatterplot(data=tracksdf, x='duration_min', y='popularity')

# Set the plot labels and title
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')
plt.title('Duration vs. Popularity of Songs')

# Display the plot
plt.show()

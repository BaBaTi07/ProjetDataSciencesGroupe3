import os
import django
import pandas as pd

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AidePourTous.settings")
django.setup()

from app.models import Etablissement

df = pd.read_excel('..\Data\liste-des-etablissement-pour-aines-en-wallonie.xlsx')

# Split the 'Coordonnées' column into 'latitude' and 'longitude'
df[['latitude', 'longitude']] = df['Coordonnées'].str.split(',', expand=True)

# Convert the columns to float
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)

for index, row in df.iterrows():
    Etablissement.objects.create(
        spw_id=row['SPW ID'],
        type_etablissement=row['Type d\'établissement'],
        implementation=row['Implémentation'],
        nom_etablissement=row['Nom de l\'établissement'],
        latitude=row['latitude'],
        longitude=row['longitude'],
        # Ajoutez d'autres champs selon vos besoins...
    )
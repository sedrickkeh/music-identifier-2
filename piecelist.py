import os 
import random

my_list = ["Bach", "Beethoven", "Chopin", "Debussy", "Dvořák", "Elgar", "Grieg", "Handel", "Haydn", "Liszt", "Mendelssohn", "Mozart", "Mussorgsky", "Rachmaninoff", "Saint-Saëns", "Schubert", "Schumann", "Strauss", "Tchaikovsky"]
piecelist = []
data_dir = "./data"
for subdir, dirs, files in os.walk(data_dir):
    for file in files:
        composer = subdir.split('/')[-1]
        if composer not in my_list: continue
        piecepath = os.path.join(subdir, file)
        composer = piecepath.split('/')[2]
        piecename = ",".join(piecepath.split('/')[-1].split(',')[2:-1]).strip()
        piecelist.append((piecepath, composer, piecename))
random.shuffle(piecelist)

def get_piece():
    random.shuffle(piecelist)
    return random.choice(piecelist)

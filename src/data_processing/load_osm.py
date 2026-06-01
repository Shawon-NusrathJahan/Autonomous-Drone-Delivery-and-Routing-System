import osmnx as ox

def load_osm(path):
    return ox.load_graphml(path)
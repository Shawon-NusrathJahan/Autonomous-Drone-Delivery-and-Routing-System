import osmnx as ox        # downloads and processes OpenStreetMap data
import networkx as nx     # stores the graph of roads/paths
import os                 # for creating folders and building file paths

def load_chittagong_graph(
    place_name="Chittagong, Bangladesh",
    network_type="all",        # "all" includes roads AND footpaths (drones can fly over both)
    cache_folder="../data/osm/"
):
    """
    Downloads the road/path network for Chittagong from OpenStreetMap
    and saves it as a .graphml file so we don't have to re-download it.
    
    A graph has two components:
    - Nodes: intersections or points on the map
    - Edges: the road segments connecting them
    
    For drone delivery, we use this graph to:
    - Find the shortest path between a depot and a delivery point
    - Calculate real-world distances (not straight lines)
    - Later: add obstacle layers on top of this base graph
    
    Returns:
        G: a NetworkX graph object representing Chittagong's road network
    """
    
    # Create cache folder if it doesn't exist
    os.makedirs(cache_folder, exist_ok=True)
    
    # Build a safe filename from the place name
    # "Chittagong, Bangladesh" → "Chittagong_Bangladesh.graphml"
    safe_name = place_name.replace(", ", "_").replace(" ", "_")
    cache_path = os.path.join(cache_folder, f"{safe_name}.graphml")
    
    # --- Check if we already have the file cached ---
    # This is important: downloading from OSM can take 30–60 seconds.
    # If we already saved the file, we load it instantly from disk instead.
    if os.path.exists(cache_path):
        print(f"Loading cached graph from: {cache_path}")
        G = ox.load_graphml(cache_path)
    else:
        print(f"Downloading graph for: {place_name}")
        print("This may take 30–90 seconds depending on your internet speed...")
        
        # ox.graph_from_place downloads the entire road network for that place.
        # network_type="all" means roads, footpaths, cycleways — everything.
        G = ox.graph_from_place(place_name, network_type=network_type)
        
        # Save to disk so we never need to download again
        ox.save_graphml(G, cache_path)
        print(f"Graph saved to: {cache_path}")
    
    return G


def get_graph_stats(G):
    """
    Returns a summary of the graph's key properties.
    This is your evidence that the graph loaded correctly.
    """
    stats = {
        'num_nodes':       G.number_of_nodes(),   # intersections / decision points
        'num_edges':       G.number_of_edges(),   # road segments
        'is_directed':     nx.is_directed(G),     # True = one-way streets modelled
        'is_connected':    nx.is_weakly_connected(G),  # True = all nodes reachable
        'avg_node_degree': sum(dict(G.degree()).values()) / G.number_of_nodes()
    }
    return stats
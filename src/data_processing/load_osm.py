import osmnx as ox
import networkx as nx
import os

def load_chittagong_graph(
    place_name="Chittagong, Bangladesh",
    network_type="all",
    cache_folder="../datasets/osm/"
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

    # Create the graphml output folder if it doesn't exist yet
    os.makedirs(cache_folder, exist_ok=True)

    # Also create and set the osmnx HTTP cache folder.
    # osmnx saves raw API responses here so it doesn't re-request the same
    # data from the internet. We put it INSIDE datasets/osm/ so everything
    # related to OSM stays in one place and avoids the notebooks/cache/ error.
    http_cache = os.path.join(cache_folder, "http_cache")
    os.makedirs(http_cache, exist_ok=True)

    # IMPORTANT: set osmnx settings BEFORE any osmnx function is called.
    # If you set these after, osmnx has already tried to use the wrong folder.
    ox.settings.cache_folder = http_cache
    ox.settings.use_cache = True

    # Build a safe filename from the place name.
    # "Chittagong, Bangladesh" becomes "Chittagong_Bangladesh.graphml"
    safe_name = place_name.replace(", ", "_").replace(" ", "_")
    graphml_path = os.path.join(cache_folder, f"{safe_name}.graphml")

    # If we already downloaded and saved the graph before, load it from disk.
    # This avoids a 30-90 second download every time you run the notebook.
    if os.path.exists(graphml_path):
        print(f"Loading cached graph from: {graphml_path}")
        G = ox.load_graphml(graphml_path)

    else:
        print(f"Downloading graph for: {place_name}")
        print("This may take 30-90 seconds depending on your internet speed...")

        # This downloads the full road + footpath network for the named place
        G = ox.graph_from_place(place_name, network_type=network_type)

        # Save it so next time this runs it loads instantly
        ox.save_graphml(G, graphml_path)
        print(f"Graph saved to: {graphml_path}")

    return G

def load_chittagong_bbox(
    cache_folder="../datasets/osm/"
):
    """
    Downloads a smaller rectangular area of central Chittagong
    using a bounding box instead of the full city boundary.

    This covers GEC Circle to Agrabad — approx 4km x 4km.
    Much faster than load_chittagong_graph() and enough for
    Week 1 demonstration and routing algorithm testing.

    Returns:
        G: a NetworkX graph object
    """
    os.makedirs(cache_folder, exist_ok=True)

    http_cache = os.path.join(cache_folder, "http_cache")
    os.makedirs(http_cache, exist_ok=True)

    ox.settings.cache_folder = http_cache
    ox.settings.use_cache = True
    ox.settings.requests_timeout = 180

    graphml_path = os.path.join(cache_folder, "chittagong_central.graphml")

    if os.path.exists(graphml_path):
        print(f"Loading cached graph from: {graphml_path}")
        G = ox.load_graphml(graphml_path)
    else:
        print("Downloading central Chittagong bounding box...")
        print("Covers GEC Circle to Agrabad — approx 4km x 4km.")
        print("Should complete in 30-60 seconds...")

        north = 22.390
        south = 22.320
        east  = 91.840
        west  = 91.790

        G = ox.graph_from_bbox(
            north, south, east, west,
            network_type="all"
        )

        ox.save_graphml(G, graphml_path)
        print(f"Graph saved to: {graphml_path}")

    return G

def get_graph_stats(G):
    """
    Returns a dictionary summarising the graph's key properties.
    These numbers are your proof of evidence for Week 1.
    """
    stats = {
        'num_nodes':       G.number_of_nodes(),
        'num_edges':       G.number_of_edges(),
        'is_directed':     nx.is_directed(G),
        'is_connected':    nx.is_weakly_connected(G),
        'avg_node_degree': round(
            sum(dict(G.degree()).values()) / G.number_of_nodes(), 2
        )
    }
    return stats


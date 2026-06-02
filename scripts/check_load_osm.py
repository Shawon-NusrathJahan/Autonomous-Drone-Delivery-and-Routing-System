import sys, os, traceback
sys.path.insert(0, os.path.abspath('src'))
try:
    from data_processing.load_osm import load_chittagong_bbox
    print('Imported load_chittagong_bbox')
    G = load_chittagong_bbox(cache_folder='datasets/osm/')
    print('Loaded graph, nodes=', G.number_of_nodes())
except Exception:
    print('ERROR:')
    traceback.print_exc()

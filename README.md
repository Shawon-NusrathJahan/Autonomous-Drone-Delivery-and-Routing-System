# Autonomous Drone Delivery & Routing System

## Project Overview

This project focuses on the design and development of an Autonomous Drone Delivery & Routing System for urban logistics. The system aims to optimize delivery operations through intelligent route planning, energy-aware decision-making, adaptive rerouting, and simulation-based evaluation.

The project is being developed as part of an academic research initiative and will evaluate multiple routing and optimization approaches under realistic operational constraints.

## Objectives

- Design an autonomous drone delivery framework for urban environments
- Reduce delivery time and operational energy consumption
- Support adaptive rerouting in dynamic conditions
- Evaluate different routing and optimization algorithms
- Simulate multi-drone delivery operations
- Measure system performance using defined evaluation metrics

## Datasets

The project currently utilizes the following datasets and data sources:

### MDRP-P
Multi-Drone Routing Problem benchmark dataset used for:

- Delivery locations
- Depot information
- Routing constraints
- Drone operational parameters

### OpenStreetMap (OSM)
Used to obtain real-world urban map data for:

- Road network extraction
- Geographic modeling
- Graph construction

### Synthetic Delivery Requests
Custom-generated dataset used for:

- Delivery demand simulation
- Drone assignment testing
- Routing experiments

### HetroD (Planned)
Dynamic trajectory dataset intended for:

- Obstacle simulation
- Traffic-aware routing
- Adaptive rerouting evaluation

## Project Structure

```text
Autonomous-Drone-Delivery-and-Routing-System/

├── datasets/
│   └── MDRP/
│
├── notebooks/
│   └── 01_dataset_exploration.ipynb
│
├── src/
│   ├── dataset_processing/
│   ├── routing/
│   ├── optimization/
│   ├── simulation/
│   └── evaluation/
│
├── docs/
│   ├── dataset_selection.md
│   └── project_progress_report.md
│
├── requirements.txt
├── .gitignore
└── README.md
````

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd Autonomous-Drone-Delivery-and-Routing-System
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install platform-specific dependencies first

Some geospatial packages require native C libraries and must be installed
with pre-built binaries **before** running the full requirements install.
Skip any that install cleanly without the flag — this is only a fallback.

**Windows (run these first):**
```bash
pip install rtree --only-binary :all:
pip install fiona --only-binary :all:
```

**macOS (if you hit errors):**
```bash
brew install spatialindex
pip install rtree
```

**Linux (if you hit errors):**
```bash
sudo apt-get install libspatialindex-dev
pip install rtree
```

### 4. Install all dependencies

```bash
pip install -r requirements.txt
```

### 5. Register the virtual environment as a Jupyter kernel

```bash
python -m ipykernel install --user --name=drone-delivery
```

Then when opening any `.ipynb`, select **drone-delivery** as the kernel.

### 6. Verify the geospatial setup

```bash
python -c "import osmnx as ox; print('OSMnx', ox.__version__)"
python -c "import geopandas; print('GeoPandas OK')"
```

Both lines should print without errors before running any notebooks.

## Current Status

Completed:

* Project repository setup
* GitHub integration
* Project folder structure
* MDRP-P dataset integration
* Dataset exploration notebook creation
* Documentation framework setup
* OSMnx environment setup

In Progress:

* OpenStreetMap graph extraction
* Synthetic request dataset generation
* HetroD dataset acquisition

Planned:

* A* routing implementation
* Energy-aware routing
* Genetic algorithm optimization
* Multi-drone simulation
* Performance evaluation framework

## Documentation

Detailed project documentation is available in the `docs/` directory:

* `dataset_selection.md` — Dataset selection, justification, and usage
* `project_progress_report.md` — Project development progress and milestones

## Contributors

Add team member names here.

## License

This project is developed for academic and research purposes.

```
```

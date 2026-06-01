# Dataset Selection and Justification

## Autonomous Drone Delivery & Routing System

## 1. Introduction

The Autonomous Drone Delivery & Routing System aims to develop a simulation-based framework for intelligent drone delivery operations in urban environments. The project focuses on route optimization, energy-aware navigation, multi-drone coordination, and adaptive rerouting in response to environmental changes.

To support these objectives, multiple datasets and data sources are required. No single dataset provides all information needed for routing, urban environment modeling, delivery demand generation, and obstacle simulation. Therefore, a combination of benchmark datasets, geographic data sources, and generated datasets has been selected.

This document describes the datasets chosen for the project, the reasoning behind each selection, their expected usage, and their contribution to the overall system.

# 2. Dataset Selection Strategy

The project requires four major categories of data:

1. Routing and optimization benchmark data
2. Urban environment and map data
3. Delivery demand data
4. Dynamic obstacle and movement data

The selected datasets are intended to collectively support all phases of system development, including:

* Graph construction
* Route planning
* Energy-aware optimization
* Multi-drone scheduling
* Obstacle avoidance
* Simulation-based evaluation

# 3. MDRP-P Dataset

## Dataset Category

Routing and Optimization Benchmark

## Current Status

Downloaded and integrated into the project repository.

## Purpose

The MDRP-P (Multi-Drone Routing Problem) dataset serves as the primary routing benchmark for the project.

The dataset provides structured routing instances that simulate drone delivery scenarios under operational constraints.

## Contents

The dataset typically contains:

* Depot locations
* Delivery node locations
* Customer demand information
* Drone operational constraints
* Distance information
* Energy-related constraints
* Routing benchmark instances

Example structure:

| Node ID    | X Coordinate | Y Coordinate | Demand |
| ---------- | ------------ | ------------ | ------ |
| Depot      | 0            | 0            | 0      |
| Customer 1 | 12           | 5            | 1      |
| Customer 2 | 8            | 18           | 1      |

Additional constraints may include:

* Battery capacity
* Payload capacity
* Maximum flight distance
* Service limitations

## Role in the Project

The MDRP-P dataset will be used for:

* Route optimization experiments
* A* path planning evaluation
* Energy-aware routing studies
* Genetic algorithm optimization
* Multi-drone task allocation

## Reason for Selection

The project proposal focuses heavily on routing optimization and delivery efficiency.

MDRP-P was selected because:

* It is a recognized research benchmark
* It directly supports routing algorithm evaluation
* It provides realistic operational constraints
* It enables comparison with existing academic work

## Expected Outputs

The dataset will eventually be transformed into:

* Graph representations
* Delivery node networks
* Optimization problem instances
* Scheduling scenarios

# 4. OpenStreetMap (OSM)

## Dataset Category

Urban Environment and Geographic Data

## Current Status

Integration in progress.

OSMnx has been successfully installed, but urban graph extraction is still under development.

## Purpose

OpenStreetMap provides real-world geographic information that will be used to create realistic urban simulation environments.

Unlike synthetic grid environments, OpenStreetMap allows routing algorithms to operate on actual city structures.

## Contents

OpenStreetMap contains:

* Road networks
* Intersections
* Geographic coordinates
* Building locations
* Urban infrastructure
* Transportation networks

## Selected Tool

OSMnx

OSMnx is a Python library that extracts OpenStreetMap data and converts it into graph structures suitable for network analysis and routing applications.

## Role in the Project

OpenStreetMap will be used to:

* Model the urban environment
* Construct navigation graphs
* Provide realistic spatial constraints
* Support route planning experiments
* Enable future visualization of delivery operations

## Reason for Selection

The project proposal specifically targets urban logistics.

Using OpenStreetMap provides:

* Real-world geographic realism
* Accurate road network topology
* Reproducible city-scale environments
* Compatibility with graph-based routing algorithms

## Expected Outputs

The extracted map data will eventually be converted into:

* Nodes
* Edges
* Distance weights
* Routing graphs

These outputs will become the foundation of the routing engine.

# 5. Synthetic Delivery Request Dataset

## Dataset Category

Delivery Demand Simulation

## Current Status

Under development.

Dataset schema has been designed and generation scripts are being prepared.

## Purpose

The project requires delivery requests to simulate customer demand.

Since real delivery datasets are generally proprietary and difficult to obtain, synthetic data will be generated internally.

## Planned Structure

| Field       | Description               |
| ----------- | ------------------------- |
| request_id  | Unique request identifier |
| source      | Pickup location           |
| destination | Delivery location         |
| priority    | Delivery priority         |

Example:

| request_id | source  | destination | priority |
| ---------- | ------- | ----------- | -------- |
| 1          | Depot_A | Customer_1  | High     |
| 2          | Depot_A | Customer_2  | Medium   |

## Role in the Project

The synthetic dataset will be used for:

* Delivery scheduling
* Drone assignment
* Route planning experiments
* Simulation testing
* System evaluation

## Reason for Selection

Synthetic generation provides:

* Full control over data
* Scalability
* Repeatability
* Flexible experimentation

This approach also avoids legal and availability issues associated with commercial delivery datasets.

## Expected Outputs

The generated dataset will become the primary source of delivery demand during simulation runs.

# 6. HetroD Dataset

## Dataset Category

Dynamic Obstacle and Trajectory Data

## Current Status

Access request submitted.

Awaiting approval and dataset availability.

## Purpose

The project proposal requires dynamic obstacle handling and adaptive rerouting.

HetroD was identified as a suitable source of realistic movement trajectories.

## Contents

The dataset contains:

* Vehicle trajectories
* Pedestrian trajectories
* Time-stamped movement data
* Urban mobility patterns

Example:

| Object ID | Time | X   | Y   |
| --------- | ---- | --- | --- |
| Vehicle_1 | 0    | 100 | 200 |
| Vehicle_1 | 5    | 110 | 210 |
| Vehicle_1 | 10   | 125 | 220 |

## Role in the Project

If integrated, HetroD will support:

* Dynamic obstacle simulation
* Route conflict detection
* Adaptive rerouting
* Traffic-aware navigation

## Reason for Selection

Most student projects generate random obstacles.

HetroD provides realistic movement patterns, making the simulation environment more representative of real-world conditions.

## Expected Outputs

Trajectory data may later be transformed into:

* Dynamic obstacles
* Temporary route blockages
* Moving hazard zones

These features will enhance the realism of the simulation.

# 7. Dataset Integration Overview

The datasets complement one another and support different components of the system.

| Dataset            | Purpose                                         |
| ------------------ | ----------------------------------------------- |
| MDRP-P             | Routing benchmarks and optimization constraints |
| OpenStreetMap      | Urban environment modeling                      |
| Synthetic Requests | Delivery demand generation                      |
| HetroD             | Dynamic obstacle simulation                     |

Together they provide the information required to model realistic autonomous drone delivery operations.

# 8. Future Data Processing Pipeline

The planned data pipeline is as follows:

```text
MDRP-P
    ↓
Routing Constraints

OpenStreetMap
    ↓
Urban Graph Construction

Synthetic Requests
    ↓
Delivery Demand Generation

HetroD
    ↓
Dynamic Obstacle Modeling

Combined Inputs
    ↓
Routing Engine
    ↓
Optimization Engine
    ↓
Simulation Environment
    ↓
Performance Evaluation
```

This pipeline will form the foundation of the complete Autonomous Drone Delivery & Routing System.

# 9. Conclusion

The selected dataset combination provides a balanced foundation for both theoretical routing research and realistic urban simulation.

MDRP-P supplies benchmark routing scenarios, OpenStreetMap provides geographic realism, synthetic requests generate controllable delivery demand, and HetroD offers the potential for realistic obstacle modeling.

Together, these datasets support the project's objectives of reducing delivery time, minimizing energy consumption, enabling adaptive rerouting, and evaluating autonomous drone delivery performance under realistic operational conditions.

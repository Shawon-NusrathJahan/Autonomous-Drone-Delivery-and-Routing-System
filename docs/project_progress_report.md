# Autonomous Drone Delivery & Routing System

## Project Progress Report

### Project Information

**Project Title:** Autonomous Drone Delivery & Routing System

**Project Type:** Simulation-Based Research and Development Project

**Objective:**
To design and evaluate an autonomous drone delivery system that integrates route optimization, energy-aware decision making, and dynamic obstacle handling within a realistic urban environment.

---

# 1. Initial Project Setup

## Purpose

Before implementing any routing algorithms or simulations, a structured project environment was established to support collaborative development, version control, documentation, and future scalability.

## Completed Tasks

### Project Directory Creation

A dedicated project directory was created:

```text
Autonomous-Drone-Delivery-and-Routing-System/
```

This serves as the central workspace for all project assets.

### Standardized Folder Structure

The following folders were created:

```text
datasets/
notebooks/
src/
docs/
```

### Reasoning

Each folder has a specific responsibility:

| Folder    | Purpose                                        |
| --------- | ---------------------------------------------- |
| datasets  | Stores all project datasets and generated data |
| notebooks | Exploratory analysis and experimentation       |
| src       | Main implementation code                       |
| docs      | Documentation and project records              |

This separation follows standard software engineering and data science project practices.

---

# 2. GitHub Repository Setup

## Purpose

Version control was established to support team collaboration, project backup, change tracking, and future deployment.

## Completed Tasks

### Repository Creation

A GitHub repository was created for the project.

### Repository Cloning

The repository was cloned to the local development environment.

### Git Initialization Verification

The project was successfully connected to the remote GitHub repository.

### Git Ignore Configuration

A `.gitignore` file was created.

#### Purpose

To prevent unnecessary files from being uploaded to GitHub, including:

* large datasets
* temporary files
* operating system generated files
* cache files

This keeps the repository clean and lightweight.

---

# 3. Project Documentation Setup

## Purpose

Documentation was established early to ensure project decisions, dataset selections, and progress are properly recorded.

## Completed Files

### README.md

Created to provide:

* project overview
* project structure
* installation instructions
* dataset overview
* future roadmap

### dataset_selection.md

Created to document:

* selected datasets
* dataset purposes
* justification for dataset choices
* expected use within the project

### project_progress_report.md

Created to maintain a chronological record of project development activities.

---

# 4. Source Code Architecture Planning

## Purpose

The source directory structure was planned before implementation to encourage modular development.

## Created Structure

```text
src/

├── data_processing/
├── routing/
├── optimization/
├── simulation/
└── evaluation/
```

## Reasoning

### data_processing

Responsible for:

* loading datasets
* cleaning datasets
* transforming data formats

### routing

Responsible for:

* A* algorithm
* shortest path computation
* route generation

### optimization

Responsible for:

* genetic algorithms
* multi-objective optimization
* energy-aware route optimization

### simulation

Responsible for:

* drone behavior
* environment modeling
* delivery execution

### evaluation

Responsible for:

* performance metrics
* comparative analysis
* experiment results

This modular structure allows independent development of each subsystem.

---

# 5. Dataset Selection Process

## Objective

To identify datasets capable of supporting:

* route optimization
* urban environment modeling
* delivery request generation
* future dynamic obstacle simulation

After reviewing multiple alternatives, the following datasets were selected.

---

# 6. MDRP-P Dataset Integration

## Status

Completed

## Purpose

The MDRP-P benchmark dataset was selected as the primary routing benchmark.

## Dataset Contents

The dataset contains:

* delivery locations
* depot locations
* routing constraints
* drone operational constraints
* optimization benchmark instances

## Reason for Selection

The project proposal focuses heavily on:

* route optimization
* energy-aware routing
* multi-drone scheduling

MDRP-P directly supports these objectives.

## Work Completed

* Dataset downloaded successfully
* Dataset stored in the project dataset directory
* Dataset available for future processing and routing experiments

Current status:

```text
Completed and available for use
```

---

# 7. OpenStreetMap Integration

## Status

In Progress

## Purpose

To obtain realistic urban environment data for route planning and simulation.

## Selected Technology

OSMnx library was selected.

Reason:

OSMnx allows direct extraction of OpenStreetMap road networks and converts them into graph structures suitable for routing algorithms.

## Work Completed

* OSMnx installed successfully
* Dependency installation verified
* Initial map extraction experiments performed

## Current Status

Map extraction has not yet been completed successfully.

The team is currently investigating:

* OSMnx API behavior
* bounding box extraction methods
* location query formats

Current status:

```text
In Progress
```

---

# 8. Synthetic Delivery Request Dataset

## Status

Under Development

## Purpose

To simulate delivery demand within the routing system.

## Reason for Selection

Real-world delivery datasets are often:

* proprietary
* incomplete
* difficult to obtain

Generating synthetic requests provides:

* complete control
* repeatability
* scalability

## Planned Dataset Fields

| Field       | Description               |
| ----------- | ------------------------- |
| request_id  | Unique request identifier |
| source      | Delivery origin           |
| destination | Delivery destination      |
| priority    | Delivery priority level   |

## Work Completed

* Dataset schema designed
* Request generation strategy defined
* Initial generation code prepared

Current status:

```text
Under Construction
```

---

# 9. HetroD Dataset Acquisition

## Status

Pending

## Purpose

To support future dynamic obstacle simulation.

## Intended Use

The dataset will provide:

* vehicle trajectories
* pedestrian trajectories
* movement patterns

These can later be converted into:

* dynamic obstacles
* route conflicts
* rerouting events

## Work Completed

* Dataset identified and evaluated
* Access request submitted to dataset providers

Current status:

```text
Awaiting dataset access
```

---

# 10. Notebook Development

## Purpose

To separate experimentation and dataset exploration from production code.

## Created Notebook

### 01_dataset_exploration.ipynb

Purpose:

* inspect datasets
* validate dataset loading
* test OpenStreetMap extraction
* verify future preprocessing workflows

This notebook serves as the primary exploratory workspace during the early project phases.

---

# 11. Current Project Status

## Completed

* Project structure established
* GitHub repository configured
* Version control operational
* Documentation framework created
* MDRP-P dataset acquired
* OSMnx installed and configured
* Dataset strategy finalized
* Notebook environment prepared

## In Progress

* OpenStreetMap extraction
* Synthetic request generation

## Pending

* HetroD acquisition
* Dataset preprocessing
* Graph construction
* A* implementation
* Energy-aware routing
* Genetic algorithm optimization
* Simulation environment development
* Evaluation framework

---

# Next Immediate Objectives

1. Complete OpenStreetMap graph extraction.
2. Generate synthetic delivery request dataset.
3. Create data processing scripts.
4. Convert datasets into graph representations.
5. Begin A* routing implementation.
6. Prepare routing evaluation metrics.

---

# Summary

The project foundation has been successfully established through repository setup, documentation creation, architectural planning, and acquisition of the primary routing benchmark dataset (MDRP-P). The current focus is on completing urban environment acquisition through OpenStreetMap and constructing the synthetic delivery request dataset that will support routing and simulation experiments in subsequent development phases.

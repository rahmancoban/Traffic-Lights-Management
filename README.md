# Traffic Lights Management

## Table of Contents

- [Overview](#Overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contact](#contact)

## Overview

The Traffic Lights Management project is a multi-agent simulation designed to model and manage traffic flow within a city grid. This project utilizes the Mesa framework to create, manage, and visualize agents representing traffic lights and vehicles. The primary objective is to optimize traffic flow, reduce congestion, and ensure vehicles adhere to traffic light signals.

## Features

- **TrafficLight Agents**: Control traffic flow at intersections by changing states between RED and GREEN.
- **Vehicle Agents**: Represent individual vehicles moving within the grid, stopping at red lights, and avoiding collisions with other vehicles.
- **Custom Scheduler**: Activates agents based on their type (traffic lights and vehicles).
- **Simulation Visualization**: Provides a visual representation of traffic lights and vehicle movements within the grid.

## Installation

### Prerequisites

- Python 3.6 or higher
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/Traffic-Lights-Management.git
   cd Traffic-Lights-Management
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv traffic_env
   source traffic_env/bin/activate  # On Windows use `traffic_env\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Usage**:

   ```sh
   python run.py
   ```

5. **Open the Browser**:

   ```sh
   Navigate to http://127.0.0.1:8521 to see the simulation in action.
   ```

## Project Structure

```
Traffic-Lights-Management/
├── traffic/
│   ├── __init__.py
│   ├── agents.py
│   ├── schedule.py
│   └── server.py
├── traffic_model.py
├── requirements.txt
├── run.py
└── README.md
```

- traffic/agents.py: Defines the TrafficLight and Vehicle agents with their attributes and behaviors.
- traffic/schedule.py: Implements a custom scheduler (RandomActivationByType) for agent activation.
- traffic/server.py: Sets up the visualization and server for running the simulation in a browser.
- traffic_model.py: Defines the TrafficModel class, setting up the grid and managing agents.
- run.py: Main entry point to start the simulation server.
- requirements.txt: List of dependencies required for the project.
- README.md: This file.clear

## Contact

- **Abdurrahman Coban** - [abnncbnn@gmail.com](mailto:abnncbnn@gmail.com)
- GitHub: [https://github.com/rahmancoban](https://github.comrahmancoban)

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import Slider
from traffic_model import TrafficModel
from traffic.agents import TrafficLight, Vehicle

def agent_portrayal(agent):
    """
    Define how agents are portrayed in the visualization.
    """
    if isinstance(agent, TrafficLight):
        portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
        portrayal["Color"] = "green" if agent.state == "GREEN" else "red"
    elif isinstance(agent, Vehicle):
        portrayal = {"Shape": "arrowHead", "scale": 0.5, "Filled": "true", "Color": "blue", "Layer": 1}
        if agent.direction == "N":
            portrayal["heading_x"] = 0
            portrayal["heading_y"] = 1
        elif agent.direction == "S":
            portrayal["heading_x"] = 0
            portrayal["heading_y"] = -1
        elif agent.direction == "E":
            portrayal["heading_x"] = 1
            portrayal["heading_y"] = 0
        elif agent.direction == "W":
            portrayal["heading_x"] = -1
            portrayal["heading_y"] = 0
    return portrayal

# Create a grid to visualize the agents
grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)

# Create a ModularServer to manage the simulation and visualization
server = ModularServer(
    TrafficModel,
    [grid],
    "Traffic Management Model",
    {
        "width": 20,
        "height": 20,
        "num_vehicles": Slider("Number of vehicles", 10, 1, 40, 1)  # Max number of cars set to 40
    }
)

server.port = 8521  # The default port for the server

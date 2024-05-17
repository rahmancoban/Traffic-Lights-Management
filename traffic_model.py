from mesa import Model
from mesa.space import MultiGrid
from traffic.agents import TrafficLight, Vehicle
from traffic.schedule import RandomActivationByType
import random  # Import the random module for random initialization

class TrafficModel(Model):
    """
    TrafficModel is the main model class that defines the grid, creates agents, 
    and manages the simulation steps.
    """
    def __init__(self, width=20, height=20, num_vehicles=40):
        super().__init__()
        self.grid = MultiGrid(width, height, True)  # Create a grid with wrapping edges
        self.schedule = RandomActivationByType(self)  # Custom scheduler to handle agent activation
        self.num_vehicles = num_vehicles
        
        # Create traffic lights and vehicles
        self.create_traffic_lights()
        self.create_vehicles()
        
        self.running = True

    def create_traffic_lights(self):
        """
        Create traffic lights at specified positions with random initial states.
        """
        traffic_light_positions = [
            (5, 5), (5, 15), (15, 5), (15, 15),
            (10, 10), (10, 15), (15, 10), (5, 10),
            (10, 5)
        ]
        
        for pos in traffic_light_positions:
            initial_state = "GREEN" if random.random() < 0.5 else "RED"
            traffic_light = TrafficLight(self.next_id(), self, initial_state)
            self.grid.place_agent(traffic_light, pos)
            self.schedule.add(traffic_light)

    def create_vehicles(self):
        """
        Create a specified number of vehicles at random positions in the grid.
        """
        for i in range(self.num_vehicles):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            vehicle = Vehicle(self.next_id(), self)
            self.grid.place_agent(vehicle, (x, y))
            self.schedule.add(vehicle)

    def step(self):
        """
        Advance the model by one step.
        """
        self.schedule.step()

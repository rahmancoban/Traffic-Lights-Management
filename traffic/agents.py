from mesa import Agent
import random

class TrafficLight(Agent):
    """
    TrafficLight agent controls traffic flow at intersections by switching
    states between RED and GREEN at regular intervals.
    """
    def __init__(self, unique_id, model, initial_state="RED"):
        super().__init__(unique_id, model)
        self.state = initial_state  # Initial state of the traffic light
        self.counter = 0
        self.time_to_change = 10  # Number of steps before changing state

    def step(self):
        """
        Update the state of the traffic light after a certain number of steps.
        """
        self.counter += 1
        if self.counter >= self.time_to_change:
            self.state = "GREEN" if self.state == "RED" else "RED"
            self.counter = 0
        print(f"TrafficLight {self.unique_id}: State={self.state}, Counter={self.counter}")

class Vehicle(Agent):
    """
    Vehicle agent represents individual vehicles moving within the grid.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.direction = random.choice(["N", "S", "E", "W"])  # Initial direction of the vehicle
        self.waiting = False  # Track if the vehicle is waiting

    def step(self):
        """
        Move the vehicle in the current direction if possible, otherwise change direction.
        """
        current_pos = self.pos

        # Check if the vehicle can move in the current direction
        if self.can_move(current_pos):
            new_position = self.get_new_position(current_pos)
            self.model.grid.move_agent(self, new_position)
            self.waiting = False  # Vehicle is not waiting after moving
        else:
            # If it cannot move because of red light or vehicle, stay in place
            if not self.is_waiting_at_red_light() and not self.is_waiting_behind_vehicle():
                # Change direction and find a new valid position
                self.change_direction()
                new_position = self.get_new_position(current_pos)
                if self.can_move(new_position):
                    self.model.grid.move_agent(self, new_position)
                    self.waiting = False  # Vehicle is not waiting after moving
            else:
                self.waiting = True  # Vehicle is waiting

    def can_move(self, pos):
        """
        Check if the vehicle can move to the next position.
        """
        next_pos = self.get_new_position(pos)

        if self.model.grid.out_of_bounds(next_pos):
            return False

        # Check for traffic light or vehicle directly in the path
        contents = self.model.grid.get_cell_list_contents([next_pos])
        for item in contents:
            if isinstance(item, TrafficLight) and item.state == "RED":
                return False
            if isinstance(item, Vehicle):
                return False

        return True

    def is_waiting_at_red_light(self):
        """
        Check if the vehicle is waiting at a red light.
        """
        current_pos = self.pos
        next_pos = self.get_new_position(current_pos)

        if self.model.grid.out_of_bounds(next_pos):
            return False

        contents = self.model.grid.get_cell_list_contents([next_pos])
        for item in contents:
            if isinstance(item, TrafficLight) and item.state == "RED":
                return True
        return False

    def is_waiting_behind_vehicle(self):
        """
        Check if the vehicle is waiting behind another vehicle that is waiting at a red light.
        """
        current_pos = self.pos
        next_pos = self.get_new_position(current_pos)

        if self.model.grid.out_of_bounds(next_pos):
            return False

        contents = self.model.grid.get_cell_list_contents([next_pos])
        for item in contents:
            if isinstance(item, Vehicle):
                # Check if the vehicle ahead is waiting
                if item.waiting:
                    return True
        return False

    def get_new_position(self, current_pos):
        """
        Calculate the next position based on the current direction.
        """
        if self.direction == "N":
            return (current_pos[0], current_pos[1] + 1)
        elif self.direction == "S":
            return (current_pos[0], current_pos[1] - 1)
        elif self.direction == "E":
            return (current_pos[0] + 1, current_pos[1])
        elif self.direction == "W":
            return (current_pos[0] - 1, current_pos[1])

    def change_direction(self):
        """
        Change the vehicle's direction to a new random direction.
        """
        new_direction = random.choice(["N", "S", "E", "W"])
        while new_direction == self.direction:
            new_direction = random.choice(["N", "S", "E", "W"])
        self.direction = new_direction

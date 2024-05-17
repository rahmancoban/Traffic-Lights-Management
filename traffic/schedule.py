from mesa.time import RandomActivation

class RandomActivationByType(RandomActivation):
    """
    A scheduler that allows activating agents by their type. This is a subclass of Mesa's RandomActivation
    scheduler that provides additional functionality to activate agents based on their type.
    """
    def __init__(self, model):
        """
        Initialize the scheduler.
        
        Args:
            model: The model instance this scheduler belongs to.
        """
        super().__init__(model)
        self.agents_by_type = {}  # Dictionary to keep track of agents by their type

    def add(self, agent):
        """
        Add an agent to the schedule.
        
        Args:
            agent: An agent to be added to the scheduler.
        """
        agent_type = type(agent).__name__
        if agent_type not in self.agents_by_type:
            self.agents_by_type[agent_type] = []  # Initialize a list for this type if not already present
        self.agents_by_type[agent_type].append(agent)
        super().add(agent)  # Call the parent class's add method

    def remove(self, agent):
        """
        Remove an agent from the schedule.
        
        Args:
            agent: An agent to be removed from the scheduler.
        """
        agent_type = type(agent).__name__
        if agent_type in self.agents_by_type:
            self.agents_by_type[agent_type].remove(agent)
            if not self.agents_by_type[agent_type]:  # Remove the type entry if no agents of that type remain
                del self.agents_by_type[agent_type]
        super().remove(agent)  # Call the parent class's remove method

    def step(self, by_type=True):
        """
        Execute the step of all agents, either by type or randomly.
        
        Args:
            by_type: If True, step through agents by type. Otherwise, step through all agents randomly.
        """
        if by_type:
            for agent_type in list(self.agents_by_type):
                self.step_type(agent_type)  # Step through all agents of each type
        else:
            super().step()  # Call the parent class's step method

    def step_type(self, type_class):
        """
        Step all agents of a given type.
        
        Args:
            type_class: The class of agents to be stepped.
        """
        if type_class in self.agents_by_type:
            for agent in self.agents_by_type[type_class]:
                agent.step()  # Call the step method of each agent of the specified type

import uuid

class Engine:
    def __init__(self):
        # Maps a modifyable, human readable name to a constant string identifier.
        self.namespace = {}
        self.memory = {}
        # The memory stores a "map" of how to find the value - in memory, on disk, on network, etc. with all relevant details.

    def define_value(self, value, alias=None):
        # Define a value and asigns it an optional alias. 
        reference = str(uuid.uuid4())
        if reference not in self.memory and value:
            self.memory[reference] = value
        self.namespace[alias] = reference
        return reference

    def get_memory(self, reference):
        return self.memory[reference]

    # All variables are immutable.
        
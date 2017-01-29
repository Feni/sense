class Node:
    def __init__(self):
        self.parents = []
        self.namespace = {}

class Value:
    def __init__(self):
        pass

class NotFoundException(Exception):
    pass

class Environment:
    def __init__(self):
        pass

    def run(self):
        pass

    def resolve_name(self, node, name):
        # Returns the node which contains this value
        # Skips over any cycles
        # Returns key error if the value was not found
        if name in node.namespace:
            return node
        visited = set()
        visited.add(node)
        stack = list(reversed(node.parents))
        while stack:
            parent_node = stack.pop()  # Returns the last item
            if parent_node in visited:
                continue
            visited.add(parent_node)
            if name in parent_node.namespace:
                return parent_node
            stack.extend(reversed(parent_node.parents))
        raise NotFoundException()


class Frame:
    def __init__(self):
        # The order of the parent frames determine precedence
        self.parent_frames = []
        self.namespace = {}

    def __setitem__(self, key, val):
        self.namespace[key] = val

    def __getitem__(self, key):
        # If you have circular imports this could lead to a stack overflow
        if key in self.namespace:
            return 
        
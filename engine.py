from collections import defaultdict, namedtuple

class Engine:
    def __init__(self):
        # Stores a node name to list of relations.
        # Nodes are constant names in this version. Have a different layer to map human readable names to these constants.
        # TODO: The graph should store not a list, but a map of relationType to list.
        self.graph = defaultdict(list)

    def statement(self, statement_graph):
        for node, relations in statement_graph.items():
            self.graph[node] += relations
            # Add reverse relations
            for relation, related_node in relations:
                self.graph[related_node].append( ("reverse_" + relation, node))

    def query(self, query_graph):
        response = []
        for node, relations in query_graph.items():
            if node == "UNKNOWN":
                # Backwards relation
                for relation, relation_node in relations:
                    assert relation_node != "UNKNOWN"
                    return filter(lambda x: x[0] == "reverse_" + relation, self.graph[relation_node])
            else:
                # Forward lookup
                node_relations = self.graph[node]
                for relation, relation_node in relations:
                    assert relation_node == "UNKNOWN"
                    # Then this is what we have to find.
                    return filter(lambda x: x[0] == relation, node_relations)



    def list_all(self):
        print self.graph

    
        
from collections import defaultdict, namedtuple

class Engine:
    def __init__(self):
        # Stores a node name to list of relations.
        # Nodes are constant names in this version. Have a different layer to map human readable names to these constants.
        # TODO: The graph should store not a list, but a map of relationType to list.
        self.graph = defaultdict(lambda : defaultdict(list))

    def inverse_relation(self, relation):
        if "-" in relation:
            return relation.replace("-", "")
        else:
            return "-" + relation

    def statement(self, statement_graph):
        for nodes, relations in statement_graph.items():
            if not isinstance(nodes, tuple):
                nodes = tuple([nodes])
            for node in nodes:
                for relation, related_nodes in relations.items():
                    for related_node in related_nodes:
                        self.graph[node][relation].append(related_node)
                        self.graph[related_node][self.inverse_relation(relation)].append(node)

    def query(self, query_graph):
        # Right now only supports a single unknown per query
        # Finds the closest match - implicit and of all queries.
        response = []
        for node, relations in query_graph.items():
            if node == "UNKNOWN":
                node_matches = []
                for relation, related_nodes in relations.items():
                    for related_node in related_nodes:
                        # Work backwards from the relations
                        tuple(self.graph[related_node][self.inverse_relation(relation)])
            elif related_node == "UNKNOWN":
                # Forward lookup
                return tuple(self.graph[node][relation])

    def list_all(self):
        print self.graph

    
        
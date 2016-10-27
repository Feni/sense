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
        for node, relations in statement_graph.items():
            for relation, related_nodes in relations.items():
                for related_node in related_nodes:
                    self.graph[node][relation].append(related_node)
                    self.graph[related_node][self.inverse_relation(relation)].append(node)

    def query(self, query_graph):
        response = []
        for node, relations in query_graph.items():
            for relation, related_nodes in relations.items():
                for related_node in related_nodes:
                    if node == "UNKNOWN":
                        # Work backwards from the relations
                        assert related_node != "UNKNOWN"
                        return self.graph[related_node][self.inverse_relation(relation)]
                    elif related_node == "UNKNOWN":
                        # Forward lookup
                        return self.graph[node][relation]

    def list_all(self):
        print self.graph

    
        
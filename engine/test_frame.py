from frame import *

def test_namespace_resolution():
    env = Environment()
    base_node = Node()
    parent1_node = Node()
    parent2_node = Node()
    parent2_parent_node = Node()
    parent1_parent_node = Node()
    base_node.parents = [parent1_node, parent2_node]
    parent1_node.parents = [parent1_parent_node]
    parent2_node.parents = [parent2_parent_node]
    parent2_parent_node.namespace["testkey"] = "correct_testval"
    parent2_node.namespace["testkey"] = "bredth_first_testval"
    result = env.resolve_name(base_node, "testkey")
    assert result == parent2_node

def test_direct_namespace_resolution():
    env = Environment()
    base_node = Node()
    parent1_node = Node()
    parent2_node = Node()
    parent2_parent_node = Node()
    parent1_parent_node = Node()
    base_node.parents = [parent1_node, parent2_node]
    parent1_node.parents = [parent1_parent_node]
    parent2_node.parents = [parent2_parent_node]
    base_node.namespace["testkey"] = "correct_testval"
    parent2_node.namespace["testkey"] = "bredth_first_testval"
    result = env.resolve_name(base_node, "testkey")
    assert result == base_node

test_namespace_resolution()
# test_direct_namespace_resolution()
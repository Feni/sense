from engine import Engine

def test_variables():
    engine = Engine()
    ref = engine.define_value(42, alias="hello world")
    print ref
    assert engine.get_memory(ref) == 42
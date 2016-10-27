from engine import Engine

def test_variables():
    engine = Engine()
    engine.statement({"dog": [("is", "animal")]})
    engine.statement({"dog": [("is", "mammal")]})
    engine.list_all()
    print engine.query({"dog": [("is", "UNKNOWN")]})
    print engine.query({"UNKNOWN": [("is", "mammal")]})
    # ref = engine.define_value(42, alias="hello world")
    # print ref
    # assert engine.get_memory(ref) == 42
from engine import Engine

def test_variables():
    engine = Engine()
    engine.statement({"dog": {"is": ["animal"]}})
    engine.statement({"dog": {"is": ["mammal"]}})
    engine.list_all()
    print engine.query({"dog": {"is": ["UNKNOWN"]}})
    print engine.query({"UNKNOWN": {"is": ["mammal"]} })
    # ref = engine.define_value(42, alias="hello world")
    # print ref
    # assert engine.get_memory(ref) == 42

def test_election_data():
    engine = Engine()
    engine.statement({"houston": {"typeof": ["city"]}})
    engine.statement({"austin": {"typeof": ["city"]}})
    engine.statement({"dallas": {"typeof": ["city"]}})
    engine.statement({"waco": {"typeof": ["town"]}})
    engine.statement({("city", "town"): {"typeof": ["location"]}})
    
    locations = engine.query({"UNKNOWN": {"typeof": ["location"]}})
    assert 'city' in locations and 'town' in locations

    print engine.query({"UNKNOWN": {"typeof": ["city", "town"]}})

    engine.statement({"houston": {"voted": ["democrat"]}})
    engine.statement({"austin": {"voted": ["democrat"]}})
    engine.statement({"dallas": {"voted": ["republican"]}})
    engine.statement({"waco": {"voted": ["republican"]}})
    # This does an implicit AND
    # To do "or" we need the ability to send it multiple queries and combine them before sending the results back.
    print engine.query({"UNKNOWN": {"typeof": ["city"], "voted": ["democrat"]}})
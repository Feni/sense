class SemanticEngine(dict):
    def __init__(self):
        super(SemanticEngine, self).__init__(*arg, **kw)


def ladder_match():
    env = SemanticEngine()
    # env['a']
    # env['team']
    # env['team']
    #    # (instances list)
    #    # 'a', 'b', 'c', 'd', 'e', f'
    # I want to specify that team is a 'class' of items. and then that should define a bunch of sub-types I can define.
    # while creating a copy of fields on creation is more expensive and less robust, it's the simpler solution for now, so let's go with that.
    # Expresses a ladder match between a bunch of players
    # Express what exists - the teams
    # So you need an identifier for the team (the name) and the fact that they're a team
    teams = ['a', 'b', 'c', 'd', 'e', 'f']
    # I need to express that I want to create pairs of teams
    # Let's call this generated pairs list a round
    # match
    #   [TEAM, TEAM]
    #   Schema for match has two teams as field types, but without a field value. It has an implicit name for each one.
    #   The default name is team_a, team_b
    #   Below the schema is the list of requirements
    #   team_a != team_b
    
    # Rounds also have a previous round and a next round. Just define these abstractly as 'round' object as well. 
    # Rounds have a bunch of matches (unknown number)
    # Rounds have participants which are members of these matches - one match each
    #   So define the constraint that a team should be in atleast one match and no more than one match
    #
    # What is a round? A round is a pairing up of the teams that are currently in the running
    # Okay, so teams have an attribute which defines if they're still in the running or not
    # and this attribute starts at true
    # Okay, so a round has pairings
    # round = list of pairings
    # pairing = team a and team b
    # such that team a is still in the running
    # such that team b is still in the running
    # and team a != team b since a team can't play itself
    # okay at this point I expect the system to give me a generated 'round' as a response
    # then I would ask it to proceed to generate the next round
    # The players in the next round are the winners from this round
    # express that whoever wins this round will also play in the next round
    # Then the part that leaps over existing things is for it to be able to carry this uncertain value
    # forward and generate the rest of the recursive graph knowing the initial state without knowing who won
    # That tree is the ladder for the matches
    # Okay. So now let's convert this to code
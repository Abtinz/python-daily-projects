class EqualChecker:
    def __init__(self, dfa1, dfa2):
        self.dfa1 = dfa1
        self.dfa2 = dfa2
        self.complement_dfa1 = self.complement(dfa1)
        self.complement_dfa2 = self.complement(dfa2)

    def complement(self, dfa):
        new_final_states = set(dfa['states']) - set(dfa['final_states'])
        return {
            'states': dfa['states'],
            'alphabet': dfa['alphabet'],
            'start_state': dfa['start_state'],
            'transitions': dfa['transitions'],
            'final_states': new_final_states
        }

    def product_automaton(self, dfa1, dfa2, is_intersection):
        new_states = {(s1, s2) for s1 in dfa1['states'] for s2 in dfa2['states']}
        new_start_state = (dfa1['start_state'], dfa2['start_state'])
        new_transitions = {}
        new_final_states = set()

        for (s1, s2) in new_states:
            new_transitions[(s1, s2)] = {}
            for symbol in dfa1['alphabet']:
                if symbol in dfa2['alphabet'] and symbol in dfa1['transitions'][s1] and symbol in dfa2['transitions'][s2]:
                    new_transitions[(s1, s2)][symbol] = (dfa1['transitions'][s1][symbol], dfa2['transitions'][s2][symbol])
                    if is_intersection:
                        if (s1 in dfa1['final_states'] and s2 in dfa2['final_states']):
                            new_final_states.add((s1, s2))
                    else:
                        if (s1 in dfa1['final_states'] or s2 in dfa2['final_states']):
                            new_final_states.add((s1, s2))

        return {
            'states': new_states,
            'alphabet': dfa1['alphabet'],
            'start_state': new_start_state,
            'transitions': new_transitions,
            'final_states': new_final_states
        }

    def check_equal(self):
        intersection1 = self.product_automaton(self.dfa1, self.complement_dfa2, True)
        intersection2 = self.product_automaton(self.dfa2, self.complement_dfa1, True)
        union_dfa = self.product_automaton(intersection1, intersection2, False)
        return self.is_empty_dfa(union_dfa)

    def is_empty_dfa(self, dfa):
        reachable = set()
        queue = [dfa['start_state']]
        while queue:
            state = queue.pop(0)
            if state in dfa['final_states']:
                return False
            if state not in reachable:
                reachable.add(state)
                for symbol in dfa['alphabet']:
                    if symbol in dfa['transitions'][state]:
                        queue.append(dfa['transitions'][state][symbol])
        return True
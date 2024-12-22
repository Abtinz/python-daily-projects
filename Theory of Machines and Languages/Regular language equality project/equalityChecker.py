class EqualChecker:
    def __init__(self, dfa1, dfa2):
        """
        Initializes the EqualChecker with two DFAs.
        Args:
            dfa1 (dict): The first DFA as a dictionary.
            dfa2 (dict): The second DFA as a dictionary.
        
        Upon initialization, this class also computes the complements of each DFA using the complement method.
        """
        self.dfa1 = dfa1
        self.dfa2 = dfa2
        self.complement_dfa1 = self.complement(dfa1)  # Compute complement of the first DFA
        self.complement_dfa2 = self.complement(dfa2)  # Compute complement of the second DFA

    def information(self):
        print("# Equality check------------------------------------------------------------------------------------")
        print(f"\nFirst DFA: {self.dfa1}")
        print(f"\nSecond DFA: {self.dfa2}")
        print(f"\nFirst DFA complement: {self.complement_dfa1}")
        print(f"\nSecond DFA complement: {self.complement_dfa2}")

    def complement(self, dfa):
        """
        Generates the complement of a given DFA.
        Args:
            dfa (dict): A DFA dictionary.

        Returns:
            dict: A new DFA dictionary representing the complement of the given DFA.
        """
        new_final_states = set(dfa['states']) - set(dfa['final_states'])
        return {
            'states': dfa['states'],
            'alphabet': dfa['alphabet'],
            'start_state': dfa['start_state'],
            'transitions': dfa['transitions'],
            'final_states': new_final_states
        }

    def product_automaton(self, dfa1, dfa2, is_intersection):
        """
        Constructs a product automaton from two DFAs.
        Args:
            dfa1, dfa2 (dict): The dictionaries of the two DFAs to combine.
            is_intersection (bool): Determines if the operation should compute the intersection or union.

        Returns:
            dict: A new DFA dictionary representing the product automaton.
        """
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
        """
        Determines if the two DFAs are equivalent by creating their product automaton and checking if the resulting DFA is empty.
        
        Returns:
            bool: True if the DFAs are equivalent, False otherwise.
        """
        self.information()
        intersection1 = self.product_automaton(self.dfa1, self.complement_dfa2, True)
        intersection2 = self.product_automaton(self.dfa2, self.complement_dfa1, True)
        union_dfa = self.product_automaton(intersection1, intersection2, False)
        return self.is_empty_dfa(union_dfa)

    def is_empty_dfa(self, dfa):
        """
        Checks if a DFA has any reachable final states starting from its start state.

        Args:
            dfa (dict): The DFA to check.

        Returns:
            bool: True if the DFA does not have any reachable final states, indicating an empty language.
        """
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

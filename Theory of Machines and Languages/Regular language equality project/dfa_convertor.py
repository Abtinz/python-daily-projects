from collections import deque, defaultdict

class DFAConverter:
    def __init__(self, nfa):
        self.nfa = nfa
        self.dfa_states = []
        self.dfa_start_state = None
        self.alphabet = None
        self.dfa_transitions = defaultdict(dict)
        self.dfa_final_states = set()

    def convert(self):
        self.alphabet = self.nfa.variables
        queue = deque([frozenset([self.nfa.start_variable])])
        seen = set([frozenset([self.nfa.start_variable])])
        self.dfa_start_state = frozenset([self.nfa.start_variable])

        while queue:
            current = queue.popleft()
            self.dfa_states.append(current)

            # Checking for final states in the current set
            if any(state in self.nfa.final_states for state in current):
                self.dfa_final_states.add(current)

            for terminal in self.nfa.terminals:
                next_states = set()
                for state in current:
                    try:
                
                        if terminal in self.nfa.transitions[state]:
                            next_states.update(self.nfa.transitions[state][terminal])
                    except Exception as error:
                        pass
            
                if next_states:
                    next_state_frozenset = frozenset(next_states)
                    self.dfa_transitions[current][terminal] = next_state_frozenset
                    if next_state_frozenset not in seen:
                        seen.add(next_state_frozenset)
                        queue.append(next_state_frozenset)
        self.DFA_Information()

        return {
            'states': self.dfa_states,
            'alphabet': self.alphabet,
            'start_state': self.dfa_start_state,
            'transitions': self.dfa_transitions,
            'final_states': self.dfa_final_states
        }

    def DFA_Information(self):
        print(f"DFA Start State: {self.dfa_start_state}")
        print(f"DFA States: {self.dfa_states}")
        print(f"DFA Transitions: {self.dfa_transitions}")
        print(f"DFA Final States: {self.dfa_final_states}")

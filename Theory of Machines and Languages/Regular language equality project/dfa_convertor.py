from collections import deque, defaultdict

class DFAConverter:
    def __init__(self, nfa):
        """
        Initializes the DFAConverter with an NFA.
        Args:
            nfa (object): An object representing the NFA which includes its start variable, variables, terminals,
                          transitions, and final states.
                          
        The constructor initializes several attributes used to build the DFA.
        """
        self.nfa = nfa  # The NFA to convert
        self.dfa_states = []  # List to store the states of the DFA
        self.dfa_start_state = None  # The start state of the DFA
        self.alphabet = None  # The alphabet used in the DFA, derived from NFA's variables
        self.dfa_transitions = defaultdict(dict)  # A dictionary to hold state transitions
        self.dfa_final_states = set()  # Set to hold the final states of the DFA

    def convert(self):
        """
        Converts the NFA to a DFA using the subset construction algorithm.
        
        Returns:
            dict: A dictionary representing the constructed DFA with details about its states,
                  alphabet, start state, transitions, and final states.
        """
        self.alphabet = self.nfa.variables  # Set the alphabet from the NFA's variables
        queue = deque([frozenset([self.nfa.start_variable])])  # Initialize queue with the start state
        seen = set([frozenset([self.nfa.start_variable])])  # Keep track of seen states to avoid reprocessing
        self.dfa_start_state = frozenset([self.nfa.start_variable])  # Define the start state of the DFA

        while queue:
            current = queue.popleft()  # Current composite state being processed
            self.dfa_states.append(current)  # Add current state to the list of DFA states

            # Check if the current state should be a final state
            if any(state in self.nfa.final_states for state in current):
                self.dfa_final_states.add(current)

            # Process each terminal in the NFA's alphabet
            for terminal in self.nfa.terminals:
                next_states = set()
                for state in current:
                    # Transition to next states based on the terminal
                    try:
                        if terminal in self.nfa.transitions[state]:
                            next_states.update(self.nfa.transitions[state][terminal])
                    except Exception as error:
                        # Exception handling if the transition is not defined
                        pass
            
                # If there are next states, update the DFA transitions
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
        print("# DFA Conversion Information------------------------------------------------------------------------------------")
        print(f"DFA Start State: {self.dfa_start_state}")
        print(f"DFA States: {self.dfa_states}")
        print(f"DFA Transitions: {self.dfa_transitions}")
        print(f"DFA Final States: {self.dfa_final_states}")

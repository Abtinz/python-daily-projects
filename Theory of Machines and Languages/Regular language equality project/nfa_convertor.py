
class NFAConvertor:
    def __init__(self, grammar):
        """
        Initializes the NFA converter with the given grammar.
        Args:
            grammar (dict): The grammar dictionary containing variables, terminals, productions, and a start variable.
        
        The constructor extracts all necessary components from the grammar, sets up the initial states, and
        calls the convert method to build the NFA.
        """
        self.start_variable = grammar["start_variable"]  # The start variable of the NFA
        self.variables = grammar["variables"]            # Set of non-terminal variables
        self.terminals = grammar["terminals"]            # Set of terminal symbols
        self.p = grammar["p"]                            # Dictionary of production rules
        self.states = set(grammar["variables"])          # NFA states initialized to grammar variables
        self.transitions = None                          # Placeholder for transition dictionary
        self.final_states = set()                        # Set to hold final states of the NFA
        self.nfa = self.convert()                        # Invokes the convert method to create the NFA


    def NFA_Information(self):
        print("###NFA conversion------------------------------------------------------------------------------------")
        print(f'given data: variables:{self.variables}\n terminals:{self.terminals}\n productions:{self.p}\n start_variable:{self.start_variable}\n')
        print(f'results: final_states:{self.final_states}\n transitions:{self.transitions}\n')

    def transitions_function(self):
        """
        Initializes the transitions dictionary where each state has a dictionary mapping each symbol to the resultant state(s).
        This method sets up the structure for storing the NFA transitions.
        """

        self.transitions = {state: {} for state in self.states }
         
    def convert(self):
        """
        this method will converts the given grammar into an NFA by setting up transitions based on production rules.
        it iterates through each production rule and updates the transitions and final states accordingly.
        After defining transitions and final states, it invokes NFA_Information to print the NFA details.
        """

        self.transitions_function()
        if self.transitions != None:
            for variable, rules in self.p.items():
                for rule in rules:
                    if len(rule) == 1:
                        # Production to a terminal (leading to a final state)
                        char = rule[0]
                        if char not in self.transitions[variable]:
                            self.transitions[variable][char] = set()
                        self.transitions[variable][char].add("final_" + variable)
                        self.final_states.add("final_" + variable)

                    if len(rule) == 2:
                        # Production to another variable
                        char, next_state = rule
                        if char not in self.transitions[variable]:
                            self.transitions[variable][char] = set()
                        self.transitions[variable][char].add(next_state)
        self.NFA_Information()


class NFAConvertor:
    def __init__(self, grammar):
        self.start_variable = grammar["start_variable"]
        self.variables = grammar["variables"]
        self.terminals = grammar["terminals"]
        self.p = grammar["p"]
        self.states =  set(grammar["variables"])
        self.transitions = None
        self.final_states = set()
        self.nfa = self.convert()

    def NFA_Information(self):
        print(f'given data: variables:{self.variables}\n terminals:{self.terminals}\n productions:{self.p}\n start_variable:{self.start_variable}\n')
        print(f'results: final_states:{self.final_states}\n transitions:{self.transitions}\n')

    def transitions_function(self):
        self.transitions = {state: {} for state in self.states }
         
    def convert(self):
        self.transitions_function()
        if self.transitions != None:
            for variable, rules in self.p.items():
                for rule in rules:
                    print(f"Processing rule: {variable} -> {rule}")

                    if len(rule) == 1:
                        char = rule[0]
                        if char not in self.transitions[variable]:
                            self.transitions[variable][char] = set()
                        self.transitions[variable][char].add("final_" + variable)
                        self.final_states.add("final_" + variable)

                    if len(rule) == 2:
                        char, next_state = rule
                        if char not in self.transitions[variable]:
                            self.transitions[variable][char] = set()
                        self.transitions[variable][char].add(next_state)
        self.NFA_Information()

        

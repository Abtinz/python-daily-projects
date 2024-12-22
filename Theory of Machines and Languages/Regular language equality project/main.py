from nfa_convertor import NFAConvertor
from dfa_convertor import DFAConverter
from equalityChecker import EqualChecker

"""
    this function will prompts the user for components of a grammar and returns a dictionary representing the grammar.
    Better to say, the function collects input for the alphabet, variables, terminals, start variable, and productions.
    Each component is split by spaces or specific delimiters as instructed to the user.
"""
def read_grammar():
    print("Please enter the grammar alphabet (split with spaces):")
    alphabet = set(input().split())
    
    print("Please enter the grammar variables (split with spaces):")
    variables = set(input().split())
    
    print("Please enter the grammar terminals (split with spaces):")
    terminals = set(input().split())
    
    print("Please enter the start variable (one character):")
    start_variable = input().strip()
    
    productions = {}
    print("Enter the productions (each production as LHS -> RHS, split multiple RHS with '|', separate productions with ';'):")
    productions_input = input().split(';')
    for production in productions_input:
        lhs, rhs = production.split('->')
        lhs = lhs.strip()
        rhs_list = rhs.split('|')
        productions[lhs] = [tuple(r.split()) for r in rhs_list]
    
    return {
        "variables": variables,
        "terminals": terminals,
        "alphabet": alphabet,
        "p": productions,
        "start_variable": start_variable
    }

def main():
    print("Entering first grammar:")
    grammar1 = read_grammar()
    
    print("Entering second grammar:")
    grammar2 = read_grammar()
    
    print("\nFirst Grammar:", grammar1)
    print("\nSecond Grammar:", grammar2)

    nfa1 = NFAConvertor(grammar1)
    nfa2 = NFAConvertor(grammar2)

    dfa_converter1 = DFAConverter(nfa1)
    dfa_converter2 = DFAConverter(nfa2)
    dfa1 = dfa_converter1.convert()
    dfa2 = dfa_converter2.convert()
    print(dfa1)
    
    equal_checker = EqualChecker(dfa1, dfa2)
    are_equal = equal_checker.check_equal()

    print(f"The grammars are equivalent: {are_equal}")

if __name__ == "__main__":
    main()

grammar4 = {
        "variables": {"S", "A"},
        "terminals": {"a", "b"},
        "p": {
            "S": [("a", "S"), ("b", "A"), ("b")],
            "A": [("a", "S"), ("landa")]
        },
        "start_variable": "S"
    }

grammar3 = {
        "variables": {"T", "B"},
        "terminals": {"a", "b", "c"},
        "p": {
            "T": [("a", "T"), ("b", "B"), ("c")],
            "B": [("b", "B"), ("landa")]
        },
        "start_variable": "T"
    }
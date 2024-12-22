from nfa_convertor import NFAConvertor
from dfa_convertor import DFAConverter
from equalityChecker import EqualChecker

def main():
    # Define two example grammars as given
    grammar1 = {
        "variables": {"S", "A"},
        "terminals": {"a", "b"},
        "p": {
            "S": [("a", "S"), ("b", "A"), ("b")],
            "A": [("a", "S"), ("landa")]
        },
        "start_variable": "S"
    }

    grammar2 = {
        "variables": {"T", "B"},
        "terminals": {"a", "b", "c"},
        "p": {
            "T": [("a", "T"), ("b", "B"), ("c")],
            "B": [("b", "B"), ("landa")]
        },
        "start_variable": "T"
    }

    # Convert grammars to NFAs (hypothetical function calls, assuming these are implemented)
    nfa1 = NFAConvertor(grammar1)
    nfa2 = NFAConvertor(grammar2)

    # Convert NFAs to DFAs (using the hypothetical DFAConverter class)
    dfa_converter1 = DFAConverter(nfa1)
    dfa_converter2 = DFAConverter(nfa2)
    dfa1 = dfa_converter1.convert()
    dfa2 = dfa_converter2.convert()
    print(dfa1)
    
    # Check if the two DFAs are equal
    equal_checker = EqualChecker(dfa1, dfa2)
    are_equal = equal_checker.check_equal()

    # Print the result
    print(f"The grammars are equivalent: {are_equal}")

# Assuming that NFAConverter and DFAConverter classes have methods to properly initialize and convert NFAs to DFAs
if __name__ == "__main__":
    main()

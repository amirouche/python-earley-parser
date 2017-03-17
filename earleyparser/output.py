from grammar import grammar_from_api
from earley_parser import parser

if __name__ == "__main__":
    phrase = "la petite ferme le voile".split(" ")
    grammar = grammar_from_api()
    ess = parser(grammar, phrase)
    # ess.post_porcess()
    ess.output_dot()

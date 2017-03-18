from grammar import grammar_from_api
from earley_parser import parser


def main(grammar, phrase):
    return parser(grammar, phrase.split())


if __name__ == "__main__":
    ess = main(grammar_from_api(), "la petite ferme le voile")
    ess.output_dot()

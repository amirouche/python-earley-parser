from __future__ import print_function

import sys

from grammar import grammar_from_text
from earley_parser import parser
from earley_parser import build_parse_tree
from parse_tools import ParseRuleSet




if __name__ == "__main__":
    text = sys.stdin.read()
    grammar = grammar_from_text(text)
    sentence = sys.argv[1:]

    ess = parser(grammar, sentence)

    parses = ParseRuleSet(ess)

    # print('* node cache')
    # parses._print_node_cache()

    # print('* parse result set')
    # parses.output_flat()

    forest = build_parse_tree(parses.root, parses.cache)

    print('* results')
    for idx, tree in enumerate(forest):
        print("** tree", idx)
        tree.show()


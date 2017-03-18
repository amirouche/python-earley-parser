from __future__ import print_function

from grammar import grammar_from_api
from earley_algorithm import *
from earley_super_set import EarleySuperSet
from parse_tools import ParseRuleSet
from earley_algorithm import parser

class ParseNode:

    def __init__(self, item):
        self.item = item
        self.rhs = []

    def show(self):
        lhs_output = "%s ->" % self.item
        rhs_output = " ".join([str(e.item) for e in self.rhs])
        print("%s %s" % (lhs_output, rhs_output))
        for item in self.rhs:
            if item.rhs:
                item.show()


def build_parse_tree(parse_item, cache):
    # parse_item est un ParseItem donc lhs, rhs, et rule
    # cache est le dictionnaire des regle avec des parse_item
    if not str(parse_item) in cache.keys():
        return [ParseNode(parse_item)]  # leaf node

    parse_trees = []

    for parse_item_rule in cache[str(parse_item)]:
        # create parse node, with lhs item as parse_item

        # rhs will be base on parse_item_rule
        rhs_parse_sets = []

        for rhs_item in parse_item_rule.rhs:
            rhs_item_parse_set = build_parse_tree(rhs_item, cache)
            rhs_parse_sets.append(rhs_item_parse_set)

        config_max = [len(e) - 1 for e in rhs_parse_sets]
        config = [0 for e in rhs_parse_sets]

        # do
        parse_node = ParseNode(parse_item)
        parse_trees.append(parse_node)
        for rhs_index in range(len(parse_item_rule.rhs)):
            index = config[rhs_index]
            rhs_item = rhs_parse_sets[rhs_index][index]
            parse_node.rhs.append(rhs_item)

        from tools import next_uplet

        # while
        while next_uplet(config, config_max):
            parse_node = ParseNode(parse_item)
            parse_trees.append(parse_node)
            for rhs_index in range(len(parse_item_rule.rhs)):
                index = config[rhs_index]
                rhs_item = rhs_parse_sets[rhs_index][index]
                parse_node.rhs.append(rhs_item)

    return parse_trees


if __name__ == "__main__":
    phrase = "la petite ferme le voile".split(" ")
    grammar = grammar_from_api()
    ess = parser(grammar, phrase)

    pf = ParseRuleSet(ess)
    print('* node cache')
    pf._print_node_cache()

    print('* parse result set')
    pf.output_flat()

    forest = build_parse_tree(pf.root, pf.cache)

    print('* results')
    for idx, tree in enumerate(forest):
        print("** tree", idx)
        tree.show()


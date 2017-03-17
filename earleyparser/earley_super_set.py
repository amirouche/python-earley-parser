# This Python file uses the following encoding: utf-8
from tremendous import yellow, bold, blue, red


class EarleySuperSet:

    def __init__(self, grammar, phrase):
        self.grammar = grammar
        self.phrase = phrase
        self.first_free = 0

        self.items = list()

        self.charts = [list() for position in range(len(phrase) + 1)]

        self.children = []
        self.is_closed = False

    def add(self, item, parent=None):
        new = False
        if not item in self.items:
            self.items.append(item)
            self.charts[item.end].append(item)
            new = True
        else:
            index = self.items.index(item)
            item = self.items[index]
        if parent:
            item.parents.append(parent)
        if not self.is_closed and new:
            # we check for terminaison only if it's a new item
            if(self.is_closed_item(item)):
                self.is_closed = True

    def post_process_items(self):
        L = len(self.phrase)
        for item in self.charts[L]:
            if self.is_closed_item(item):
                item.tokeep()

    def is_closed_item(self, item):
        rule = item.rule
        if rule.lhs.symbole == "S":
            if item.start == 0:
                if item.end == len(self.phrase):
                    if len(rule.rhs) == item.position:
                        return True
        return False

    def show(self):
        """Outputs informations about all items on stdin"""
        for index in range(len(self.items)):
            item = self.items[index]
            print("# item index : %d" % index)
            complete = "# %s" % item.complete_string()
            print(complete)
            item.show()
            print("\n")

    def output_dot(self):
        """Prints on stdin a graph in dot langage, see Makefile rule dot"""
        print("""digraph {""")
        for item in self.items:
            if item.parents:
                item_index = self.items.index(item)
                for parent in item.parents:
                    parent_index = self.items.index(parent)
                    parent_node_str = "\"<%d|%s|%d>[%s]{%d}" % (
                        parent.start, parent.complete_string(), parent.end, parent.type, parent_index)

                    item_node_str = "\"<%d|%s|%d>[%s]{%d}" % (
                        item.start, item.complete_string(), item.end, item.type, item_index)
                    if item.keep:
                        item_node_str = item_node_str + "❤"
                    if parent.keep:
                        parent_node_str = parent_node_str + "❤"
                    item_node_str += "\""
                    parent_node_str += "\""
                    print("%s -> %s;" % (parent_node_str, item_node_str))
        print("""}""")

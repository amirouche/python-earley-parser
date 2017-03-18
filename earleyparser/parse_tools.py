from __future__ import print_function


red = bold = yellow = lambda x: x


class ParseItem:

    def __init__(self, start, end, symbole):
        self.start = start
        self.end = end
        self.symbole = symbole

    def __cmp__(self, o):
        if self.start != o.start:
            return 1
        if self.end != o.end:
            return 1
        if self.symbole != o.symbole:
            return 1
        return 0

    def is_root(self, ess):
        if self.symbole != "S":
            return False
        if self.start != 0:
            return False
        if self.end != len(ess.phrase):
            return False
        return True

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return "%s[%s..%s]" % (self.symbole, str(self.start), str(self.end))


class ParseRule:

    def __init__(self, rule, lhs, rhs):
        self.rule = rule
        self.lhs = lhs
        self.rhs = rhs

    def __eq__(self, o):
        if self.lhs != o.lhs:
            return False
        L = len(self.rhs)
        if L != len(o.rhs):
            return False
        for rhs_item_index in range(L):
            if self.rhs[rhs_item_index] != o.rhs[rhs_item_index]:
                return False
        return True

    def __hash__(self):
        return id(self)

    def __repr__(self):
        lhs_string = str(self.lhs)
        rhs = [str(rhs_item) for rhs_item in self.rhs]
        rhs_string = " ".join(rhs)
        return lhs_string + " -> " + rhs_string


class ParseRuleSet:

    def __init__(self, ess):
        self.ess = ess
        self.root = None
        self.parse_items = []
        self.tree_nodes = []

        self.cache = {}

        self.tree = []

        self.__build_tree_nodes__()

    def _print_node_cache(self):
        for key in self.cache.keys():
            print(bold(red("# %s" % key)))
            for item in self.cache[key]:
                print(yellow("## %s" % str(item)))

    def __build_tree_nodes__(self):
        for item in self.ess.items:
            if item.keep:
                if item.rule.is_terminal():
                    continue
                # build lhs parse item
                start = item.start
                end = item.end
                symbole = item.rule.lhs.symbole

                lhs_parse_item = self.__get_parse_item__(start, end, symbole)
                # done!

                # build rhs parse items
                rhs_parse_items = []
                last = item.start
                sane = True
                for rhs_item_index in range(len(item.rule.rhs)):
                    start = last
                    end = item.intervals[rhs_item_index]
                    symbole = item.rule.rhs[rhs_item_index].symbole

                    if end is None:
                        sane = False
                        break

                    parse_item = self.__get_parse_item__(start, end, symbole)

                    last = end

                    rhs_parse_items.append(parse_item)
                if sane:
                    # create tree node
                    node = ParseRule(
                        item.rule,
                        lhs_parse_item,
                        rhs_parse_items)
                    if not node in self.tree_nodes:
                        self.tree_nodes.append(node)

                        # update cache :
                        node_string = str(node.lhs)
                        node_list = self.cache.get(node_string, [])
                        if node_list:
                            node_list.append(node)
                        else:
                            self.cache[node_string] = [node]

    def __get_parse_item__(self, start, end, symbole):
        item = ParseItem(start, end, symbole)
        if item in self.parse_items:
            saved_item_index = self.parse_items.index(item)
            return self.parse_items[saved_item_index]
        else:
            self.parse_items.append(item)
            if not self.root:
                if item.is_root(self.ess):
                    self.root = item
            return item

    def output_flat(self):
        print('root node : ', self.root)
        for node in self.tree_nodes:
            print(node)

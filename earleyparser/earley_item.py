# This Python file uses the following encoding: utf-8
from tremendous import bold, red, cyan, blue, yellow, bold


class EarleyItem:

    def __init__(self):
        self.position = 0
        self.start = 0
        self.end = 0
        self.keep = False
        self.type = None
        self.rule = None
        self.parents = list()
        self.intervals = None

    def set_rule(self, rule):
        self.rule = rule
        L = len(rule.rhs)
        self.intervals = [None for e in range(L)]

    def __cmp__(self, other):
        """if self == other : return 0; else return 1"""
        for attribute in ("position", "start", "end", "type", "rule"):
            if getattr(self, attribute) != getattr(other, attribute):
                return 1
        length = len(self.intervals)

        if length != len(other.intervals):
            return 1

        for interval_idx in range(length):
            if self.intervals[interval_idx] != other.intervals[interval_idx]:
                return 1

        return 0

    def show(self):
        print(bold(red("## %s" % str(self))))
        if self.keep:
            print(red("# keep"))
        else:
            print(red("# don't keep"))
        for attribute in ("position", "start", "end", "keep", "type"):
            print(
                blue(
                    "## %s: %s" %
                    (attribute, str(
                        getattr(
                            self, attribute)))))

        lhs = self.rule.lhs.symbole
        rhs = " ".join([e.symbole for e in self.rule.rhs])

        print(cyan("## rule: %s -> %s" % (lhs, rhs)))
        print("## parents: %s" % self.parents)
        print("## intervals %s" % self.intervals)

    def is_scan_complete(self):
        if self.rule.is_terminal():
            return self.position == 1
        else:
            return len(self.rule.rhs) == self.position

    def short_string(self):
        lhs = self.rule.lhs.symbole
        rhs_list = [e.symbole for e in self.rule.rhs]
        rhs_list.insert(self.position, "ø")
        rhs = " ".join(rhs_list)
        return "%s => %s" % (lhs, rhs)

    def complete_string(self):
        lhs = "%s[%d..%d] ->" % (self.rule.lhs.symbole, self.start, self.end)
        rhs = []
        start = self.start
        for rhs_index in range(len(self.rule.rhs)):
            rhs_item = self.rule.rhs[rhs_index]

            start = str(start)
            end = str(self.intervals[rhs_index])
            rhs.append("%s[%s..%s]" % (rhs_item.symbole, start, end))

            try:
                start = int(end) + 1
            except:
                start = 0

        rhs.insert(self.position, "ø")
        return "%s -> %s" % (lhs, " ".join(rhs))

    def tokeep(self):
        self.keep = True
        for parent in self.parents:
            parent.tokeep()

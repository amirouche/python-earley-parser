class Token:

    def __init__(self, symbole):
        self.symbole = symbole
        self.rules = set()

    def is_terminal(self):
        return len(self.rules) == 0


class Rule:

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        if rhs:
            self.rhs = rhs
        else:
            self.rhs = []

    def is_terminal(self):
        return len(self.rhs) == 0


class Grammar:

    def __init__(self, name):
        self.name = name
        self.tokens = {}

    def show_flat(self):
        for token in self.tokens.keys():
            for regle in self.tokens[token].rules:
                lhs = regle.lhs.symbole
                rhs = [e.symbole for e in regle.rhs]
                print("%s -> %s" % (lhs, " ".join(rhs)))

    def add_token(self, token):
        if token not in self.tokens.keys():
            self.tokens[token] = Token(token)

    def get_token(self, token):
        return self.tokens.get(token, None)

    def get_rules(self, token):
        return self.tokens[token].rules

    def add_rule(self, lhs, *rhs):  # left_handle_side, right_*
        token = self.get_token(lhs)
        rhs = [self.get_token(rhs_item) for rhs_item in rhs]
        lhs = self.get_token(lhs)
        regle = Rule(lhs, rhs)
        token.rules.add(regle)


def grammar_from_api():
    grammar = Grammar("petite_ferme")

    grammar.add_token("H")
    grammar.add_token("S")
    grammar.add_token("GN")
    grammar.add_token("GV")
    grammar.add_token("D")
    grammar.add_token("ADJ")
    grammar.add_token("N")
    grammar.add_token("PRO")
    grammar.add_token("V")
    grammar.add_token("la")
    grammar.add_token("petite")
    grammar.add_token("ferme")
    grammar.add_token("le")
    grammar.add_token("voile")

    grammar.add_rule("S", "H")
    grammar.add_rule("H", "GN", "GV")
    grammar.add_rule("GN", "D", "ADJ", "N")
    grammar.add_rule("GN", "D", "N")
    grammar.add_rule("GN", "PRO")
    grammar.add_rule("GV", "PRO", "V")
    grammar.add_rule("GV", "V", "GN")
    grammar.add_rule("D", "la")
    grammar.add_rule("N", "petite")
    grammar.add_rule("ADJ", "petite")
    grammar.add_rule("N", "ferme")
    grammar.add_rule("V", "ferme")
    grammar.add_rule("PRO", "le")
    grammar.add_rule("D", "le")
    grammar.add_rule("N", "voile")
    grammar.add_rule("V", "voile")
    grammar.add_rule("la")
    grammar.add_rule("petite")
    grammar.add_rule("ferme")
    grammar.add_rule("le")
    grammar.add_rule("voile")

    return grammar

if __name__ == "__main__":
    grammar = grammar_from_api()
    grammar.show_flat()

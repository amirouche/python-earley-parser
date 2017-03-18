from earley_item import EarleyItem
from earley_super_set import EarleySuperSet


def parser(grammar, phrase):
    ess = EarleySuperSet(grammar, phrase)

    # init the parse with the root rule
    rules = ess.grammar.get_rules("S")

    for rule in rules:
        item = EarleyItem()
        item.set_rule(rule)
        item.type = prediction.__name__
        ess.add(item)

    # exec!
    for item in ess.items:
        if not completion(ess, item):
            if not scanning(ess, item):
                prediction(ess, item)

    ess.post_process_items()
    return ess


def initialisation(ess):
    return ess


def prediction(ess, item):
    if not item.rule.is_terminal() and not item.is_scan_complete():
        # it's a non terminal token
        rules = item.rule.rhs[item.position].rules
        for rule in rules:
            # for each rule we create a new item
            new = EarleyItem()
            new.set_rule(rule)
            new.position = 0
            new.start = item.end
            new.end = item.end

            new.type = prediction.__name__

            ess.add(new, item)


def scanning(ess, item):

    if(item.rule.is_terminal()):  # it's terminal rule
        word = ess.phrase[item.end]
        symbole = item.rule.lhs.symbole

        if(symbole == word):  # word and symbole match, this rule is scanned
            new = EarleyItem()
            new.type = scanning.__name__

            new.set_rule(item.rule)
            new.position = item.position + 1
            new.start = item.start
            new.end = item.end + 1

            ess.add(new, item)
            return True
    return False


def completion(ess, item):

    if(item.is_scan_complete() and item.type in ("completion", "scanning")):
        symbole = item.rule.lhs.symbole

        for current in ess.charts[item.start]:
            # we are looking for items in the item_set aka chart that
            # we can complete with the current completly scanned rule -
            # read item that has `symbole` @ `position` in rule

            if current.rule.is_terminal():
                continue  # can't complete a terminal rule
            if current.position == len(current.rule.rhs):
                continue  # can't complete a completed rule

            current_symbole = current.rule.rhs[current.position].symbole

            if(item.rule.lhs.symbole == current_symbole):
                new = EarleyItem()
                new.type = completion.__name__

                new.set_rule(current.rule)
                new.position = current.position + 1
                new.start = current.start
                new.end = item.end

                new.intervals = list(current.intervals)
                # the next line means : the token is read at item.end
                # in the sentence
                new.intervals[current.position] = item.end

                ess.add(new, item)

        return True

    return False

def next_uplet(nuplet, nuplet_max):
    for i in range(len(nuplet)):
        if(nuplet[i] < nuplet_max[i]):
            nuplet[i] += 1
            return True
        else:
            nuplet[i] = 0
    return False


def iter_config(max):
    uplet = [0 for e in max]
    return next_uplet(uplet, max)

import sys

def split_further(split_runner):
    l = []
    m = {}

    with open('registry.toml', 'r') as f:
        for x in f:
            x = x.strip('\r\n')
            if x == 'runner = \'%s\'' % split_runner:
                runner = x[len('runner = \''):-1]
                if runner not in m:
                    m[runner] = 0
                m[runner] += 1
            l += [x]

    l2 = []
    m2 = {}

    for x in l:
        if x == 'runner = \'%s\'' % split_runner:
            runner = x[len('runner = \''):-1]
            if runner not in m2:
                m2[runner] = 0
            m2[runner] += 1
            if m2[runner] - 1 > (m[runner] - 1) * 3 / 4:
                runner = runner + '-4'
            elif m2[runner] - 1 > (m[runner] - 1) * 2 / 4:
                runner = runner + '-3'
            elif m2[runner] - 1 > (m[runner] - 1) * 1 / 4:
                runner = runner + '-2'
            l2 += ['runner = \'%s\'' % runner]
        else:
            l2 += [x]

    with open('registry.toml', 'w') as f:
        for x in l2:
            f.write(x + '\n')

split_further('molly4')
split_further('molly6')
# TODO

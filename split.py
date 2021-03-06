l = []
m = {}

with open('registry.toml', 'r') as f:
    for x in f:
        x = x.strip('\r\n')
        if x.startswith('runner = \'') and x.endswith('\''):
            runner = x[len('runner = \''):-1]
            if runner not in m:
                m[runner] = 0
            m[runner] += 1
        l += [x]

l2 = []
m2 = {}

for x in l:
    if x.startswith('runner = \'') and x.endswith('\''):
        runner = x[len('runner = \''):-1]
        if runner not in m2:
            m2[runner] = 0
        m2[runner] += 1
        if m2[runner] - 1 > (m[runner] - 1) * 7 / 8:
            runner = runner + '8'
        elif m2[runner] - 1 > (m[runner] - 1) * 6 / 8:
            runner = runner + '7'
        elif m2[runner] - 1 > (m[runner] - 1) * 5 / 8:
            runner = runner + '6'
        elif m2[runner] - 1 > (m[runner] - 1) * 4 / 8:
            runner = runner + '5'
        elif m2[runner] - 1 > (m[runner] - 1) * 3 / 8:
            runner = runner + '4'
        elif m2[runner] - 1 > (m[runner] - 1) * 2 / 8:
            runner = runner + '3'
        elif m2[runner] - 1 > (m[runner] - 1) * 1 / 8:
            runner = runner + '2'
        l2 += ['runner = \'%s\'' % runner]
    else:
        l2 += [x]

with open('registry.toml', 'w') as f:
    for x in l2:
        f.write(x + '\n')

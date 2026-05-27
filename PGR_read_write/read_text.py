fname = 'organic.out'

HtoeV = 27.2114
convergence = []

f = open(fname,'r')

for line in f:
    print(line)

f.close()

g = open('convergence.out','w+')
g.write('This is how to write to a file\n')
g.write('There are ' + str(HtoeV) + ' eV per atomic unit of energy (Hartree)')
g.close()

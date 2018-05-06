#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################
## Python Optimal BST ##
##   Leonardo Dutra   ##
########################

##########################################################################
# Uso:                                                                   #
# optimal-bst.py [-h] [--p P [P ...]] [--q Q [Q ...]]                    #
#                                                                        #
# Exemplo:                                                               #
# $ python arvoreotima.py --p .15 .1 .05 .1 .2 --k 25 12 23 34 45 #
##########################################################################


class OptimalBst:
    def __init__(self, p, k):
        self.p = p
        self.k = k
        self.root = dict()

    def optimal_tree(self, n):
        e = dict()
        w = dict()
        for i in range(1, n + 2):
            e[(i, i - 1)] = self.k[i - 1]
            w[(i, i - 1)] = self.k[i - 1]
        for l in range(1, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                e[(i, j)] = float("inf")
                w[(i, j)] = w[(i, j - 1)] + self.p[j - 1] + self.k[j]
                for r in range(i, j + 1):
                    t = round(e[(i, r - 1)] + e[(r + 1, j)] + w[(i, j)], 2)
                    if t < e[(i, j)]:
                        e[(i, j)] = t
                        self.root[(i, j)] = r
        return e

    def construct_optimal_tree(self):
        k = self.root[(1, len(self.p))]
        print("k[%d] é a raiz" % k)
        l, r = [(1, k - 1,)], [(k + 1, len(self.p),)]
        p = [k]
        while p:
            if l:
                i, j = l.pop(0)
                if j < i:
                    print("d[%d] is the left child of k[%d]" % (j, p[0]))
                else:
                    k = self.root[(i, j)]
                    print("k[%d] é o filho esquerdo de k[%d]" % (k, p[0]))
                    p[:0] = [k]
                    l.insert(0, (i, k - 1,))
                    r.insert(0, (k + 1, j))
            else:
                i, j = r.pop(0)
                if j < i:
                    print("d[%d] é o filho direito de k[%d]" % (j, p.pop(0)))
                else:
                    k = self.root[(i, j)]
                    print("k[%d] é o filho direito de k[%d]" % (k, p.pop(0)))
                    p[:0] = [k]
                    l.insert(0, (i, k - 1))
                    r.insert(0, (k + 1, j,))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Encontrar a árvore ótima '
                                                 'baseado na probabilidade das chaves')
    parser.add_argument('--p', metavar='P', type=float, nargs='+',
                        help='A list of all probabilities or frequencies of each key')
    parser.add_argument('--k', metavar='k', type=float, nargs='+',
                        help='A list of keys')
    args = parser.parse_args()
    bst = OptimalBst(args.p, args.k)
    bst.optimal_tree(len(args.p))
    bst.construct_optimal_tree()

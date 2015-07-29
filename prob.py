import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def freqCheck(testlist):
    c = collections.Counter(testlist)

    count_sum = sum(c.values())

    for k, v in c.iteritems():
        print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

def boxplotCheck(x):
    plt.figure()
    plt.boxplot(x)
    plt.savefig("boxplot.png")

def histCheck(x):
    plt.figure()
    plt.hist(x, histtype='bar')
    plt.savefig("histogram.png")

def qqCheck(data, figname):
    plt.figure()
    graph = stats.probplot(data, dist="norm", plot=plt)
    plt.savefig(figname)

test_data1 = np.random.normal(size=1000)
test_data2 = np.random.uniform(size=1000)

testlist = [1, 4, 5, 6, 9, 9, 9]
plotPoints = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

freqCheck(testlist)

histCheck(plotPoints)

boxplotCheck(plotPoints)

qqCheck(test_data1, "normal_dist")
qqCheck(test_data2, "uniform_dist")
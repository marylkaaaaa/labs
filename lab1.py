import numpy as np
from scipy import stats

F = ['x1.txt', 'x2.txt']

for FILE in F:
    print('Array: ', FILE)

    with open(FILE) as file:
        array = [row.strip() for row in file]

    a = []
    for i in array:
        a.append(float(i))

    a = np.array(a)
    print('Mean:', np.mean(a))
    print('Variance: ', np.var(a))
    print('Unb variance: ', np.var(a) * (len(a) / len(a) - 1))
    print('Standard deviation: ', np.std(a))
    print('Skewness: ', stats.skew(a))
    print('Kurtosis: ', stats.kurtosis(a))
    print('Mode: ', stats.mode(a))
    print('Median: ', np.median(a))
    print()

    if FILE == F[0]:
        arr1 = a
        E1 = np.mean(a)
        o1 = np.std(a)
    else:
        arr2 = a
        E2 = np.mean(a)
        o2 = np.std(a)

    # plt.title(FILE)
    # plt.xlabel('N')
    # plt.ylabel('X')
    # plt.plot(np.arange(len(a)), a, 'o-', label='Xn')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

# print('Covariation coefficient \n:',np.cov(arr1,arr2))
# print('Covariation coefficient \n:',np.correlate(arr1,arr2))


print('Covariation coefficient',stats.pearsonr(arr1, arr2)[0]*o1*o2)
print('Correlation coefficient',stats.pearsonr(arr1, arr2)[0])

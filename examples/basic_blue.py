#!/usr/bin/env python3

# test of the example in Nucl. Instrum. Meth. A 270 (1988) 110

import blue_combine as blue

measurements = blue.Measurements([9.5, 11.9, 11.1, 8.9])
E = blue.CovarianceMatrix(
    [[2.74, 1.15, 0.86, 1.31],
     [1.15, 1.67, 0.82, 1.32],
     [0.86, 0.82, 2.12, 1.05],
     [1.31, 1.32, 1.05, 2.93]]
)

print('Measurements:', measurements)
print('Covariance Matrix:')
print(E)

comb = blue.BLUE(measurements, E)
print()
print('BLUE result:')
print(comb)

#!/usr/bin/env python3

import blue_combine as blue

measurements = blue.Measurements([125.25, 126.5])
errors = blue.Errors([2, 3])
E = blue.CovarianceMatrix.from_correlation_matrix(
    errors,
    [[1, .5],
     [.5, 1]])

print('Measurements:')
print(measurements)
print('Errors:')
print(errors)
print('Covariance matrix:')
print(E)

print(blue.BLUE(measurements, E))

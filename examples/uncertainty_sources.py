#!/usr/bin/env python3

import blue_combine as blue
import numpy as np
from collections import OrderedDict

n = 2
measurements = blue.Measurements([172.250, 172.800])

# correlation matrices for 0% and 100% correlation
UNCORR = np.identity(n)
CORR = np.ones((n, n))

# build covariance matrices for different uncertainty sources
components = OrderedDict()
components['Stat']    = blue.CovarianceMatrix.from_correlation_matrix([0.20, 0.30], UNCORR)
components['JES']     = blue.CovarianceMatrix.from_correlation_matrix([0.15, 0.16], CORR)
components['ISR']     = blue.CovarianceMatrix.from_correlation_matrix([0.25, 0.32], CORR)
components['FSR']     = blue.CovarianceMatrix.from_correlation_matrix([0.35, 0.40], CORR)
components['PDF']     = blue.CovarianceMatrix.from_correlation_matrix([0.02, 0.01], CORR)
components['BKG']     = blue.CovarianceMatrix.from_correlation_matrix([0.05, 0.09], UNCORR)
components['Trigger'] = blue.CovarianceMatrix.from_correlation_matrix([0.01, 0.05], UNCORR)

# build total covariance matrix
E = blue.CovarianceMatrix(np.zeros((n, n)))
for comp in components.values():
    E += comp

print('Total covariance matrix:')
print(E)
print('Total correlation matrix:')
print(E.correlation_matrix())
print('Blue combination:')
print(blue.BLUE(measurements, E))

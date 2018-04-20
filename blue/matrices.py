# Copyright 2018 Johannes Lange
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math
import numpy as np


class Measurements(np.matrix):

    def __new__(cls, *args, **kwargs):
        instance = super(Measurements, cls).__new__(cls, *args, **kwargs)
        assert instance.shape[0] == 1, 'measurement vector must be one-dimensional'
        return instance


class Errors(np.matrix):

    def __new__(cls, *args, **kwargs):
        instance = super(Errors, cls).__new__(cls, *args, **kwargs)
        assert instance.shape[0] == 1, 'error vector must be one-dimensional'
        return instance


class CovarianceMatrix(np.matrix):

    def __new__(cls, *args, **kwargs):
        instance = super(CovarianceMatrix, cls).__new__(cls, *args, **kwargs)
        dim = instance.shape
        assert dim[0] == dim[1], 'covariance matrix needs to be square'
        return instance

    @classmethod
    def from_correlation_matrix(cls, errors, rho, reduce_correlations=False):
        errors = Errors(errors)
        n = errors.shape[1]
        rho = np.matrix(rho)
        assert rho.shape == (n, n), '%d measurements, but rho is of dim %s' % (n, str(E.shape))

        # create the covariance matrix
        cov = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                corr = rho[i, j]
                if reduce_correlations and corr == 1.0:
                    # reduce correlation to rho = sigma_X/sigma_Y,
                    # assuming sigma_X <= sigma_Y
                    cov[i, j] = min(errors[0, i], errors[0, j])**2
                else:
                    cov[i, j] = corr * errors[0, i] * errors[0, j]

        return cls.__new__(cls, cov)

    def correlation_matrix(self):
        corr = np.zeros(self.shape)
        n = self.shape[0]
        for i in range(n):
            sigma_i = math.sqrt(self[i, i])
            for j in range(n):
                sigma_j = math.sqrt(self[j, j])
                corr[i, j] = self[i, j] / (sigma_i * sigma_j)
        return corr

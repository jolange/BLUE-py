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

import numpy as np
from . import matrices


class BLUE:

    def __init__(self, y, E):
        assert isinstance(y, matrices.Measurements)
        assert isinstance(E, matrices.CovarianceMatrix)
        n = y.shape[1]
        assert E.shape == (n, n), '%d measurements, but E is of dim %s' % (n, str(E.shape))
        U = np.ones((n, 1))
        self.alpha = E.I * U / (U.T * E.I * U)
        self.mean = y * self.alpha
        self.sigma = np.sqrt(self.alpha.T * E * self.alpha)
        delta = y-self.mean
        self.chi2 = delta*E.I*delta.T
        self.Ndf = n-1  # number of degrees of freedom

    def weights(self):
        return self.alpha.T

    def p_value(self):
        from scipy import stats
        return 1 - stats.chi2.cdf(self.chi2, self.Ndf)

    def __str__(self):
        string = 'weights = ' + str(self.weights()) + '\n'
        string += 'result = %g +- %g\n' % (self.mean, self.sigma)
        string += 'chi2/Ndf = %.1f/%d' % (self.chi2, self.Ndf)
        try:
            string += ', p=%.3f' % self.p_value()
        except (ModuleNotFoundError, ImportError):
            string += ', p=no scipy.stats module found'
        return string

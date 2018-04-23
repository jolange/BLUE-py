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

    def weights(self):
        return self.alpha.T

    def __str__(self):
        string = 'weights = ' + str(self.weights()) + '\n'
        string += 'result = %g +- %g' % (self.mean, self.sigma)
        return string

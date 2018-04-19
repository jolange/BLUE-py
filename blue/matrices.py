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


class Measurements(np.matrix):

    def __new__(cls, *args, **kwargs):
        instance = super(Measurements, cls).__new__(cls, *args, **kwargs)
        assert instance.shape[0] == 1, 'measurement vector must be one-dimensional'
        return instance


class CovarianceMatrix(np.matrix):

    def __new__(cls, *args, **kwargs):
        instance = super(CovarianceMatrix, cls).__new__(cls, *args, **kwargs)
        dim = instance.shape
        assert dim[0] == dim[1], 'covariance matrix needs to be square'
        return instance

#!/usr/bin/env python3

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

comb = blue.BLUE(measurements, E)
print(comb)

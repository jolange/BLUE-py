#!/usr/bin/env python3

# test of the example in Nucl. Instrum. Meth. A 270 (1988) 110

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

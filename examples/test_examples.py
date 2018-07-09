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

from importlib import import_module

expected_output = {}

expected_output['basic_blue'] = """
weights = [[ 0.14507476  0.46957738  0.34729705  0.03805081]]
result = 11.1598 +- 1.13404
chi2/Ndf = 6.0/3, p=0.111
"""

expected_output['from_correlation_matrix'] = """
weights = [[ 0.85714286  0.14285714]]
result = 125.429 +- 1.96396
chi2/Ndf = 0.2/1, p=0.637
"""

expected_output['uncertainty_sources'] = """
weights = [[ 0.95822281  0.04177719]]
result = 172.273 +- 0.500237
chi2/Ndf = 2.0/1, p=0.157
"""

expected_output['reduced_correlations'] = """
weights = [[ 0.80848214  0.19151786]]
result = 172.355 +- 0.492223
chi2/Ndf = 1.4/1, p=0.245
"""


def test_examples():
    for name, exp_output in expected_output.items():
        example = import_module(name)
        output = str(example.comb).strip().replace(" ", "")
        exp_output = exp_output.strip().replace(" ", "")
        assert output == exp_output, "failing example " + name

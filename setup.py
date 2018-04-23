from setuptools import setup


long_desc = """## BLUE method

A description of the BLUE method as implemented in this package can be found in

- L. Lyons, D. Gibaut and P. Clifford,
  "How to Combine Correlated Estimates of a Single Physical Quantity",
  Nucl. Instrum. Meth. A 270 (1988) 110,
  doi:10.1016/0168-9002(88)90018-6.

- A. Valassi,
  "Combining correlated measurements of several different physical quantities",
  Nucl. Instrum. Meth. A 500 (2003) 391,
  doi:10.1016/S0168-9002(03)00329-2.

## Usage
- the examples directory contains different usage possibilities
- `basic_blue.py`: basic usage of the BLUE class (example in Nucl. Instrum. Meth. A 270 (1988) 110)
- `from_correlation_matrix.py`: use uncertainties and correlation matrix as input
- `uncertainty_sources.py`: specify different uncertainty sources with individual correlations
- `reduced_correlations.py`: use the "reduced correlations" option
  (reduce a 100% correlation to rho = sigma_X/sigma_Y, assuming sigma_X <= sigma_Y)
"""

setup(name='blue_combine',
      version='0.2',
      description='Python package for the Best Linear Unbiased Estimate (BLUE) method',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      url='https://github.com/jolange/BLUE-py',
      author='Johannes Lange',
      license='GPL-3.0',
      packages=['blue_combine'],
      python_requires='>=3',
      install_requires=['numpy'])

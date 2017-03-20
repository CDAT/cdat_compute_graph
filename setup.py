from setuptools import setup, find_packages

setup(name='cdat_compute_graph',
      version='0.1',
      description='Bindings for the CDAT libraries to the compute_graph library',
      url='http://github.com/UV-CDAT/cdat_compute_graph',
      license='BSD 2-clause',
      packages=find_packages(),
      zip_safe=True,
      test_suite='nose.collector'
)

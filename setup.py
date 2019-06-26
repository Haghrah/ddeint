from setuptools import setup

setup(name='ddeint',
      version='0.2.0',
      description='Scipy-based Delay Differential Equations Solver',
      url='https://github.com/Haghrah/ddeint',
      author='Zulko, Amir Arslan Haghrah',
      license='GPL-3.0',
      packages=['ddeint'],
      install_requires=['numpy', 'scipy', ],
      zip_safe=False)

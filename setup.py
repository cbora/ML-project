from setuptools import setup, find_packages

setup (
    name = 'ml-project',
    version = '0.0.1',
    description = 'helper for ML project',
    packages = find_packages(),
    install_requires = [
        'numpy',
        'matplotlib',
        'scikit-learn',
        'scipy',
        'Click',
        ],
    entry_points={
        'console_scripts': ['ml-project = project.cli:cli']
        },
    )
    

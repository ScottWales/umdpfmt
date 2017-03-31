=============================
umdpfmt
=============================

UMDP3 Formatter

.. image:: https://readthedocs.org/projects/umdpfmt/badge/?version=latest
  :target: https://readthedocs.org/projects/umdpfmt/?badge=latest
.. image:: https://travis-ci.org/ScottWales/umdpfmt.svg?branch=master
  :target: https://travis-ci.org/ScottWales/umdpfmt
.. image:: http://codecov.io/github/ScottWales/umdpfmt/coverage.svg?branch=master
  :target: http://codecov.io/github/ScottWales/umdpfmt?branch=master
.. image:: https://landscape.io/github/ScottWales/umdpfmt/master/landscape.svg?style=flat
  :target: https://landscape.io/github/ScottWales/umdpfmt/master
.. image:: https://codeclimate.com/github/ScottWales/umdpfmt/badges/gpa.svg
  :target: https://codeclimate.com/github/ScottWales/umdpfmt
.. image:: https://badge.fury.io/py/umdpfmt.svg
  :target: https://pypi.python.org/pypi/umdpfmt

.. content-marker-for-sphinx

------------------
Build Instructions
------------------

Pip install (into a virtual environment)::

    # TODO: Upload to PyPI
    pip install umdpfmt

or::
    
    # TODO: Support Antlr from $CLASSPATH
    pip install git+https://github.com/ScottWales/umdpfmt

or (for development)::

    git checkout git+https://github.com/ScottWales/umdpfmt
    cd umdpfmt
    wget http://www.antlr.org/download/antlr-4.7-complete.jar
    pip install -e '.[dev]'

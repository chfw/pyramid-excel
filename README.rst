================================================================================
pyramid-excel - Let you focus on data, instead of file formats
================================================================================

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel.github.io/master/images/patreon.png
   :target: https://www.patreon.com/chfw

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel-mobans/master/images/awesome-badge.svg
   :target: https://awesome-python.com/#specific-formats-processing

.. image:: https://codecov.io/gh/pyexcel-webwares/pyramid-excel/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/pyexcel-webwares/pyramid-excel

.. image:: https://badge.fury.io/py/pyramid-excel.svg
   :target: https://pypi.org/project/pyramid-excel



.. image:: https://pepy.tech/badge/pyramid-excel/month
   :target: https://pepy.tech/project/pyramid-excel


.. image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :target: https://gitter.im/pyexcel/Lobby

.. image:: https://img.shields.io/static/v1?label=continuous%20templating&message=%E6%A8%A1%E7%89%88%E6%9B%B4%E6%96%B0&color=blue&style=flat-square
    :target: https://moban.readthedocs.io/en/latest/#at-scale-continous-templating-for-open-source-projects

.. image:: https://img.shields.io/static/v1?label=coding%20style&message=black&color=black&style=flat-square
    :target: https://github.com/psf/black
.. image:: https://readthedocs.org/projects/pyramid-excel/badge/?version=latest
   :target: http://pyramid-excel.readthedocs.org/en/latest/

Support the project
================================================================================

If your company has embedded pyexcel and its components into a revenue generating
product, please support me on github, or `patreon <https://www.patreon.com/bePatron?u=5537627>`_
maintain the project and develop it further.

With your financial support, I will be able to invest a little bit more time in coding,
documentation and writing interesting posts.


Known constraints
==================

Fonts, colors and charts are not supported.

Nor to read password protected xls, xlsx and ods files.

Introduction
================================================================================
Here is a typical conversation between the developer and the user::

 User: "I have uploaded an excel file"
       "but your application says un-supported file format"
 Developer: "Did you upload an xlsx file or a csv file?"
 User: "Well, I am not sure. I saved the data using "
       "Microsoft Excel. Surely, it must be in an excel format."
 Developer: "OK. Here is the thing. I were not told to support"
            "all available excel formats in day 1. Live with it"
            "or delay the project x number of days."

**pyramid-excel** is based on `pyexcel <https://github.com/pyexcel/pyexcel>`_ and makes
it easy to consume/produce information stored in excel files over HTTP protocol as
well as on file system. This library can turn the excel data into a list of lists,
a list of records(dictionaries), dictionaries of lists. And vice versa. Hence it
lets you focus on data in Pyramid based web development, instead of file formats.

The idea originated from the common usability problem: when an excel file
driven web application is delivered for non-developer users (ie: team assistant,
human resource administrator etc). The fact is that not everyone knows (or cares)
about the differences between various excel formats: csv, xls, xlsx are all
the same to them. Instead of training those users about file formats, this
library helps web developers to handle most of the excel file
formats by providing a common programming interface. To add a specific excel
file format type to you application, all you need is to install an extra pyexcel
plugin. Hence no code changes to your application and no issues with excel file
formats any more. Looking at the community, this library and its associated ones
try to become a small and easy to install alternative to Pandas.


The highlighted features are:

#. excel data import into and export from databases
#. turn uploaded excel file directly into Python data structure
#. pass Python data structures as an excel file download
#. provide data persistence as an excel file in server side
#. supports csv, tsv, csvz, tsvz by default and other formats are supported via
   the following plugins:

.. _file-format-list:
.. _a-map-of-plugins-and-file-formats:

.. table:: A list of file formats supported by external plugins

   ======================== ======================= =================
   Package name              Supported file formats  Dependencies
   ======================== ======================= =================
   `pyexcel-io`_            csv, csvz [#f1]_, tsv,  csvz,tsvz readers depends on `chardet`
                            tsvz [#f2]_
   `pyexcel-xls`_           xls, xlsx(read only),   `xlrd`_,
                            xlsm(read only)         `xlwt`_
   `pyexcel-xlsx`_          xlsx                    `openpyxl`_
   `pyexcel-ods3`_          ods                     `pyexcel-ezodf`_,
                                                    lxml
   `pyexcel-ods`_           ods                     `odfpy`_
   ======================== ======================= =================

.. table:: Dedicated file reader and writers

   ======================== ======================= =================
   Package name              Supported file formats  Dependencies
   ======================== ======================= =================
   `pyexcel-xlsxw`_         xlsx(write only)        `XlsxWriter`_
   `pyexcel-libxlsxw`_      xlsx(write only)        `libxlsxwriter`_
   `pyexcel-xlsxr`_         xlsx(read only)         lxml
   `pyexcel-xlsbr`_         xlsb(read only)         pyxlsb
   `pyexcel-odsr`_          read only for ods, fods lxml
   `pyexcel-odsw`_          write only for ods      loxun
   `pyexcel-htmlr`_         html(read only)         lxml,html5lib
   `pyexcel-pdfr`_          pdf(read only)          camelot
   ======================== ======================= =================


Plugin shopping guide
------------------------

Since 2020, all pyexcel-io plugins have dropped the support for python versions
which are lower than 3.6. If you want to use any of those Python versions, please use pyexcel-io
and its plugins versions that are lower than 0.6.0.


Except csv files, xls, xlsx and ods files are a zip of a folder containing a lot of
xml files

The dedicated readers for excel files can stream read


In order to manage the list of plugins installed, you need to use pip to add or remove
a plugin. When you use virtualenv, you can have different plugins per virtual
environment. In the situation where you have multiple plugins that does the same thing
in your environment, you need to tell pyexcel which plugin to use per function call.
For example, pyexcel-ods and pyexcel-odsr, and you want to get_array to use pyexcel-odsr.
You need to append get_array(..., library='pyexcel-odsr').



.. _pyexcel-io: https://github.com/pyexcel/pyexcel-io
.. _pyexcel-xls: https://github.com/pyexcel/pyexcel-xls
.. _pyexcel-xlsx: https://github.com/pyexcel/pyexcel-xlsx
.. _pyexcel-ods: https://github.com/pyexcel/pyexcel-ods
.. _pyexcel-ods3: https://github.com/pyexcel/pyexcel-ods3
.. _pyexcel-odsr: https://github.com/pyexcel/pyexcel-odsr
.. _pyexcel-odsw: https://github.com/pyexcel/pyexcel-odsw
.. _pyexcel-pdfr: https://github.com/pyexcel/pyexcel-pdfr

.. _pyexcel-xlsxw: https://github.com/pyexcel/pyexcel-xlsxw
.. _pyexcel-libxlsxw: https://github.com/pyexcel/pyexcel-libxlsxw
.. _pyexcel-xlsxr: https://github.com/pyexcel/pyexcel-xlsxr
.. _pyexcel-xlsbr: https://github.com/pyexcel/pyexcel-xlsbr
.. _pyexcel-htmlr: https://github.com/pyexcel/pyexcel-htmlr

.. _xlrd: https://github.com/python-excel/xlrd
.. _xlwt: https://github.com/python-excel/xlwt
.. _openpyxl: https://bitbucket.org/openpyxl/openpyxl
.. _XlsxWriter: https://github.com/jmcnamara/XlsxWriter
.. _pyexcel-ezodf: https://github.com/pyexcel/pyexcel-ezodf
.. _odfpy: https://github.com/eea/odfpy
.. _libxlsxwriter: http://libxlsxwriter.github.io/getting_started.html

.. table:: Other data renderers

   ======================== ======================= ================= ==================
   Package name              Supported file formats  Dependencies     Python versions
   ======================== ======================= ================= ==================
   `pyexcel-text`_          write only:rst,         `tabulate`_       2.6, 2.7, 3.3, 3.4
                            mediawiki, html,                          3.5, 3.6, pypy
                            latex, grid, pipe,
                            orgtbl, plain simple
                            read only: ndjson
                            r/w: json
   `pyexcel-handsontable`_  handsontable in html    `handsontable`_   same as above
   `pyexcel-pygal`_         svg chart               `pygal`_          2.7, 3.3, 3.4, 3.5
                                                                      3.6, pypy
   `pyexcel-sortable`_      sortable table in html  `csvtotable`_     same as above
   `pyexcel-gantt`_         gantt chart in html     `frappe-gantt`_   except pypy, same
                                                                      as above
   ======================== ======================= ================= ==================

.. _pyexcel-text: https://github.com/pyexcel/pyexcel-text
.. _tabulate: https://bitbucket.org/astanin/python-tabulate
.. _pyexcel-handsontable: https://github.com/pyexcel/pyexcel-handsontable
.. _handsontable: https://cdnjs.com/libraries/handsontable
.. _pyexcel-pygal: https://github.com/pyexcel/pyexcel-chart
.. _pygal: https://github.com/Kozea/pygal
.. _pyexcel-matplotlib: https://github.com/pyexcel/pyexcel-matplotlib
.. _matplotlib: https://matplotlib.org
.. _pyexcel-sortable: https://github.com/pyexcel/pyexcel-sortable
.. _csvtotable: https://github.com/vividvilla/csvtotable
.. _pyexcel-gantt: https://github.com/pyexcel/pyexcel-gantt
.. _frappe-gantt: https://github.com/frappe/gantt

.. rubric:: Footnotes

.. [#f1] zipped csv file
.. [#f2] zipped tsv file


This library makes information processing involving various excel files as easy as
processing array, dictionary when processing file upload/download, data import into
and export from SQL databases, information analysis and persistence. It uses
**pyexcel** and its plugins:

#. to provide one uniform programming interface to handle csv, tsv, xls, xlsx, xlsm and ods formats.
#. to provide one-stop utility to import the data in uploaded file into a database and to export tables in a database as excel files for file download.
#. to provide the same interface for information persistence at server side: saving a uploaded excel file to and loading a saved excel file from file system.



Tested Pyramid Versions
========================

So far pyexcel-xls plugin does not work with Python 3.9 

.. image:: https://img.shields.io/badge/pyramid-1.10.4-green.svg
    :target: http://travis-ci.org/pyexcel/pyramid-excel

.. image:: https://img.shields.io/badge/pyramid-1.9-green.svg
    :target: http://travis-ci.org/pyexcel/pyramid-excel

.. image:: https://img.shields.io/badge/pyramid-1.8.4-green.svg
    :target: http://travis-ci.org/pyexcel/pyramid-excel

.. image:: https://img.shields.io/badge/pyramid-1.7.6-green.svg
    :target: http://travis-ci.org/pyexcel/pyramid-excel

.. image:: https://img.shields.io/badge/pyramid-1.6.1-green.svg
    :target: http://travis-ci.org/pyexcel/pyramid-excel

.. image:: https://img.shields.io/badge/pyramid-1.5.8-green.svg
    :target: http://travis-ci.org/pyexcel/pyramid-excel

.. image:: https://img.shields.io/badge/pyramid-1.4.9-green.svg
    :target: http://travis-ci.org/pyexcel/pyramid-excel


Installation
================================================================================

You can install pyramid-excel via pip:

.. code-block:: bash

    $ pip install pyramid-excel


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel-webwares/pyramid-excel.git
    $ cd pyramid-excel
    $ python setup.py install

Setup
======
Once the pyramid_excel is installed, you must use the config.include mechanism to include
it into your Pyramid project's configuration::

    config = Configurator(.....)
    config.include('pyramid_excel')

Alternately, you may activate the extension by changing your application's .ini file by
adding it to the pyramid.includes list::

    pyramid.includes = pyramid_excel



Development guide
================================================================================

Development steps for code changes

#. git clone https://github.com/pyexcel/pyramid-excel.git
#. cd pyramid-excel

Upgrade your setup tools and pip. They are needed for development and testing only:

#. pip install --upgrade setuptools pip

Then install relevant development requirements:

#. pip install -r rnd_requirements.txt # if such a file exists
#. pip install -r requirements.txt
#. pip install -r tests/requirements.txt

Once you have finished your changes, please provide test case(s), relevant documentation
and update changelog.yml

.. note::

    As to rnd_requirements.txt, usually, it is created when a dependent
    library is not released. Once the dependency is installed
    (will be released), the future
    version of the dependency in the requirements.txt will be valid.


How to test your contribution
--------------------------------------------------------------------------------

Although `nose` and `doctest` are both used in code testing, it is advisable
that unit tests are put in tests. `doctest` is incorporated only to make sure
the code examples in documentation remain valid across different development
releases.

On Linux/Unix systems, please launch your tests like this::

    $ make

On Windows, please issue this command::

    > test.bat


Before you commit
------------------------------

Please run::

    $ make format

so as to beautify your code otherwise your build may fail your unit test.




License
================================================================================

New BSD License


pip freeze
nosetests --with-cov --cover-package pyexcel_pyexcel --cover-package tests --with-doctest --doctest-extension=.rst tests README.rst  pyramid_excel && flake8 . --exclude=.moban.d 

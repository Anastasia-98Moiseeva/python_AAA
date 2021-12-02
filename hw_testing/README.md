# Запуск тестов

### issue-01
* python -m doctest -v -o NORMALIZE_WHITESPACE test/issue01.py
* результаты запуска лежат в файле result/issue01.txt

### issue-02
* python -m pytest test/issue02.py
* результаты запуска лежат в файле result/issue02.txt

### issue-03
* python -m unittest, 

    или: python -m pytest test/issue03.py

* результаты запуска лежат в файле result/issue03.txt

### issue-04
* python -m pytest test/issue04.py
* результаты запуска лежат в файле result/issue04.txt

### issue-05
* coverage run -m pytest test/issue05.py
* coverage report
* coverage html

* результаты запуска лежат в файле result/issue05.txt


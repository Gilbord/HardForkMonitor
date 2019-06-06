## Запуск
1. Открыть директорию HardForkMonitor (с Pipfile и Pipfile.lock)
2. Установить python3.7 и pipenv (apt install pipenv / pip install pipenv)
3. `pipenv --python 3.7` (создаст виртуальное окружение с нужной версией питона)
4. `pipenv install` (установит зависимости)
5. `pipenv run python  main.py --timestamp 1559807035 --user user --password password --mode rpc --host 127.0.0.1 --port 18332` (запуск)
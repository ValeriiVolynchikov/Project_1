  
#                                            **ПРОЕКТ**  


**IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько  
последних успешных банковских операций клиента. Этот проект, который на бэкенде будет готовить данные для отображения в новом виджете.**

##                                       ***ЗАДАНИЕ ПЕРВОЕ***

1. Организация проекта — создание основных пакетов: **\src** — для исходного кода, **\tests** — для тестов.
2. Установка инструментов для проверки качества кода ***(Flake8, black, isort, mypy)***.
3. Настройка файл *.flake8* для конфигурации линтера *Flake8*.
4. Добавление конфигурации для *black*, *isort* и *mypy* в файл **pyproject.toml**. 
5. В пакете **src** создан модуль с названием **masks**. Здесь реализовано две функции:  
    - Функция маскировки номера банковской карты **get_mask_card_number**.
    - Функция маскировки номера банковского счета **get_mask_account**.

###                                  ***Как работают функции***

- Функция **get_mask_card_number** принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован
  и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры,
   остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами. Пример работы функции:
  7000792289606361     # входной аргумент 7000 79** **** 6361  # выход функции.

-  Функция **get_mask_account** принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате 
   **XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки. Пример работы функции:
   73654108430135874305  # входной аргумент **4305  # выход функции.
- Реализована запись логов в файл. Логи записываются в папку **logs** в корне проекта. Файлы логов имеют расширение **.log**.
  Формат записи лога в файл включает метку времени, название модуля, уровень серьезности и сообщение,
  описывающее событие или ошибку, которые произошли.

##                                       ***ЗАДАНИЕ ВТОРОЕ*** 

1. Инициализация нового локального Git-репозитория в папке проекта.
2. Создание файл .gitignore в корне проекта и добавьте в него стандартные шаблоны для Python, чтобы исключить системные и временные файлы, такие как 
    __pycache__, .idea и другие.
3. В пакете **\src** создан новый модуль с именем **widget**. Этот модуль будет содержать функции для работы с новыми возможностями приложения.
4. В модуле **widget** создана функция **mask_account_card**, которая умеет обрабатывать информацию как о картах, так и о счетах.
   Функция должна:
   - принимать один аргумент — строку, содержащую тип и номер карты или счета.
   - Возвращать строку с замаскированным номером. Для карт и счетов используйте разные типы маскировки.
     Переиспользована уже существующие функции маскировки из проекта, чтобы избежать дублирования кода.
5. В том же модуле создана функция **get_date**, которая принимает на вход строку с датой в формате 
   "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").

 ##                                      ***ЗАДАНИЕ ТРЕТЬЕ*** 

 1. В директории **\src** проекта создан модуль **processing**, который будет содержать новые функции обработки данных.
 2. В модуле **processing** реализована функция **filter_by_state**, которая принимает список словарей и опционально значение для ключа 
     **state** (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
      state соответствует указанному значению.
 3. В том же модуле реализована функция **sort_by_date**, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date).   
  
 ###                                      ***ИНСТРУКЦИЯ ПО УСТАНОВКЕ И КОНФИГУРАЦИИ***
1. Созданы новые ветки в локальном репозитории для работы по GitFlow. Ветка разработки имеет имя **develop**, ветки
    разработки конкретного задания с префиксом **feature**. Для домашней работы урока 10.1 имя будет **feature/homework_10_1**.
2. Создан пустой репозиторий на GitHub, имя проекта **pythonProject4**. Ветка разработки **feature/homework_10_1** и **develop** 
   отправлена в GitHub.

##                                        ***ЗАДАНИЕ ЧЕТВЕРТОЕ - тестирование***
1. Созданы новые ветки в локальном репозитории для работы по GitFlow. Ветка разработки имеет имя **develop**, ветки
    разработки конкретного задания с префиксом **feature**. Для домашней работы урока 10.1 имя будет **feature/homework_10_2_test**.
2. В созданную папку **\tests**  три тест-кейса **(test_masks.py, test_widget.py, test_processing.py)** для тестирования модулей: **masks**,
   **widget**, **processing**.
   - в **test_masks.py** созданы условия для тестирования:
         функции **mask_account_card**:
            Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
            Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
            Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
         функции **get_data**:
            Тестирование правильности преобразования даты.
            Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
            Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
   - в **test_processing.py** созданы условия для тестирования:
         функции **filter_by_state**:
            Тестирование фильтрации списка словарей по заданному статусу state.
            Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
            Параметризация тестов для различных возможных значений статуса state.
         функции **sort_by_date**:
            Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
            Проверка корректности сортировки при одинаковых датах.
            Тесты на работу функции с некорректными или нестандартными форматами дат.
   - в **test_widget.py**:
         функции **mask_account_card**:
            Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа
            входных данных (карта или счет).
            Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
            Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
         функции **get_data**:
            Тестирование правильности преобразования даты.
            Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
            Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
  3. Для проверки функциональности кода созданы условия для проверки покрытия с помощью **Code coverage**.
     Отчет сгенерирован в папке **htmlcov** и храниться в файле с названием **index.html**.

##                                             ***ЗАДАНИЕ ПЯТОЕ - генераторы***
1. Создание нового модуля в проекте под названием **generators**. Этот модуль будет содержать все новые функции,
    реализующие генераторы для обработки данных.
   - Создание функции **filter_by_currency**, которая принимает на вход список словарей, представляющих транзакции.
     Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
     (например, USD).
###                                              **Пример использования функции**
\```
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }

\```
2. Создание генератора **transaction_descriptions**, который принимает список словарей с транзакциями и возвращает
     описание каждой операции по очереди.
###                                              **Пример использования функции**
\```
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации

\```

3. Создание генератора **card_number_generator**, который выдает номера банковских карт в формате 
    XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999. Генератор принимает начальное и конечное значения для
    генерации диапазона номеров. 
###                                              **Пример использования функции**
\```
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005

\``` 

4. Создан тест для нового функционала проекта, **test_generators**. Данный функционал размещен в папке **tests**.
    Тестируются весь модуль **generators**, в нем две функции **filter_by_currency**  **transaction_descriptions** 
    и генератор **card_number_generator**.
###                                              **Пример входных данных функций**
\```
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

\```

##                                             ***ЗАДАНИЕ ШЕСТОЕ - декоратор***
1. Создан новый модуль **decorators** в проекте. Этот модуль будет использоваться для размещения декораторов,
    включая декоратор **log**.
2. Декоратор **log** автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
   Декоратор принимает необязательный аргумент **filename**. В **mylog.txt** записываются логи. Логирование включает
    имя функции и результат выполнения при успешной операции и если выполнение функции привело к ошибке то вносится
    тип возникшей ошибки и входные параметры. 
3. Создан для тестирования **pytest** файл **test_decorators.py** в папке **tests**.

###                                            **Пример использования декоратора**
\```
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

# Вызов функции
my_function(1, 2)

# Пример вызова с ошибкой
# my_function(1, '2')  # Раскомментируйте эту строку, чтобы увидеть обработку ошибки
\```

##                                             ***ЗАДАНИЕ СЕДЬМОЕ - JSON API***
1. Реализована функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
   о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
   Функцию находится в модуле **utils** в папке **srs**. Файл с данными о финансовых транзакциях **operations.json** помещен в
   директорию **data/** в корне проекта.
2. Реализована функция, которая принимает на вход транзакцию и возвращает сумму транзакции **(amount)** в рублях,
    тип данных — **float**. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли. Для конвертации валюты используется
     [Exchange Rates Data API:](https://apilayer.com/exchangerates_data-api). 
3. Функция конвертации помещена в модуль **external_api** в папке **srs**.
4. Использованы переменные окружения из файла **.env** для сокрытия чувствительных данных **(токенов доступа для API).**
   Создан шаблон файла **.env** -> **.env.example** c размещением в репозитории на GitHub.
5. Создан модуль **test_utils.py** в папке **tests**, где реализовано тестирование используя **Mock** и **patch**.
6. Реализована запись логов в файл **utils**. Логи записываются в папку **logs** в корне проекта. Файлы логов имеют расширение **.log**.
  Формат записи лога в файл включает метку времени, название модуля, уровень серьезности и сообщение,
  описывающее событие или ошибку, которые произошли.

##                                             ***ЗАДАНИЕ ВОСЬМОЕ - csv и pandas***
1. Создан отдельный модуль для новых функций **data_reader**. Реализованы функция для считывания финансовых операций из CSV
   **read_transactions_from_csv** и функция для считывания финансовых операций из Excel **read_transactions_from_excel**.
    функции для считывания финансовых операций из CSV и Excel принимают путь к файлу CSV и Excel в качестве аргумента.
    Функция для считывания финансовых операций из CSV и Excel выдают список словарей с транзакциями.
    Все необходимые для работы библиотеки добавлены в зависимости проекта.
2. Созданы тесты к новым функциональностям проекта, модуль **test_data_reader**.
   Тесты для функции считывания финансовых операций из CSV и Excel используют Mock и patch.
3. В модули внесены компоненты логирования. Данные результатов логирования собираются в файл **transactions.log**, в 
   папку **logs**.
4. Для реализации считывания финансовых операций из CSV- и XLSX-файлов скачаны файлы (transactions.csv) и (transactions_excel.xlsx). 
   Данные файлы помещены в директорию **data**.

##                                             ***ЗАДАНИЕ ДЕВЯТОЕ - re, collections, random***
1. Создан модуль **main** в папке **src**. В ней создана функция **load_transactions**, которая принимает список словарей
   с данными о банковских операциях и строку поиска, а возвращает список словарей, у которых в описании есть данная строка.
   При реализации этой функции использована библиотека **re**. Данная функция обрабатывает файлы находящиеся в папке **data**
   с расширениями CSV XLSX и json -файлов. Список словарей с данными о банковских операциях и список категорий операций
   возвращается в словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
   Категории операций хранятся в поле **description**.
2. В модуле **main** реализована следующая логика проекта. 
   Ожидаемое поведение программы:

    **Программа приветствует пользователя:**
    **Программа:** _Привет! Добро пожаловать в программу работы с банковскими транзакциями._ 
     _Выберите необходимый пункт меню:_
     **1. Получить информацию о транзакциях из JSON-файла**
     **2. Получить информацию о транзакциях из CSV-файла**
     **3. Получить информацию о транзакциях из XLSX-файла**
     **Пользователь:** _1_
     **Программа: Для обработки выбран JSON-файл.**
     **Программа: Введите статус, по которому необходимо выполнить фильтрацию.** 
                  **Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING**
     **Пользователь:**  _EXECUTED_
     **Программа:Операции отфильтрованы по статусу "EXECUTED"**
       В случае, если пользователь ввел неверный статус, программа не должна падать в ошибку, а должна возвращать
       пользователя к вводу корректного статуса:
     **Пользователь:** _test_
     **Программа: Статус операции "test" недоступен.**
     **Программа: Введите статус, по которому необходимо выполнить фильтрацию.** 
                  **Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING**
       После фильтрации программа выводит следующие вопросы для уточнения выборки операций, необходимых пользователю,
       и выводит в консоль операции, соответствующие выборке пользователя:
     **Программа: Отсортировать операции по дате?** _Да/Нет_
     **Пользователь:** _да_
     **Программа: Отсортировать по возрастанию или по убыванию?**
     **Пользователь: по возрастанию/по убыванию**
     **Программа: Выводить только рублевые транзакции?** _Да/Нет_
     **Пользователь:** _да_
     **Программа: Отфильтровать список транзакций по определенному слову в описании?** _Да/Нет_
     **Пользователь:** _да/нет_
     **Программа: Распечатываю итоговый список транзакций...**

     ***Программа: Всего банковских операций в выборке: 4***

     08.12.2019 Открытие вклада 
     Счет **4321
     Сумма: 40542 руб. 

     12.11.2019 Перевод с карты на карту
     MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
     Сумма: 130 USD

     18.07.2018 Перевод организации 
     Visa Platinum 7492 65** **** 7202 -> Счет **0034
     Сумма: 8390 руб.

     03.06.2018 Перевод со счета на счет
     Счет **2935 -> Счет **4321
     Сумма: 8200 EUR

     Если выборка оказалась пустой, программа выводит сообщение:
     ***Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации***

3. Создан модуль **config** для хранения конфигурационных параметров, настроек и глобальных переменных,
   которые использованы в других частях приложения. Это позволяет централизовать управление настройками и упрощает
   изменение конфигурации без необходимости вносить изменения в код. Это сделано для централизованного управления,
   упрощение кода, для легкости в тестировании и разделение логики и конфигурации.
4. Для тестирования в **tests** создан модуль **test_main*. В нем реализованы 29 функций для тестирования модуля **main**.

 

## Описание:
Данный проект создан для разработки программы по работе с банковскими операциями клиента.

## Установка:
+ Клонируйте репозиторий:
```

git@github.com:vzacerkovniy/dz10_1.git

```
+ Активируйте окружение и установите зависимости.
```
poetry shell
poetry install
```

## Структура
1. Модуль masks. Две функции для скрытия номера счета и карты.
2. Модуль widget. Две функции для скрытия номера счета/карты и вывода даты из строки.
3. Модуль processing. Две функции для фильтрации и сортировки списков по задаваемым параметрам.
4. Модуль generators. Одна функция-генератор фильтрации списка по валюте и две функции-генератора: одна собирает 
описание операций по картам, другая генерирует номера карт от 0000 0000 0000 0000 до 9999 9999 9999 9999 (можно использовать 
разные начальные и конечные значения)
5. Модуль decorators. Содержит декоратор, записывающий лог выполнения функций в консоль или файл. Логи записываются в 
отдельный файл с указанным именем. При отсутствии имени файла логи будут выведены в консоль. 

## Тестирование
#### Тестирования проводятся при использовании фреймворка pytest. Установка:
```poetry add --group dev pytest```
#### Используемые фикстуры прописаны в файле conftest.py
1. В модуле test_widget тестируется функция состоящая из двух отдельных функций для карты и счета, а также функция 
форматирования даты.
2. В модуле test_masks функции карты и счета тестируются поотдельности.
3. В модуле test_processing тестируются функции фильтрации и сортировки списков по задаваемым параметрам.
4. В модуле test_generators тестируются функции-генераторы.
5. В модуле test_decorators идет проверка декоратора по предикату. Также идет проверка вывода в консоль.
#### Результаты тестирования и покрытие кода находятся в `/htmlcov/index.html`

## Документация:

Для получения дополнительной информации обратитесь к [документации](./README.md).

## Лицензия:


© 2024 Начальный пакет

Настоящим предоставляется бесплатное разрешение любому лицу, получающему копию данного программного обеспечения 
и связанных с ним файлов документации («Программное обеспечение»), на работу с Программным обеспечением без ограничений, 
включая, без ограничений, права на использование, копирование, модификацию, объединение, публикацию, распространение, 
сублицензирование и/или продавать копии Программного обеспечения и разрешать лицам, которым предоставляется Программное 
обеспечение, делать это при соблюдении следующих условий:

Вышеуказанное уведомление об авторских правах и данное уведомление о разрешении должны быть включены во все копии или 
существенные части Программного обеспечения.

ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ, НО НЕ 
ОГРАНИЧИВАЯСЬ ИМИ, ГАРАНТИИ ТОВАРНОЙ ПРИГОДНОСТИ, ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННОЙ ЦЕЛИ И НЕНАРУШЕНИЯ АВТОРСКИХ ПРАВ. НИ ПРИ 
КАКИХ ОБСТОЯТЕЛЬСТВАХ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ ОТВЕТСТВЕННОСТИ ЗА КАКИЕ-ЛИБО ПРЕТЕНЗИИ, УЩЕРБ ИЛИ ИНУЮ 
ОТВЕТСТВЕННОСТЬ, БУДЬ ТО В РЕЗУЛЬТАТЕ ДЕЙСТВИЯ ДОГОВОРА, ГРАЖДАНСКОГО ПРАВОНАРУШЕНИЯ ИЛИ ИНЫМ ОБРАЗОМ, ВЫТЕКАЮЩИЕ ИЗ 
ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИЛИ В СВЯЗИ С НИМ.

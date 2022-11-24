# Урок 8. Python: от простого к практике. Продолжение
Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

# Описание проекта
База данных товаров в формате CSV, включающая в себя артикул, наименование товара, наименование номенклатурной группы, код номенклатурной группы, цену товара в рублях, продажи за 6 месяцев.

# Структура проекта
1. Модуль для запуска программы
- **menu.py**
2. Модуль для просмотра всех артикулов в базе
- **see_all.py**
3. Модуль для поиска артикула
- **search_smth.py**
4. Модуль для добавления нового артикула
- **new_art.py**
5. Модуль для изменения цены артикула
- **change_smth.py**
6. Модуль для удаления артикула
- **delete_smth.py**

# Краткое руководство пользователя
1. Главное меню

![Menu](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%9C%D0%B5%D0%BD%D1%8E%20%D0%B1%D0%B0%D0%B7%D1%8B.png)

2. Просмотреть все артикулы
   
Программа выведет все товары, находящиеся на данный момент в базе с дополнительной информацией (номенклатурная группа, код номенклатурной группы, цена товара).

![See all](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/see_all.png)

3. Добавить артикул
   
Доступно добавление нового артикула.

![New art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D0%B0.png)

![New art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%A3%D1%81%D0%BF%D0%B5%D1%88%D0%BD%D0%BE%D0%B5%20%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D0%B0.png)

**ВНИМАНИЕ!** Для успешного добавления в базу ВСЕ поля должны быть заполнены, иначе программа вернёт Вас в окно заполнения информации с соответсвующем оповещением.

![ALERT](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%94%D0%BE%D0%BB%D0%B6%D0%BD%D1%8B%20%D0%B1%D1%8B%D1%82%D1%8C%20%D0%B7%D0%B0%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D0%BF%D0%BE%D0%BB%D1%8F.png)

4. Найти артикул

Вы можете выбрать параметр для поиска - по артикульному номеру, по номенклатурной группе, по коду номенклатурной группы.
   
![search art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%9C%D0%B5%D0%BD%D1%8E%20%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0.png)

- Поиск по артикулу

Введите корректный артикульный номер и программа покажет Вам всю информацию о нем (номенклатурную группу, код номенклатурной группы, цену и средние продажи за 6 мес в рублях и штуках). В случае некорректного ввода программа ничего не выведет, а Вам будет доступен возврат в меню для повторного ввода.

![search art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%BF%D0%BE%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%83.png)

![search art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%20%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0%20%D0%BF%D0%BE%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%83.png)

- Поиск по номенклатурной группе

Введите корретное наименование номенклатурной группы и программа покажет Вам все товары, относящиеся к этой номенклатурной группе с дополнительной информацией о каждом артикуле (номенклатурная группа, код номенклатурной группы, цена в рублях, средние продажи за 6 месяцев в рублях и штуках). В случае некорректного ввода программа ничего не выведет, а Вам будет доступен возврат в меню для повторного ввода.

![search art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%BF%D0%BE%20%D0%BD%D0%BE%D0%BC%D0%B5%D0%BD%D0%BA%D0%BB%D0%B0%D1%82%D1%83%D1%80%D0%BD%D0%BE%D0%B9%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B5.png)

![search art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%20%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0%20%D0%BF%D0%BE%20%D0%BD%D0%BE%D0%BC%D0%B5%D0%BD%D0%BA%D0%BB%D0%B0%D1%82%D1%83%D1%80%D0%BD%D0%BE%D0%B9%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B5.png)

- Поиск по коду номенклатурной группы

Введите корретный код номенклатурной группы и программа покажет Вам все товары, относящиеся к этой номенклатурной группе с дополнительной информацией о каждом артикуле (номенклатурная группа, код номенклатурной группы, цена в рублях, средние продажи за 6 месяцев в рублях и штуках). В случае некорректного ввода программа ничего не выведет, а Вам будет доступен возврат в меню для повторного ввода.

![search art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%BF%D0%BE%20%D0%BA%D0%BE%D0%B4%D1%83%20%D0%BD%D0%BE%D0%BC%D0%B5%D0%BD%D0%BA%D0%BB%D0%B0%D1%82%D1%83%D1%80%D0%BD%D0%BE%D0%B9%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%8B.png)

![search art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%20%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0%20%D0%BF%D0%BE%20%D0%BA%D0%BE%D0%B4%D1%83%20%D0%BD%D0%BE%D0%BC%D0%B5%D0%BD%D0%BA%D0%BB%D0%B0%D1%82%D1%83%D1%80%D0%BD%D0%BE%D0%B9%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%8B.png)

5. Изменить цену

В программе доступно изменение цены товара. Откроется поле для ввода артикульного номера, цену которого Вы хотите изменить и следом окно для ввода новой цены. В случае корректного водда появится сообщение об упешном изменении цены и по поиску у артикула уже будет отображаться новая цена. 

![change price](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%98%D0%B7%D0%BC%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%86%D0%B5%D0%BD%D1%8B%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB.png)
![change price](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%98%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%86%D0%B5%D0%BD%D1%8B%20%D1%86%D0%B5%D0%BD%D0%B0.png)

![change price](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%A6%D0%B5%D0%BD%D0%B0%20%D1%83%D1%81%D0%BF%D0%B5%D1%88%D0%BD%D0%BE%20%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B0.png)

![change price](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%20%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20%D1%86%D0%B5%D0%BD%D1%8B.png)

6. Удалить артикульный номер

Введите артикульный номер для удаления товара из базы.

![delete art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%A3%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%86%D0%B5%D0%BD%D1%8B.png)
![delete art](https://github.com/Fenri4ka/For-GB-lessons/blob/main/base/screenshoots/%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%20%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D0%B0.png)

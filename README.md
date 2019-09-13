# Взламываем электронный дневник

![взломщик Вова](https://dvmn.org/media/lessons/Django_1-st_LVl_004.png)

Данный скрипт предназначен для удаления плохих оценок в электронном дневнике, замечаний и добавления добрых слов в адрес любого ученика школы N.

## Как запустить
 Данный скрипт адаптирован под проект https://github.com/devmanorg/e-diary/tree/master. 
 
 Для начала необходимо его скачать и запустить (инструкции по запуску ищите в Readme.md).
 
 Далее скачиваем скрипт и располагаем его папке с файлом manage.py.
 
 Для запуска скрипта вам понадобится shell. 
 
 ``pip install shell`` 
 
 В вашем распоряжении 3 функции:
 1) Для создания похвалы ученику - ``create_commendation(name, subject)``, где name - имя ученика, subject - предмет, по которому хочется получить похвалу.
 2) Для исправления всех плохих оценок (2 и 3) на 5 - ``fix_marks(child)``, где child - экземпляр модели Schoolkid.
 3) Для удаления всех замечаний ученика - ``remove_chastisements(child)``,  где child - экземпляр модели Schoolkid.
## Примеры использования для каждой функции
 Командой ``python manage.py shell`` мы запускаем shell
 
 Импортируем нужную функцию командой ``from scripts import create_commendation``
 
 Для проверки заходим в электронный дневник на страничку текущего ученика и исследуем ее данные. В данном случае заостряем свое внимание на комментариях учителей по поводу поведения ученика. Запускаем. 
 
 ``create_commendation('Фролов Иван')``
 
 Должна появится рандомная похвала. 
 
 Для функций ``fix_marks(child)`` и ``remove_chastisements(child)`` добываем экземпляр модели Schoolkid командой:
 
 ``child=Schoolkids.objects.get(full_name__contains="Фролов Иван")``
 
 Заостряем свое внимание на оценках и замечаниях нужного ученика (в данном случае Фролова Ивана) и запускаем функции. 
 В результате все плохие оценки стали пятерками, а замечания удалены! 

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/) 

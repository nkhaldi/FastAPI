#### Используя FastAPI создать:

1. Эндпоинт для загрузки и обработки файла bills.csv<br>
    В базу писать только валидные счета. Счет считается валидным, если выполнены все условия:
    + значение sum является числом
    + в service не пусто ( пусто так же считается, если вместо текста знак “-”)
    + корректная дата (дата считается корректной, если есть день, месяц и год).
    + №(номер счета) тип  int
    + указаны client_name и client_org

2. Эндпоинт со списком счетов с возможностью фильтровать по организации, клиенту.<br>
    Отображать нужно всю информацию по счету, что была в bills.csv
<br>

Пояснения к данным в файле bills.csv:<br>
+ Множество значений в колонке service конечно. По сути это справочник.<br>
+ У одного client_name может быть несколько разных client_org<br>
+ № счета уникален для client_name и client_org (к примеру OOO Client1Org1 клиента client1 не может иметь более одного счета с № 1 и тд.)<br>
<br>

Если нет опыта с FastAPI можно использовать DRF или Flask

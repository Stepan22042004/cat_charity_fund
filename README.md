# Проект Cat charity fund 

Приложение для Благотворительного фонда поддержки котиков QRKot. 
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

### Как запустить проект:  

```  

git clone git@github.com:Stepan22042004/cat_charity_fund.git

```  

```  

cd cat_charity_fund

```  

Cоздать и активировать виртуальное окружение:  

```  

python3 -m venv venv  


```  

* Если у вас Linux/macOS  

```  

    source venv/bin/activate  

```  



* Если у вас windows  
```
source venv/scripts/activate  

 ```  

Установить зависимости из файла requirements.txt:  

```  

python3 -m pip install --upgrade pip  

```  

```  
pip install -r requirements.txt  

```  

Создание базы данных:  

```  
alembic upgrade head 

```  

Команда запуска:  

```  

flask run uvicorn app.main:app --reload
```  
### Стек использованных технологий  

### Язык программирования и фреймворк:  

- **Python**: основной язык программирования. 

- **FastApi**
### Тестирование:  

- **Pytest**: для написания тестов.  

### Информация об авторе  

 

Герасимов Степан  

[Stepan_2204](https://t.me/Stepan_2204)

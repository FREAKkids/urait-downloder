# Программа для скачиваняи книг с urait.ru

#### Если вам лень читать и разбираться в мат. части, то вы можите скачать готовый [репозиторий](https://github.com/FREAKkids/urait-downloder/releases/tag/v1)


### Однако, для тех, кто готов проявить терпение, давайте разберём всё по порядку. 

## Установка и настройка:

### Необходимые библиотеки:
```
pip install PyPDF2 pytesseract pdf2image tqdm win11toast python-environ pypdf svglib
```

### 1. Скрипт скачивания книг
Данный скрипт вы можите скачать из [источника](https://github.com/SergeiPopov/UraitDownloader.git), либо же скачав мой полный репозиторий.

После копирования репозитория необходимо указать данные от аккауната urait в файле account.txt . (Это нужно для предоставления доступа к книгам).

### 2. Далее скачиваем ( если же вы не скачали мой репозиторий) скрипт [convert.py](/convert.py).

#### P.s Желательно чтобы файлы всего проекта были в одной папке.

Далее нам необходимо установить и скачать в директорию проекта [pytesseract](https://github.com/UB-Mannheim/tesseract/wiki?spm=a2ty_o01.29997173.0.0.2e3ac921xCpn4O)  и нужный [языковой фильтр](https://github.com/tesseract-ocr/tessdata.git) в моём случае это русский (rus.traineddata). 

После установки перекидываем языковой фильтр по пути:  "\UraitDownloader-main\tessdata".

Если же у вас другой языковой фильтр, необходимо изменить его :
```
23 text = pytesseract.image_to_pdf_or_hocr(image, lang='rus', extension='pdf')
```
Поменяв параметр lang='rus' на другой язык.

После необходимо прописать путь к pytesseract : 
```
9 pytesseract.pytesseract.tesseract_cmd = r'*путь до директории*\UraitDownloader-main\tesseract.exe'
```


Так же необходимо скачать [poppler](https://github.com/oschwartz10612/poppler-windows.git) и так же указать к нему путь :
```
49 poppler_path = r"UraitDownloader-main\poppler-24.08.0\Library\bin"  # Путь к Poppler
```

## Запуск :

### 1. Запускаем первый скрипт [main.py](/main.py).
В процессе запуска скрипта вам необходимо указать ссылку на книгу ( пример ссылки : https://urait.ru/author-course/osnovy-finansovoy-gramotnosti-567612). 

ОБЯЗАТЕЛЬНО !!! На книгу, а не на ссылку просмотра.

### 2. Далее переходим в скрипт [convert.py](/convert.py), и вписываем название PDF файла, который у нас скачался:

```
47 input_pdf = "Основы финансовой грамотности.pdf"  
```

Если вы всё сделали правильно, и на первичном уровне у вас не выдало ошибок, то необходимо подождать пару минут ( т.к pytesseract загружается на быстро). А после наблюдаем за шкалой выполнения программы в консоле. В результате у вас появится файлик "Выход.pdf".

В полученном файле уже можно спокойно копировать текст из книг

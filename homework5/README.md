## Домашнее задание №5: Backend: Linux
### Описание работы скриптов:
### Python
* В пакете *log_components* реализованы классы для представления логов в удобном формате:
    + *local time* - класс времени в формате [Дата; GMT]
    + *user agent* - класс http user agent (Пустой, поскольку содержит в себе достаточно много полей, сферы ответственности которых не столь важны и не используются в данной задаче)((И потому что мне было лень в них разбираться))
    + *request line* - класс строки файла с логами, содержащий в себе данные, для удобного использования в последующих методах
* Файл methods.py содержит вспомогательные методы для парсинга файла логов и представления их в удобном формате:
  + Метод открывает исходный файл с логами и парсит его в массив строк представления RequestLine:
    ```python
    @staticmethod
    def get_requests_lines():
        with open('python_code/access.log') as file:
            lines = file.readlines()
        requests_lines = [RequestLine(*i.split(' ')) for i in lines]
        return requests_lines
    ```
  + Метод возвращает урлы всех запросов:
    ```python
    def get_urls(self):
    urls = [line.request_url for line in self.lines]
    return urls
    ```
  + Метод возвращает тип запроса и количество запросов данного типа в лог файле:
  ```python
  def get_request_count_by_type(self, request_type):
    res = 0
    for i in self.lines:
        if request_type in i.request_type:
            res += 1
    return request_type, res
  ```
  + Метод возвращает запросы, статус которых удовлетворяет шаблону *status_pattern*, переданному в качестве параметра:
  ```python
  def get_requests_by_request_status(self, status_pattern):
    res = []
    for i in self.lines:
        if re.search(status_pattern, i.request_status):
            res.append(i)
    return res
  ```
  + Метод возвращает всевозможные типы запросов, присутствующих в лог файле:
  ```python
  def get_request_types(self):
    types = set()
    for i in self.lines:
        types.add(i.request_type)
    return types
  ```
* Файл main.py содержит основную логику кейсов, представленных в задании:
  + Метод пишет в файл строку:
  ```python
    def write(self, *text):
        self.file.write(str(text) + "\n")
  ```
  + Метод пишет в файл каждый тип запроса и его количество в лог файле:
  ```python
    def print_request_count_by_type(self):
        request_types = self.methods.get_request_types()
        for request_type in request_types:
            self.write(self.methods.get_request_count_by_type(request_type))
  ```
  + Метод пишет в файл общее количество запросов:
  ```python
    def print_request_count(self):
        lines = self.methods.lines
        self.write(len(lines))
  ```
  + Метод пишет в файл первые *top* самых частых запросов (url и количество):
  ```python
    def print_top_requests(self, top):
        urls = self.methods.get_urls()
        urls_dict = {}
        for url in urls:
            urls_dict.update({url: urls_dict.get(url, 0) + 1})
        cnt = 0
        for url in sorted(urls_dict, key=urls_dict.get, reverse=True):
            self.write(url, urls_dict.get(url))
            cnt += 1
            if cnt == top:
                break
  ```
  + Метод пишет в файл *top* самых больших по размеру запросов, которые завершились клиентской (4XX) ошибкой:
  ```python
    def print_top_memory_4XX_error_requests(self, top):
        requests = sorted(self.methods.get_requests_by_request_status("4.."), key=lambda x: int(x.body_bytes_send),
                          reverse=True)
        cnt = 0
        for i in requests:
            self.write(i.request_url, i.request_status, i.body_bytes_send, i.ip)
            cnt += 1
            if cnt == top:
                break
  ```
  + Метод пишет в файл *top* пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:
  ```python
    def print_top_users_5XX_error_requests(self, top):
        requests = self.methods.get_requests_by_request_status("5..")
        requests_dict = {}
        for request in requests:
            requests_dict.update({request.ip: requests_dict.get(request.ip, 0) + 1})
        cnt = 0
        for request in sorted(requests_dict, key=requests_dict.get, reverse=True):
            self.write(request, requests_dict.get(request))
            cnt += 1
            if cnt == top:
                break
  ```
Результаты представлены в файлике *result.txt*

### Bash
* Скрипт для подсчёта запросов:
```shell
echo "----------Requests amount:----------" > result.txt
wc -l < access.log >> result.txt
```
Функция *wc -l* возвращает количество строк из потока данных
* Скрипт для подсчёта количества запросов каждого типа
```shell
echo "----------Requests amount by type (amount, type):----------" >> result.txt
awk '{print $6}' access.log | cut -c 2- | sort | uniq -c | sort -rn >> result.txt
```
Функция *awk '{print $6}'* печатает 6-й столбец каждой строки из потока данных (В данном случае тип запроса),

*cut -c 2-* возвращает переданную строку без первого символа (необходимо, поскольку полученные столбцы с типом запроса имели в начале символ "),

*sort | uniq -с* сортирует поток и возвращает уникальные элементы, а также их количество

*sort -rn* сортирует по убыванию и используя сортировку по числовому значению, а не по строковому
* Скрипт для подсчёта 10 самых частых запросов
```shell
echo "----------10 the most frequent requests (amount, url):----------" >> result.txt
awk '{print $7}' access.log | sort | uniq -c | sort -rn | head -n 10 >> result.txt
```
Функция *awk '{print $7}'* печатает url запроса,

*head -n 10* возвращает первые 10 строк потока

* Скрипт для подсчёта 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой
```shell
echo "----------5 the biggest requests with request status 4XX (url, status code, size, ip):----------" >> result.txt
awk '{print $7, $9, $10, $1}' access.log | grep -E ' 4.. ' | sort -rnk3 | head -n 5 >> result.txt
```
Функция *awk '{print $7}'* печатает url, status code, size, ip запроса соответственно,

*grep -E ' 4.. '* возвращает строки, в которых присутствует искомое регулярное выражение, что соответствует наличию статуса запроса вида 4XX

*sort -rnk3* сортирует поток в обратном порядке по числовому значению третьего столбца потока

* Скрипт для подсчёта топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой
```shell
echo "----------Top-5 users by amount of requests with status 5XX (amount, ip):----------" >> result.txt
awk '{print $1, $9}' access.log | grep -E ' 5..$' | sort | uniq -c | sort -rn | head -n 5 | awk '{print $1, $2}' >> result.txt
```
Функция *awk '{print $1, $9}'* печатает ip и status code запроса

### Выводы
Нетрудно заметить, что скрипты на баше и питоне возвращают одинаковый результат, при этом код на баше значительно компактнее и требует
минимальных знаний языка, в то время как скрипт на питоне более гибкий и расширяемый, ввиду наличия шаблонизированных методов, которые удобно переиспользовать, а также не содержит хард-кода (магических чисел в виде номеров используемых столбцов) благодаря классу строки запроса, в котором каждому столбцу присвоено говорящее имя

P.S. Из артефактов найден только невалидный тип запроса, который можно увидеть в файле с результатами
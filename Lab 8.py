from collections import namedtuple

# Создаем именованный кортеж для хранения информации о сетевом запросе
Request = namedtuple('Request', ['url', 'method', 'timestamp'])

# Пример данных сетевых запросов
requests = [
    Request('example.com', 'GET', '2024-04-02 12:00:00'),
    Request('example.com', 'POST', '2024-04-02 12:05:00'),
    Request('example.org', 'GET', '2024-04-02 12:10:00'),
]

# Функция для фильтрации запросов по URL
def filter_requests_by_url(url):
    return lambda req: req.url == url

# Функция для форматирования запроса в строку
def format_request(req):
    return f'{req.method} {req.url} - {req.timestamp}'

# Функция для обработки сетевых запросов
def process_network_requests(requests, filter_func, format_func):
    filtered_requests = filter(filter_func, requests)
    formatted_requests = map(format_func, filtered_requests)
    return list(formatted_requests)

# Пример использования функций для мониторинга сетевых запросов к 'example.com'
filtered_requests = process_network_requests(requests, filter_requests_by_url('example.com'), format_request)

# Вывод отформатированных запросов
for req in filtered_requests:
    print(req)
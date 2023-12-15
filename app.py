def task_1(test_text: str, list_keys: list) -> str:
    for elem in list_keys:
        if elem in test_text:
            continue
        else:
            return f'Ошибка: {elem} нет в сообщении.'

    return 'Сообщение корректно.'


def task_2(list_version: list[list]) -> list[list]:
    dict_version = dict()
    for elem in list_version:
        if tuple(elem) not in dict_version:
            dict_version[tuple(elem)] = 0
        dict_version[tuple(elem)] += 1

    list_result = list()
    for key, value in dict_version.items():
        list_result.append([f'{key[0]}, {key[1]}, {value}'])

    return list_result


def recursive(obj, dict_result):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict):
                recursive(value, dict_result)
            else:
                dict_result[key] = value
    return dict_result


def task_3(json_old: dict, json_new: dict) -> dict:
    json_old = recursive(json_old, dict())
    json_new = recursive(json_new, dict())

    dict_result = dict()
    for key, value in json_new.items():
        if json_old[key] != json_new[key]:
            dict_result[key] = json_new[key]

    return dict_result


def task_4():
    return '''Для реализации периодической очистки можно воспользоваться следующим методом:
    expiration_time = datetime.datetime.now() - datetime.timedelta(hours=24)  # вычисляем время, прошедшее 24 часа назад
    query = {"expiration_time": {"$lt": expiration_time}}  # формируем запрос для выборки устаревших документов
    result = collection.delete_many(query)  # удаляем устаревшие документы

    while True:
        clean_expired_data()
        time.sleep(24 * 60 * 60)  # Ожидание 24 часа до следующего запуска'''


def task_5():
    return '''
    1. Входящий запрос: Все входящие веб-хуки будут направляться на один URL-адрес или endpoint на сервере. Например, /webhook.
    2. Маршрутизация запросов: При поступлении запроса на /webhook, сервер будет маршрутизировать запросы на различные обработчики на основе типа веб-хука или других параметров в запросе. Например, в зависимости от заголовка запроса или данных в теле запроса, можно определить, какой обработчик должен быть вызван.
    3. Обработчики: Каждый тип веб-хука будет иметь свой собственный обработчик, который будет выполнять нужные действия в ответ на входящий веб-хук. Это может включать сохранение данных в базу данных, обновление состояния системы, отправку уведомлений и другие действия, которые необходимо выполнить.
    4. Асинхронность: Можно рассмотреть возможность обработки входящих веб-хуков асинхронно. Вместо блокирования ответа на запрос, endpoint может добавлять входящие веб-хуки в очередь или использовать систему сообщений для дальнейшей обработки. Сервер сможет мгновенно отвечать на запросы, не ожидая завершения обработки веб-хука.
    
    Примерная реализация:
    from flask import Flask, request
    from multiprocessing import Process, Queue

    app = Flask(__name__)

    webhook_queue = Queue()

    def process_webhook(payload):
        print("Received webhook payload:", payload)
    
    def process_webhook_queue():
        while True:
            payload = webhook_queue.get()
            process_webhook(payload)
    
    @app.route('/webhook', methods=['POST'])
    def webhook():
        payload = request.json
        webhook_queue.put(payload)
        return "Webhook received and queued for processing", 200
    
    if __name__ == '__main__':
        webhook_process = Process(target=process_webhook_queue)
        webhook_process.start()
    
        app.run()
        '''


if __name__ == '__main__':
    print('TASK 1:')
    test_text_example = '''{name}, ваша запись изменена:
    {day_month} в {start_time}
    {master}
    Услуги:
    {services}
    управление записью {record_link}'''
    list_keys_example = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']
    print(task_1(test_text_example, list_keys_example))
    print('\n')

    print('TASK 2:')
    list_version_example = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]
    print(task_2(list_version_example))
    print('\n')

    print('TASK 3:')
    json_old_example = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id': 11111111, 'company_id': 111111, 'services': [{'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T11:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed': 1, 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False, 'paid_full': 0, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}
    json_new_example = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id': 11111111, 'company_id': 111111, 'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T13:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 2, 'confirmed': 1, 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False, 'paid_full': 1, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}
    print(task_3(json_old_example, json_new_example))
    print('\n')

    print(task_4())
    print('\n')

    print(task_5())

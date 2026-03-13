# Ксения Пирожок, 41 когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

# Клиент создает заказ.
# Проверяется, что по треку заказа можно получить данные о заказе.
def test_create_order_and_get_order_id():

    # 1. Выполнить запрос на создание заказа
    response = sender_stand_request.post_new_order(data.create_order)
    
    # 2. Сохранить номер трека заказа
    track_id = response.json()["track"]

    # 3. Выполнить запрос на получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track_id)

    # 4. Проверить, что код ответа равен 200
    assert get_response.status_code == 200
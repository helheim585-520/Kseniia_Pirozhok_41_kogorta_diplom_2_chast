import requests
import configuration
import data

# Создание заказа POST
def post_new_order(create_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=create_order)

# Получение заказа по его номеру
def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK_PATH,
                        params={"t": track_number})
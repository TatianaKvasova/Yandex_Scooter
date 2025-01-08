#Татьяна Квасова, 25-я когорта, дипломный проект Яндекс Самокат
import create_new_order
import data

def get_new_track(order_response):
    return order_response.json().get("track")

data.params_get["t"] = get_new_track(create_new_order.order_response)

# Автотест
def positive_assert():
    track_response = create_new_order.get_order(data.params_get)
    assert track_response.status_code == 200


def test_order():
    positive_assert()
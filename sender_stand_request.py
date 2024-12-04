import requests

import configuration  # определили url-ы
import post_data  # данные создаваемого пользователя

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=post_data.headers)


def post_products_kits(products):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products,
                         headers=post_data.headers)

#response = get_users_table()
#response = post_new_user(post_data.user_body)

response = post_products_kits(post_data.product_ids)

print(response.status_code)
print(response.json())
# print(*response.json()[0].values())
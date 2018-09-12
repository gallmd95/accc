import server.server as server
import client.client as client
from threading import Thread
from os import environ

if __name__ == "__main__":
    email = environ['EMAIL']
    name = environ['NAME']
    key = environ['API_KEY']
    addr = environ['ADDRESS']
    country = environ['COUNTRY']
    url = environ['SERVER_URL']
    api_url = environ['API_URL']
    text_path = environ['TEXT_PATH']
    html_path = environ['HTML_PATH']

    thread = Thread(target=server.start)
    thread.start()
    app = client.App(api_url, key)
    contact_emails = [
        'officonnyrre-8014@yopmail.com',
        'atulohimm-6073@yopmail.com',
        'isulennic-7520@yopmail.com',
        'umattace-8372@yopmail.com'
    ]
    list_r = app.create_list("ActiveCampaign Challenge", addr, country, url)
    list_id = list_r.json()['id']
    create_contact_with_list_id = lambda x : app.create_contact(x, list_id)
    map(create_contact_with_list_id, contact_emails)
    msg_r = app.create_message('ActiveCampaign Challenge', email, name, email, url, html_path, text_path, list_id)
    msg_id = msg_r.json()['id']
    app.create_campaign('2019-09-11 12:30:00', list_id, msg_id)
    



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
    print_res = lambda r, i : print(r.json()['result_message'] + (' id: ' + str(r.json()[i]) if i in r.json() else ''))

    contact_emails = [
        'officonnyrre-8014@yopmail.com',
        'atulohimm-6073@yopmail.com',
        'isulennic-7520@yopmail.com',
        'umattace-8372@yopmail.com'
    ]
    list_r = app.create_list("ActiveCampaign Challenge", addr, country, url)
    list_r.raise_for_status()
    list_id = list_r.json()['id']
    print_res(list_r, 'id')
    create_contact_with_list_id = lambda x : app.create_contact(x, list_id)
    for each in map(create_contact_with_list_id, contact_emails):
        each.raise_for_status()
        print_res(each, 'subscriber_id')
    msg_r = app.create_message('ActiveCampaign Challenge', email, name, email, url, html_path, text_path, list_id)
    msg_r.raise_for_status()
    print_res(msg_r, 'id')
    msg_id = msg_r.json()['id']
    addr_r = app.create_address(addr, country, list_id)
    addr_r.raise_for_status()
    print_res(addr_r, 'id')
    cmp_r = app.create_campaign('2018-09-12 8:30:00', list_id, msg_id)
    cmp_r.raise_for_status()
    print_res(cmp_r, 'id')
    



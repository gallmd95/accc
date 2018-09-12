import requests
import copy

class App (object):

    def __init__(self, url, key):
        self.key = key
        self.url = url
        self._default_params = {
            'api_action': None,
            'api_key': self.key,
            'api_output': 'json'
        }

    def create_campaign(self, sdate, list_id, msg_id):
        params = copy.deepcopy(self._default_params)
        params['api_action'] = 'campaign_create'
        payload = {
            'type': 'single',
            'segmentid': 0, 
            'bounceid': -1, 
            'name': 'ActiveCampaign Challenge', 
            'sdate': sdate, 
            'status': 1, 
            'public': 1, 
            'tracklinks': 'all', 
            'trackreads': 1, 
            'trackreplies': 0, 
            'htmlunsub': 1, 
            'textunsub': 1, 
            'p['+str(list_id)+']': list_id, 
            'm['+str(msg_id)+']': 100
        }
        return requests.post(self.url, params=params, data=payload)

    def create_list(self, name, addr, country, url):
        params = copy.deepcopy(self._default_params)
        params['api_action'] = 'list_add'
        payload = {
            'name': name, 
            'sender_addr1': addr, 
            'sender_country': country,
            'sender_name': 'Company',
            'zip': '60606',
            'city': 'Chicago',
            'sender_url': url,
            'sender_reminder': "Just bad luck."
        }
        return requests.post(self.url, params=params, data=payload)

    def create_contact(self, email, list_id):
        params = copy.deepcopy(self._default_params)
        params['api_action'] = 'contact_add'
        payload = {'email': email, 'p['+str(list_id)+']': list_id, 'status': 1}
        return requests.post(self.url, params=params, data=payload)

    def create_message(self, subject, email, name, reply, url, html_path, text_path, list_id):
        params = copy.deepcopy(self._default_params)
        params['api_action'] = 'message_add'
        payload = {
            'format': 'mime',
            'subject': subject,
            'fromemail': email,
            'fromname': name,
            'reply2': reply,
            'priority': 3,
            'charset': 'utf-8',
            'encoding': 'quoted-printable',
            'htmlconstructor': 'external',
            'htmlfetch': url + html_path,
            'htmlfetchwhen': 'send',
            'textconstructor': 'external',
            'textfetch': url + text_path,
            'textfetchwhen': 'send',
            'p['+str(list_id)+'}': list_id
        }
        return requests.post(self.url, params=params, data=payload)
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


class Parser(object):

    wsh = None

    def __init__(self):
        json_key = json.load(open('rainr/instance/Rainr-da2ea2640cb3.json'))
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = SignedJwtAssertionCredentials(
            json_key['client_email'], json_key['private_key'], scope
        )

        gc = gspread.authorize(credentials)

        sh = gc.open('Rain in Bern')
        self.wsh = sh.sheet1

    def get_rain_data(self):
        rain = self.wsh.col_values(2)

        rain_data = {}
        data = []

        for item in rain:
            if item in rain_data:
                rain_data[item] += 1
            else:
                rain_data[item] = 1

        for item in rain_data.keys():
            data.append([str(item), rain_data[item]])

        return data

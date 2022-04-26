import csv
import json
from contextlib import closing
from typing import Dict
from client import RequestsClient, Client
import constants as c


class ServiceSii():

    url = 'https://www.sii.cl/'

    def __init__(self, client: Client):
        self.client = client

    def _get_full_url(self, patch: str) -> str:
        return f'{ServiceSii.url}{patch}'

    def get_data_nomina(self, patch) -> Dict[str, Dict[str, str]]:

        csv_patch: str = patch.replace('html', 'csv')
        url: str = self._get_full_url(csv_patch)
        payload = {}

        with closing(self.client.get(url, stream=True)) as r:
            lines = (
                line.decode(encoding='UTF-8')
                    for line in r.iter_lines()
            )
            rows = csv.reader(lines, delimiter=';')
            next(rows)
            for row in rows:
                payload[row[c.ID]] = {
                    'social_reazon': row[c.SOCIAL_REASON],
                    'country': row[c.COUNTRY],
                    'dr_inscription': row[c.DR_INSCRIPTION],
                    'rs_inscription': row[c.INSCRIPTION_RESOLUTION],
                    'date_inscription': row[c.INSCRIPTION_DATE],
                    'valid_until': row[c.VALID_UNTIL],
                    'dr_update': row[c.DR_UPDATE],
                    'resolution_update': row[c.RESOLUTION_UPDATE],
                    'date_update': row[c.DATE_UPDATE],
                    'status': row[c.STATUS]
                }
        return payload

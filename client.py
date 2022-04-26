from abc import ABC, abstractmethod

from requests import Request, Session
from typing import Dict


class Client(ABC):

    @abstractmethod
    def request(
        self,
        method: str,
        url: str,
        data: Dict[str, str] = None,
        **kwargs
    ):
        pass

    @abstractmethod
    def get(self, url: str):
        pass


class RequestsClient(Client):

    def request(
        self,
        method: str,
        url: str,
        data: Dict[str, str] = None,
        **session_kwargs: Dict[str, any]
    ):
        try:
            session = Session()
            req = Request(method, url, data=data)
            prepped = session.prepare_request(req)
            return session.send(prepped, **session_kwargs)
        except Exception:
            error_message = f'Url may be wrong. url: {url}'
            raise ValueError(error_message)


    def get(self, url: str, **session_kwargs):
        return self.request('GET', url, **session_kwargs)

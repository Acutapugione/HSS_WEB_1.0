from os import getenv
from requests import get, post, put

class API_Worker:

    # host:str = getenv("API_HOST") or "localhost"
    # port:int = getenv("API_PORT") or 8000

    def __init__(self,  **kwargs)->None:
        self.host = kwargs.get("host")
        self.port = kwargs.get("port")

    def get_messages(self, _filter=None)->list:
        url = self._prepare_url("message")
        try:
            response = get(url)
            if response.status_code == 200:
                if _filter:
                    return list(filter(_filter, [x for x in response.json()]))
                return [x for x in response.json()]
        except Exception as e:
            print(f"Exception:{e}")

    def post_message(self, message):
        url = self._prepare_url("message")
        try:
            response = post(url, json=message)
            if response.status_code == 200:
                return True
        except Exception as e:
            print(f"Exception:{e}")
     


    def _prepare_url(self, endpoint)->str:
        if self.port:
            return f"{self.host}:{self.port}/{endpoint}"
        return f"{self.host}/{endpoint}"
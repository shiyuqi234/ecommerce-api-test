import requests


class APIClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.token = None

    def set_token(self, token):
        self.token = token
        self.session.headers["Cookie"] = f"token={token}"

    def get(self, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.get(f"{self.base_url}{path}", **kwargs)

    def post(self, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.post(f"{self.base_url}{path}", **kwargs)

    def put(self, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.put(f"{self.base_url}{path}", **kwargs)

    def patch(self, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.patch(f"{self.base_url}{path}", **kwargs)

    def delete(self, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.delete(f"{self.base_url}{path}", **kwargs)
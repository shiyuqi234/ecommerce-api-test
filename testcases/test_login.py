import pytest
import yaml
import logging

logger = logging.getLogger("ecommerce_test")


def load_login_data():
    with open("data/login_data.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)["login_cases"]


class TestLogin:
    @pytest.mark.parametrize("case", load_login_data())
    def test_login(self, client, case):
        payload = {k: v for k, v in case.items() if k not in ("name", "expected_code")}
        logger.info(f"[登录] {case['name']} -> POST /auth/login {payload}")
        resp = client.post("/auth/login", json=payload)

        assert resp.status_code // 100 == case["expected_code"] // 100

        if 200 <= resp.status_code < 300:
            assert "token" in resp.json()

        logger.info(f"[登录] {case['name']} -> {resp.status_code} {resp.text[:100]}")
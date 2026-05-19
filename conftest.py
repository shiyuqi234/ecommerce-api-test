import pytest
import yaml
import logging
from common.api_client import APIClient
from utils.logger import setup_logger


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logger = setup_logger()
    logger.info("=== 测试开始 ===")
    yield
    logger.info("=== 测试结束 ===")


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def client(config):
    return APIClient(config["base_url"], config["timeout"])


@pytest.fixture(scope="session")
def auth_token(client):
    payload = {"username": "mor_2314", "password": "83r5^_"}
    resp = client.post("/auth/login", json=payload)
    assert resp.status_code in (200, 201), f"登录失败: {resp.text}"
    token = resp.json().get("token")
    client.set_token(token)
    return token
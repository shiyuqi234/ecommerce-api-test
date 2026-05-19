import allure
import logging

logger = logging.getLogger("ecommerce_test")


@allure.feature("下单模块")
class TestOrder:

    @allure.title("正常下单")
    def test_place_order(self, client):
        logger.info("[下单] 正常下单 -> POST /carts")
        payload = {
            "userId": 1,
            "date": "2026-05-11",
            "products": [
                {"productId": 1, "quantity": 2},
                {"productId": 3, "quantity": 1}
            ]
        }
        resp = client.post("/carts", json=payload)
        assert resp.status_code == 201

        data = resp.json()
        assert "id" in data
        assert data["userId"] == 1
        assert isinstance(data["products"], list)
        assert len(data["products"]) == 2

        expected_products = [
            {"productId": 1, "quantity": 2},
            {"productId": 3, "quantity": 1}
        ]
        for expected, actual in zip(expected_products, data["products"]):
            assert actual["productId"] == expected["productId"]
            assert actual["quantity"] == expected["quantity"]

    @allure.title("空商品下单")
    def test_place_order_empty_products(self, client):
        logger.info("[下单] 空商品下单 -> POST /carts")
        payload = {
            "userId": 1,
            "date": "2026-05-11",
            "products": []
        }
        resp = client.post("/carts", json=payload)
        assert resp.status_code == 201

        data = resp.json()
        assert data["products"] == []

    @allure.title("缺少userId下单")
    def test_place_order_missing_userId(self, client):
        logger.info("[下单] 缺 userId -> POST /carts")
        payload = {
            "date": "2026-05-11",
            "products": [{"productId": 1, "quantity": 1}]
        }
        resp = client.post("/carts", json=payload)
        assert resp.status_code in (200, 201, 400)

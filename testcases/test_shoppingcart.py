import allure
import logging

logger = logging.getLogger("ecommerce_test")


@allure.feature("购物车模块")
class TestShoppingCart:

    @allure.title("查全部购物车")
    def test_get_all_carts(self, client):
        logger.info("[购物车] 查全部 -> GET /carts")
        resp = client.get("/carts")
        assert resp.status_code == 200

        data = resp.json()
        assert isinstance(data, list)

        for cart in data:
            assert "id" in cart
            assert "userId" in cart
            assert "date" in cart
            assert "products" in cart
            assert isinstance(cart["products"], list)
            assert len(cart["products"]) > 0

            for product in cart["products"]:
                assert "productId" in product
                assert "quantity" in product
                assert isinstance(product["productId"], int)
                assert isinstance(product["quantity"], int)
                assert product["quantity"] > 0

    @allure.title("查单个购物车")
    def test_get_cart_detail(self, client):
        logger.info("[购物车] 查单个 -> GET /carts/1")
        resp = client.get("/carts/1")
        assert resp.status_code == 200

        data = resp.json()
        assert isinstance(data, dict)
        assert data["id"] == 1
        assert isinstance(data["date"], str) and len(data["date"]) > 0
        assert isinstance(data["products"], list)
        assert len(data["products"]) > 0

        for product in data["products"]:
            assert "productId" in product
            assert "quantity" in product
            assert product["quantity"] > 0

    @allure.title("新增购物车")
    def test_add_cart(self, client):
        logger.info("[购物车] 新增 -> POST /carts")
        payload = {
            "userId": 1,
            "date": "2026-05-11",
            "products": [{"productId": 1, "quantity": 2}]
        }
        resp = client.post("/carts", json=payload)
        assert resp.status_code == 201

        data = resp.json()
        assert isinstance(data, dict)
        assert "id" in data
        assert data["userId"] == 1
        assert isinstance(data["products"], list)
        assert len(data["products"]) == 1
        assert data["products"][0]["productId"] == 1
        assert data["products"][0]["quantity"] == 2

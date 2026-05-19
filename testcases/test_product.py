import allure
import logging

logger = logging.getLogger("ecommerce_test")


@allure.feature("商品模块")
class TestProduct:

    @allure.title("查全部商品")
    def test_get_all_products(self, client):
        logger.info("[商品] 查全部商品 -> GET /products")
        resp = client.get("/products")

        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, list), f"期望列表，实际得到 {type(data)}"
        assert len(data) == 20, f"期望20个商品，实际得到 {len(data)} 个"

        for product in data:
            assert "id" in product, f"商品缺少 id 字段: {product}"
            assert "title" in product, f"商品缺少 title 字段: {product}"
            assert "price" in product, f"商品缺少 price 字段: {product}"
            assert isinstance(product["price"], (int, float))
            assert product["price"] > 0
            assert isinstance(product["description"], str) and len(product["description"]) > 0
            assert isinstance(product["category"], str) and len(product["category"]) > 0

    @allure.title("查商品详情")
    def test_get_product_detail(self, client):
        logger.info("[商品] 查商品详情 -> GET /products/1")
        resp = client.get("/products/1")

        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, dict), f"期望字典，实际得到 {type(data)}"
        assert data["id"] == 1, f"id 不匹配: {data['id']}"
        assert isinstance(data["title"], str) and len(data["title"]) > 0
        assert data["price"] > 0
        assert isinstance(data["description"], str) and len(data["description"]) > 0
        assert isinstance(data["category"], str) and len(data["category"]) > 0

import pytest


class TestProduct:
    """商品接口测试"""

    def test_get_all_products(self, client):
        """查全部商品"""
        # 1. 发请求
        resp = client.get("/products")

        # 2. 验证状态码
        assert resp.status_code == 200

        # 3. 解析响应体
        data = resp.json()

        # 4. 验证：返回的是列表
        assert isinstance(data, list), f"期望列表，实际得到 {type(data)}"

        # 5. 验证：FakeStore 固定有 20 个商品
        assert len(data) == 20, f"期望20个商品，实际得到 {len(data)} 个"

        # 6. 验证：每个商品都有 id/title/price 字段，且值合法
        for product in data:
            assert "id" in product, f"商品缺少 id 字段: {product}"
            assert "title" in product, f"商品缺少 title 字段: {product}"
            assert "price" in product, f"商品缺少 price 字段: {product}"
            assert isinstance(product["price"], (int, float)), f"price 类型不对: {type(product['price'])}"
            assert product["price"] > 0, f"price 应该大于0: {product['price']}"
            assert isinstance(product["description"], str) and len(product["description"]) > 0
            assert isinstance(product["category"], str) and len(product["category"]) > 0

    def test_get_product_detail(self, client):
        """查单个商品详情"""
        # 1. 发请求
        resp = client.get("/products/1")

        # 2. 验证状态码
        assert resp.status_code == 200

        # 3. 解析响应体
        data = resp.json()

        # 4. 验证：返回的是字典（单个对象）
        assert isinstance(data, dict), f"期望字典，实际得到 {type(data)}"

        # 5. 验证：id 和请求的 id 一致
        assert data["id"] == 1, f"id 不匹配: {data['id']}"

        # 6. 验证：字段存在且值合法
        assert isinstance(data["title"], str) and len(data["title"]) > 0, "title 为空或类型不对"
        assert data["price"] > 0, f"price 异常: {data['price']}"
        assert isinstance(data["description"], str) and len(data["description"]) > 0, "description 异常"
        assert isinstance(data["category"], str) and len(data["category"]) > 0, "category 异常"

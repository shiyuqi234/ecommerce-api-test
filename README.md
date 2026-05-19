# E-Commerce API Test

基于 Python + pytest + requests 的电商接口自动化测试项目。

被测系统：[FakeStore API](https://fakestoreapi.com)（模拟电商 RESTful 接口）

## 技术栈

- Python 3
- pytest
- requests
- PyYAML（数据驱动）
- Allure（测试报告）
- logging（日志）
- Git

## 项目结构

```
├── common/
│   └── api_client.py      # requests 封装，统一管理 Session 和 token
├── config/
│   └── config.yaml        # 接口地址、超时时间等配置
├── data/
│   └── login_data.yaml    # 登录测试数据（数据驱动）
├── logs/                  # 运行日志（自动生成）
├── reports/               # Allure 测试报告（自动生成）
├── testcases/
│   ├── test_login.py      # 登录接口测试
│   ├── test_product.py    # 商品接口测试
│   ├── test_shoppingcart.py # 购物车接口测试
│   └── test_order.py      # 下单接口测试
├── utils/
│   └── logger.py          # 日志配置
├── conftest.py            # pytest fixture（client、token、日志）
├── pytest.ini             # pytest 配置
└── requirements.txt       # 依赖清单
```

## 测试内容

| 文件 | 测试项 | 用例数 |
|------|--------|--------|
| test_login.py | 正确/错误密码登录 | 2 |
| test_product.py | 查全部商品、查商品详情 | 2 |
| test_shoppingcart.py | 查全部/单个购物车、新增购物车 | 3 |
| test_order.py | 正常下单、空商品下单、缺字段下单 | 3 |
| **合计** | | **10** |

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行所有测试
pytest

# 3. 生成 Allure 报告（需安装 Allure）
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

## 断言策略

- 状态码验证
- 响应体结构验证（字段存在性、类型、非空）
- 关键字段值验证（id 一致性、数量 > 0 等）
- 数据驱动（登录场景）

## TODO

- [ ] GitHub Actions 持续集成

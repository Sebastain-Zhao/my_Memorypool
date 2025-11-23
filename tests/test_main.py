"""
tests/test_main.py
"""
import pytest
import requests
# 从上一级目录导入 main.py 中的函数
# 注意：在 Jenkins 或根目录运行 pytest 时，Python 会自动找到 main
from main import add_numbers, check_website

# 测试用例 1: 测试纯逻辑
def test_add_numbers():
    assert add_numbers(1, 1) == 2
    assert add_numbers(-1, 1) == 0
    assert add_numbers(100, 200) == 300

# 测试用例 2: 测试网站检查 (使用 requests_mock 模拟网络，不用真连)
def test_check_website_success(requests_mock):
    # 模拟：当访问 google.com 时，强制返回 200 OK
    requests_mock.get("https://www.google.com", status_code=200)
    
    # 运行代码
    result = check_website("https://www.google.com")
    
    # 断言：结果应该是 True
    assert result is True

# 测试用例 3: 测试网站检查失败的情况
def test_check_website_failure(requests_mock):
    # 模拟：当访问 bad-url.com 时，强制返回 404 Not Found
    requests_mock.get("https://www.bad-url.com", status_code=404)
    
    result = check_website("https://www.bad-url.com")
    
    # 断言：结果应该是 False
    assert result is False
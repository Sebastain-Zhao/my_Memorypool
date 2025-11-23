"""
main.py
"""
import requests

def add_numbers(a, b):
    """一个简单的加法函数，用来演示单元测试"""
    return a + b

def check_website(url):
    """检查网站状态"""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
        return False
    except Exception:
        return False

if __name__ == "__main__":
    # 只有直接运行此文件时才会执行这里
    print(f"1 + 1 = {add_numbers(1, 1)}")
    check_website("https://www.github.com")
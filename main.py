import sys
import requests

def check_website(url):
    """检查网站是否能正常访问"""
    print(f"正在检查网站状态: {url} ...")
    try:
        response = requests.get(url, timeout=5)
        # 检查状态码是否为 200
        if response.status_code == 200:
            print(f"✅ 成功! 网站 {url} 运行正常。")
            return True
        else:
            print(f"❌ 失败! 状态码: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 错误! 无法连接到网站: {e}")
        return False

if __name__ == "__main__":
    # 比如检查 GitHub
    target_url = "https://www.github.com"
    success = check_website(target_url)
    
    # 如果失败，告诉系统出错了 (这会让 Jenkins 任务变红)
    if not success:
        sys.exit(1)

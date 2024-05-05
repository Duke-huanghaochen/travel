import time
import webbrowser

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"倒计时: {i}秒")
        time.sleep(1)

def open_default_browser():
    webbrowser.open("http://www.baidu.com")  # 在这里替换成你想要打开的网址

def main():
    countdown(3)  # 设置倒计时秒数
    print("启动默认浏览器...")
    open_default_browser()

if __name__ == "__main__":
    main()

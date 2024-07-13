from datetime import datetime
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f"函数 {func.__name__} 于 {start_time.ctime()} 开始执行...")

        result = func(*args, **kwargs)

        end_time = datetime.now()
        print(f"函数 {func.__name__} 于 {end_time.ctime()} 执行完毕！")
        return result

    return wrapper

# 示例用法
@log_execution_time
def example_function():
    # 模拟一些耗时操作
    time.sleep(2)
    print('函数执行结束！')

# 调用被装饰的函数
example_function()
'''
函数 example_function 于 Mon Jan  8 20:01:00 2024 开始执行...
函数执行结束！
函数 example_function 于 Mon Jan  8 20:01:02 2024 执行完毕！
'''

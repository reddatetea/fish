import time

class Timer:
    def __enter__(self):
        # 记录开始时间
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # 记录结束时间
        self.end_time = time.time()

        # 计算总运行时间并输出
        total_time = self.end_time - self.start_time
        print(f'Total execution time: {total_time:.6f} seconds')

# 示例用法
with Timer():
    # 在这个代码块中可以放入你想要计时的任何代码
    # 例如，这里放入一个简单的循环作为示例
    for _ in range(1000000):
        pass
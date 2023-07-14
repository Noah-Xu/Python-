import random
import numpy as np
import matplotlib.pyplot as plt

def simulate_delay_measurement(signal_strength, delay, num_samples, jitter_range):
    # 生成信号波形
    signal = np.zeros(num_samples)
    signal[num_samples // 2] = signal_strength  # 在中间位置设置信号强度

    # 模拟信号强度的抖动
    jitter = np.random.uniform(-jitter_range, jitter_range, num_samples)  # 生成信号强度的抖动

    # 计算模拟延时
    delays = np.zeros(num_samples)
    delays[num_samples // 2] = delay  # 在中间位置设置延时

    # 添加信号强度抖动对延时的影响
    delayed_delays = delays * (1 / (signal_strength + jitter))

    # 添加延时
    delayed_signal = np.roll(signal, np.round(delayed_delays).astype(int))

    return delayed_signal

# 示例用法
signal_strength = 1.0  # 假设信号强度为1.0
delay = 10  # 假设延时为10个采样点
num_samples = 1000  # 采样点数量
jitter_range = 0.2  # 信号强度的抖动范围

# 模拟延时和信号波形
delayed_signal = simulate_delay_measurement(signal_strength, delay, num_samples, jitter_range)

# 绘制信号波形
time = np.arange(num_samples)

plt.stem(time, delayed_signal, basefmt='b', linefmt='b', markerfmt='bo')
plt.xlabel('Time (samples)')
plt.ylabel('Amplitude')
plt.title('Simulated Delayed Pulse Signal')
plt.grid(True)

plt.show()
import math

print("=== 管道流速计算 ===")

# 直接给定参数，不用输入
diameter = 0.2        # 管道内径 (m)
flow_rate_m3h = 10.0  # 流量 (m³/h)

# 单位换算
flow_rate = flow_rate_m3h / 3600.0

# 计算截面积
area = math.pi * (diameter ** 2) / 4.0

# 计算流速
velocity = flow_rate / area

# 输出结果
print("\n计算结果：")
print(f"管径：{diameter:.4f} m")
print(f"流量：{flow_rate_m3h:.3f} m³/h  =  {flow_rate:.6f} m³/s")
print(f"流速：{velocity:.4f} m/s")

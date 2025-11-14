"""
demo.py
演示如何调用 simulate_pull.py 中的函数
Demo script showing how to call simulate_pull() from simulate_pull.py
"""

# 直接导入同目录下的 simulate_pull.py
# Directly import simulate_pull.py in the same folder
from simulate_pull import simulate_pull

def main():
    """
    主函数 / Main function
    """
    print("=== Docker Pull UI Simulator Demo ===")
    print("模拟拉取多个镜像 / Simulate pulling multiple images\n")

    # 示例镜像列表 / Example image list
    images = [
        ("elasticsearch", 723.4),
        ("redis", 120.0),
        ("opencti", 240.1),
    ]

    # 顺序拉取 / Sequential pulling
    for name, size in images:
        simulate_pull(name, size)

    print("\n=== All pulls completed / 所有镜像拉取完成 ===")

if __name__ == "__main__":
    main()

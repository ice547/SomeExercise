from argparse import Namespace

# 模擬命令行參數
vehicle = Namespace(
    color = "yellow",
    size  = "huge",
    verbose = True
)

# 使用參數
if vehicle.verbose:
    print(f"顏色: {vehicle.color}")
    print(f"大小: {vehicle.size}")
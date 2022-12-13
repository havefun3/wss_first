from ltp import LTP
ltp = LTP("E:\python3.8.5\Lib\site-packages\ltp_data_base1") # 默认加载 LTP/Small 模型

result = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks = ["cws","pos"])
print(result.pos)
# [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]
# [['r', 'v', 'nh', 'v', 'v', 'n', 'wp']]
from ltp import LTP

ltp = LTP("E:\python3.8.5\Lib\site-packages\ltp_data_base1") # 默认加载 LTP/Small 模型

result = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks = ["cws","dep"])
print(result.dep)

#最终结果
# [{'head': [2, 0, 2, 5, 2, 5, 2], 'label': ['SBV', 'HED', 'DBL', 'LAD', 'VOB', 'VOB', 'WP']}]
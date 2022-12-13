from ltp import LTP

ltp = LTP("E:\python3.8.5\Lib\site-packages\ltp_data_base1") # 默认加载 LTP/Small 模型

result = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks = ["cws","srl"])
print(result.srl)

## 结果如

##[[{'predicate': '叫', 'arguments': [('A0', '他'), ('A1', '汤姆'), ('A2', '去拿外衣')]}, {'predicate': '拿', 'arguments': [('A0', '汤姆'), ('A1', '外衣')]}]]
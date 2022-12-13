from ltp import LTP

ltp = LTP("E:\python3.8.5\Lib\site-packages\ltp_data_base1") #加载base1模型

words = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks = ["cws"], return_dict = False)
# [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]

print(words)
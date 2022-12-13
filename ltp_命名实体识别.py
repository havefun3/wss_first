from ltp import LTP

ltp = LTP("E:\python3.8.5\Lib\site-packages\ltp_data_base1") # 默认加载 LTP/Small 模型


result = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks = ["cws","ner"])
print(result.ner)
# [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]

# 最后的结果
# [[('Nh', '汤姆')]]
# 能看出来动作实体是汤姆？

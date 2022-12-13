from ltp import LTP
ltp = LTP("E:\python3.8.5\Lib\site-packages\ltp_data_base1") # 默认加载 LTP/Small 模型
# ltp = LTP(path = "LTP/base|LTP/small|LTP/tiny")

from ltp import StnSplit
sents1 = StnSplit().split("汤姆生病了。他去了医院。")
# [
#   "汤姆生病了。",
#   "他去了医院。"
# ]

sents2 = StnSplit().batch_split(["他叫汤姆去拿外衣。", "汤姆生病了。他去了医院。"])

# [
#   "他叫汤姆去拿外衣。",
#   "汤姆生病了。",
#   "他去了医院。"
# ]

print(sents1)
print(sents2)
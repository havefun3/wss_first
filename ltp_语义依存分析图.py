from ltp import LTP

ltp = LTP("E:\python3.8.5\Lib\site-packages\ltp_data_base1") # 默认加载 LTP/Small 模型

result = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks = ["cws","sdpg"])
print(result.sdpg)

#最终结果
#[[(1, 2, 'AGT'), (2, 0, 'Root'), (3, 2, 'DATV'), (3, 4, 'AGT'), (4, 2, 'eSUCC'), (5, 4, 'eSUCC'), (6, 5, 'PAT'), (7, 5, 'mPUNC')]]
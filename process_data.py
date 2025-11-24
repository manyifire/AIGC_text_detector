# from pathlib import Path
# import json
# import pandas as pd

# # src_path = Path("/data/wangmanyi/BoundaryDetection/Codes_and_DataForBoundaryDetectionProject/TriBERT-In_Domain_Evaluation/hybridCodeData_1boundary.jsonl")
# src_path=Path('/data/wangmanyi/MGT_Localization/hybridCodeData_mixed.jsonl')
# records = []
# with src_path.open("r", encoding="utf‑8") as fp:
#     for line in fp:              # 每行都是一个独立 JSON 对象
#         line = line.strip()
#         if not line:
#             continue             
#         records.append(json.loads(line))

# def transform1(rec: dict) -> dict:
#     human_code = '\n'.join(rec.get('human_part'))
#     machine_code = '\n'.join(rec.get('machine_part'))

#     new_rec1 = {
#         "id": rec.get("code_id"),                      
#         "question": rec.get('prompt_content'),  
#         "answer": human_code,
#         "label": 0,  # 0 for human
#         "source": rec.get('code_source')
#     }

#     return new_rec1

# def transform2(rec: dict) -> dict:
#     human_code = '\n'.join(rec.get('human_part'))
#     machine_code = '\n'.join(rec.get('machine_part'))

#     new_rec2 = {
#         "id": rec.get("code_id"),                      
#         "question": rec.get('prompt_content'),  
#         "answer": machine_code,
#         "label": 1,  # 0 for human
#         "source": rec.get('code_source')
#     }
    
#     return new_rec2

# dst_path = Path("hybridCode_full_mixed.csv")

# transformed1= (transform1(rec) for rec in records)  # 惰性生成器
# transformed2= (transform2(rec) for rec in records)  # 惰性生成器
# json_data = list(transformed1) + list(transformed2)  # 合并两个
# import random
# random.shuffle(json_data)
# # 将列表字典转换为DataFrame
# df_combined = pd.DataFrame(json_data)


# # 写入Excel文件
# df_combined.to_csv(dst_path, index=False, encoding='utf-8')
# print(f"🔄 完成！已写入 {dst_path.resolve()}")

# train = json_data[:int(0.8 * len(json_data))]  # 80% 训练集
# # val   = json_data[int(0.7 * len(json_data)):int(0.85 * len(json_data))]  
# test  = json_data[int(0.8 * len(json_data)):]

# train_path = Path("code_train_full_mixed.csv")
# val_path = Path("code_val_full_mixed.csv")
# test_path = Path("code_test_full_mixed.csv")

# df_train = pd.DataFrame(train)
# df_train.to_csv(train_path, index=False, encoding='utf-8')

# # # 验证集
# # df_val = pd.DataFrame(val)
# # df_val.to_csv(val_path_csv, index=False, encoding='utf-8')

# # 测试集
# df_test = pd.DataFrame(test)
# df_test.to_csv(test_path, index=False, encoding='utf-8')

# # ============================================================================
# # from pathlib import Path
# # import json
# # import pandas as pd

# # src_path = Path("/data/wangmanyi/BoundaryDetection/Codes_and_DataForBoundaryDetectionProject/TriBERT-In_Domain_Evaluation/hybridCodeData_cleaned.jsonl")

# # records = []
# # with src_path.open("r", encoding="utf‑8") as fp:
# #     for line in fp:              # 每行都是一个独立 JSON 对象
# #         line = line.strip()
# #         if not line:
# #             continue             
# #         records.append(json.loads(line))


# # def transform1(rec: dict) -> list:
# #     new_rec_list = []
# #     if not rec or not rec.get("human_part"):
# #         return []
# #     code_id = rec.get("code_id")
# #     prompt_content = rec.get("prompt_content")
# #     code_source = rec.get("code_source")
# #     for data in rec.get("human_part"):
# #         record_item = {
# #             "id": code_id,
# #             "question": prompt_content,
# #             "answer": data,
# #             "label": 0,
# #             "source": code_source
# #         }
# #         new_rec_list.append(record_item)
# #     return new_rec_list

# # def transform2(rec: dict) -> list:
# #     new_rec_list = []
# #     if not rec or not rec.get("machine_part"):
# #         return []
# #     code_id = rec.get("code_id")
# #     prompt_content = rec.get("prompt_content")
# #     code_source = rec.get("code_source")
# #     for data in rec.get("machine_part"):
# #         record_item = {
# #             "id": code_id,
# #             "question": prompt_content,
# #             "answer": data,
# #             "label": 1,
# #             "source": code_source
# #         }
# #         new_rec_list.append(record_item)
# #     return new_rec_list

# # dst_path = Path("hybridCode_sent.csv")

# # transformed1 = (transform1(rec) for rec in records)
# # transformed2 = (transform2(rec) for rec in records)

# # # --- 修正数据合并和压平的逻辑 ---
# # json_data_nested = list(transformed1) + list(transformed2)
# # json_data = [item for sublist in json_data_nested for item in sublist]

# # print(f"总共处理得到 {len(json_data)} 条记录。")
# # import random
# # # 后续代码保持不变...
# # random.shuffle(json_data)

# # df_combined = pd.DataFrame(json_data)
# # df_combined.to_csv(dst_path, index=False, encoding='utf-8')
# # print(f"🔄 完成！已写入 {dst_path.resolve()}")

# # train = json_data[:int(0.8 * len(json_data))]
# # test  = json_data[int(0.8 * len(json_data)):]

# # train_path = Path("code_train_sent.csv")
# # test_path = Path("code_test_sent.csv")

# # df_train = pd.DataFrame(train)
# # df_train.to_csv(train_path, index=False, encoding='utf-8')

# # df_test = pd.DataFrame(test)
# # df_test.to_csv(test_path, index=False, encoding='utf-8')


# -------- 将代码分为block level --------
import json
import csv

# 读取JSON文件
with open('/data/wangmanyi/MGT_Localization/code_test_block.json', 'r') as f:
    data = json.load(f)  # 加载JSON数据，应该是一个列表的字典

# 打开CSV文件用于写入
with open('/data/wangmanyi/AIGC_text_detector/code_data/unfilter_block/code_test_block.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'question', 'answer', 'label', 'source']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()  # 写入列头
    
    # 遍历每个字典项
    for item in data:
        article_id = item['article_id']
        merge_sentences = item['merge_sentences']
        mixed_labels = item['config_dict']['mixed_labels']
        
        # 检查merge_sentences和mixed_labels长度是否一致
        if len(merge_sentences) != len(mixed_labels):
            print(f"警告: article_id {article_id} 的 merge_sentences 和 mixed_labels 长度不匹配，跳过此条目")
            continue  # 跳过当前条目
        
        # 遍历每个merge_sentences中的句子
        for idx, sentence in enumerate(merge_sentences):
            writer.writerow({
                'id': article_id,
                'question': '',
                'answer': sentence,
                'label': mixed_labels[idx],
                'source': 'CodeSearchNet'
            })

# from pymilvus import connections


# def connect_to_milvus():
#     try:
#         # 连接到 Milvus 服务（确保 IP 和端口正确）
#         connections.connect("default", host="121.4.77.31", port="19530")
#         print("Successfully connected to Milvus!")
#     except Exception as e:
#         print(f"Failed to connect to Milvus: {e}")


# # 测试连接
# connect_to_milvus()
from pymilvus import MilvusClient, FieldSchema, CollectionSchema, DataType


# 1. 初始化设置
MILVUS_URI = "http://121.4.77.31:19530"

try:
    milvus_client = MilvusClient(uri=MILVUS_URI)
except Exception as e:
    print(f"Failed to connect to Milvus: {e}")

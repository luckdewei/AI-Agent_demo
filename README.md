# AI Agent 学习

## 本项目依赖工具使用的是 uv

### 安装 uv

```shell
pip install uv
```

### 下载依赖

```shell
uv sync
```

## 配置 .env 文件

在根目录下新建.env文件，内容如下：

``` shell
LLM_API_KEY="<KEY>"
LLM_MODEL_ID="Qwen/Qwen2.5-72B-Instruct"
LLM_BASE_URL="https://api-inference.modelscope.cn/v1/"
SERPAPI_API_KEY="<KEY>"
```

目前使用的是Qwen2.5-72B-Instruct模型，如果需要使用其他模型，可以参考[ModelScope](https://www.modelscope.cn/home)官网，获取模型ID和API Key。

SERPAPI_API_KEY 是谷歌搜索API的key，可以通过[谷歌搜索API](https://serpapi.com/google-search-api)申请。

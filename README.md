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

### 运行基础的ReAct Agent

进入basic_agent目录

在ReAct.py里修改 question 的值，然后运行
```python
...
if __name__ == "__main__":
    llm = HelloAgentsLLM()  # 初始化LLM客户端
    tool_executor = ToolExecutor()  # 初始化工具执行器
    search_desc = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"  # 工具描述
    tool_executor.registerTool("Search", search_desc, search)  # 注册工具
    agent = ReActAgent(llm_client=llm, tool_executor=tool_executor)  # 初始化ReAct智能体
    question = "你的问题"
    agent.run(question)
```

```shell
cd basic_agent

```
```shell
uv run ReAct.py
```

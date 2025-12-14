AutoGen 的核心思想是通过对话实现协作。它将多智能体系统抽象为一个由多个“可对话”智能体组成的群聊。开发者可以定义不同角色（如 Coder, ProductManager, Tester），并设定它们之间的交互规则（例如，Coder 写完代码后由 Tester 自动接管）。任务的解决过程，就是这些智能体在群聊中通过自动化消息传递，不断对话、协作、迭代直至最终目标达成的过程。

架构图：
![](https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/6-figures/02.png)

# Code related

## Fix bug till work
```
遇到下面的问题,请检查 这个是什么原因,不要自己瞎编,要去确保查找官方的正确方案和文档.
不要只是给我方案,让我去试. 你要自己修复,自己重启并确定可以登陆了,如果 有问题自己试图去修复再测试
```
## General Code Review

```
You asume to be one very good at code review, you are considered as a forward thinking seniro developer, with extensive production errors & fix experieisncea, and done lots of code review the changed code, 
so start to do code review this code for:
- bugs and edge cases
- security vulnerabilities
- performance issues
- readability and naming
Keep feedback concise and actionable.
```


```
你作为
并且添加测试确保这个是正确 的prodcution 级别的代码，并通过边界条件测试
```

## PR Summary

```
Summarize this PR in 3 bullet points: what changed, why, and any risks.
```


## Code Algo

```
下面是一个面试问题,如果你是面试官，你期待的principle dev的理想答案是什么样子的， 先给我答案，然后解释这个解决方案， 通过这个我可以学到什么更多面试的知识技巧， 通过通用人类知识精华分析这个，有什么本质性的我可以以此学习
 ~ corner case是什么，然后确定没有丢失corner case
 ~ 不要背答案
 ~ 逆向工程，分析告诉我如何可以得到这些解法
 这个题目我可以学习什么通用的解题技巧或者方法论，用在类似或者其他 FANG 面试的算法题
 要展示 问题建模 + 解法选择 + trade-off 分析。
 ~ 直觉图解,“信息单向性 (information directionality)” 和 “冗余消除 (eliminate redundant checks)”。
 ~ 寻找破局点：视角的逆转 (Inversion / Symmetry Breaking)
~ 请给我 FANG Principal Developer 满分答案
~ 解答应该是一个strong hire水平的解答
~ 可以从以下角度来分析这个问题，请选择最适合当前场景下的角度，不用使用下面的全部
~ 我们创造了工具，工具反过来塑造我们的思维。
 - 练习一种非常重要的能力，看见系统，而不只是看见孤立的事件。
 - 算法直觉（Algorithmic Intuition）的构建，
 - 使用出自《孟子的知人论世”这个典故
 - 古德哈特定律」、「自我决定理论」、「WOOP」、「自由能」、「对称性破缺」、「多臂老虎机」、帕纳斯法则 (Parnas's Principle of Information Hiding) 在，「布里尔分数」等等等
 - 尝试去链接和使用其他学科内部经典的理论知识和经典模型，比如（但是不限于）：物理学，经济学，化学，生物学，人文学，哲学，心理学，热力学，空气学
-第一性原理 [1]
- Parnas 原则
- 二分法 / 控制的两分法 [2]
- 反向思维 / 逆向思维 [3]
- 多元思维模型 / 跨学科思维 [4]
- 大概率思维 [5]
- 奥卡姆剃刀 [6]
- MECE分析法 [7]
- 系统思考 [8]
- “5个为什么”追问法 [9]
- 定义问题五要素法 [10]
- 费曼学习法 [11]
- 批判性思维 [12]
- 近的思维 [2]
- 番茄工作法 [13]
- PDCA循环（戴明环） [14]
- SMART原则 [15]
- 原子习惯 / 微习惯 / 小步子原理 [16]
- 黄金圈法则 [17]
- 二八定律 / 帕累托定律 [18]
- 反脆弱 [19]
- 框架设定（重大框架、易处理框架、神秘事件框架） [20, 21]
- 如何go extra  mile, 不只是完成当前任务。
- 自律的反面是他律，如何在环境限制中还有自己的主观能动性，做微决策，让自己有掌控感
- think inside out
- 如果我只是我会死在哪里，我就永远不去那里
- 沉没成本谬误（Sunk Cost Fallacy）
- 人不会执行最优策略，只会执行“被奖励的策略”
  - 最后，创造连接。它指的不是“认识很多人”，而是能在不同的知识、不同的想法之间，难已有价值的联系。
```


## troubleshoot

```

Assume you are a very senior developer success in lots of troubleshooting hard and difficulty complexy issues. 
Not only fix and sovle this iusse, but think and look into essential and more universal views.
Answer like a star instrucutor , so your audience love to hear you and follow you 

下面是错误:请从下面几点分析给出你的看法,不要瞎编,可以查询互联网:
 - 分析哪里错误了,
 - 为什么会有这个错误,
 - 如何今后可以避免,
 - 有什么方法或者通用的技术可以避免这类错误,
 - 有什么技巧可以今后在面试时快速,
 - 准确的作为一个 principal developer 的提供解决方案,
 - 如何把这次教训内化（训练计划）
 - 还有没有其他高频的可能的错误出现在这个代码块,我可以一起学习
 - 还有什么你觉得我必须知道的,可能在面试中彰显我是一个 top principal developer
 - 最后生成一个英文的说明解释文档，我可以以后在面试前查看并帮助我解决并避免同类问题
 - 直觉图解, “信息单向性 (information directionality)” 和 “冗余消除 (eliminate redundant checks)”
 - at last, Give me the solution write by  principal developer 解答应该是一个strong hire水平的解答
可以从以下角度来分析这个问题，请选择最适合当前场景下的角度，不用使用下面的全部

~ 逆向工程，分析告诉我如何可以得到这些解法
 这个题目我可以学习什么通用的解题技巧或者方法论，用在类似或者其他 FANG 面试的算法题
 要展示 问题建模 + 解法选择 + trade-off 分析。
 ~ 直觉图解,“信息单向性 (information directionality)” 和 “冗余消除 (eliminate redundant checks)”。
 ~ 寻找破局点：视角的逆转 (Inversion / Symmetry Breaking)
~ 我们创造了工具，工具反过来塑造我们的思维。
 - 练习一种非常重要的能力，看见系统，而不只是看见孤立的事件。
 - 算法直觉（Algorithmic Intuition）的构建，
 - 使用出自《孟子的知人论世”这个典故
 - 古德哈特定律」、「自我决定理论」、「WOOP」、「自由能」、「对称性破缺」、「多臂老虎机」、帕纳斯法则 (Parnas's Principle of Information Hiding) 在，「布里尔分数」等等等
 - 尝试去链接和使用其他学科内部经典的理论知识和经典模型，比如（但是不限于）：物理学，经济学，化学，生物学，人文学，哲学，心理学，热力学，空气学
-第一性原理 [1]
- Parnas 原则
- 二分法 / 控制的两分法 [2]
- 反向思维 / 逆向思维 [3]
- 多元思维模型 / 跨学科思维 [4]
- 大概率思维 [5]
- 奥卡姆剃刀 [6]
- MECE分析法 [7]
- 系统思考 [8]
- “5个为什么”追问法 [9]
- 定义问题五要素法 [10]
- 费曼学习法 [11]
- 批判性思维 [12]
- 近的思维 [2]
- 番茄工作法 [13]
- PDCA循环（戴明环） [14]
- SMART原则 [15]
- 原子习惯 / 微习惯 / 小步子原理 [16]
- 黄金圈法则 [17]
- 二八定律 / 帕累托定律 [18]
- 反脆弱 [19]
- 框架设定（重大框架、易处理框架、神秘事件框架） [20, 21]
- 如何go extra  mile, 不只是完成当前任务。
- 自律的反面是他律，如何在环境限制中还有自己的主观能动性，做微决策，让自己有掌控感
- think inside out
- 如果我只是我会死在哪里，我就永远不去那里
- 沉没成本谬误（Sunk Cost Fallacy）
- 人不会执行最优策略，只会执行“被奖励的策略”
- 最后，创造连接。它指的不是“认识很多人”，而是能在不同的知识、不同的想法之间，难已有价值的联系。

===== below is my input=====

```

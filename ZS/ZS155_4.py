# 5200. 项目管理  显示英文描述  我的提交返回竞赛
#
# 公司共有 n 个项目和  m 个小组，每个项目要不没有归属，要不就由其中的一个小组负责。
#
# 我们用 group[i] 代表第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。（项目和小组都是从零开始编号的）
#
# 请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：
#
# 同一小组的项目，排序后在列表中彼此相邻。
# 项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。
# 结果要求：
#
# 如果存在多个解决方案，只需要返回其中任意一个即可。
#
# 如果没有合适的解决方案，就请返回一个 空列表。

##------ 拓扑排序 -------##
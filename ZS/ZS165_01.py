# A 和 B 在一个 3 x 3 的网格上玩井字棋。
#
# 井字棋游戏的规则如下：
#
# 玩家轮流将棋子放在空方格 (" ") 上。
# 第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
# "X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
# 只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
# 如果所有方块都放满棋子（不为空），游戏也会结束。
# 游戏结束后，棋子无法再进行任何移动。
# 给你一个数组 moves，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列），它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各自的棋子位置。
#
# 如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。
#
# 你可以假设 moves 都 有效（遵循井字棋规则），网格最初是空的，A 将先行动。
#
from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        wins = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        def checkwin(S):
            for win in wins:
                flag = True
                for pos in win:
                    if pos not in S:
                        flag = False
                        break
                if flag:
                    return True
            return False

        A, B = set(), set()
        for i, (x, y) in enumerate(moves):
            if i % 2 == 0:
                A.add((x, y))
                if checkwin(A):
                    return "A"
            else:
                B.add((x, y))
                if checkwin(B):
                    return "B"

        return "Draw" if len(moves) == 9 else "Pending"


# 1. 题目分析
# 井字棋总共只有99个格子，且赢面是固定的
# 可以使用一个99位二进制数代表行走的结果，规定：
# 井字棋坐标[i,j][i,j]对应于数字的第3i+j3i+j位
# 每走一步棋等价于与对应的位进行(异)或运算
# 判断游戏结果的方法：
# 将一方的数字numnum与赢面对应的数字kk进行与运算，若结果为kk，此方获胜
# 若双方都未获胜：
# 若总步数为99步，则平局(DrawDraw)
# 否则，未完成(PendingPending)
# (附1)赢面数字：
# 井字棋的赢面只有88种(33种横+33种竖+22种对角)
# 计算举例：\{[0,0],[0,1],[0,2]\}{[0,0],[0,1],[0,2]}为横的一种赢面，对应的99位二进制数为000000111000000111，即十进制下的77
# 事实上，由对应规则可以得知：
# 33种横的赢面数字是公比为88的等比数列
# 33种竖的赢面数字是公比为22的等比数列
# 总共只需要计算出44个数字(11种横+11种竖+22种对角)，其余按倍数推导即可
# 所有赢面数字分别为7, 56(即7\times 8), 448(即7\times 8^2), 73, 146(即73\times 2), 292(即73\times 2^2), 273, 847,56(即7×8),448(即7×8
# 2
#  ),73,146(即73×2),292(即73×2
# 2
#  ),273,84
# (附2)我在评论区对使用位运算的思路进行了更细致的阐述，如果有不清楚的地方欢迎移步评论区~


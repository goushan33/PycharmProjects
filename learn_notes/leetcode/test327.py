'''
首先考虑一些奇怪的临界值
n=1：有m种可能。
n=2：有m（m-1）种可能。
m<2:并且n>2:毫无可能。
然后考虑正常情况
第一个扇面有m种可能，在不考虑最后一个和第一个扇面的颜色关系情况下，后面的n-1块都是有m-1种可能性。但这样得到的可能性是多的，接下来就是要考虑减去第一块和最后一块同色的情况。
当同色时候，其实可以把两个扇面融合，看成一个扇面，这是本题求解的关键。这样减去的部分就可以变成问题参数是（n-1，m）时得到的可能性。
递归表达式出来了：

S(n,m) = m*(m-1)^(n-1) - S(n-1,m)
其实可以进一步运用高中数学中数列知识，把m看成常数，配一下项，变成等比数列，直接得到最后通式：

Sn = (-1)^n * (m-1) + (m-1)^n
具体操作不展开了…因为我懒，并且打公式好烦。
---------------------
'''


'''
DP problem:
weight: 物品重量，n: 物品个数，w: 背包可承载重量
public int knapsack(int[] weight, int n, int w) {
  boolean[][] states = new boolean[n][w+1]; // 默认值 false
  states[0][0] = true;  // 第一行的数据要特殊处理，可以利用哨兵优化
  states[0][weight[0]] = true;
  for (int i = 1; i < n; ++i) { // 动态规划状态转移
    for (int j = 0; j <= w; ++j) {// 不把第 i 个物品放入背包
      if (states[i-1][j] == true) states[i][j] = states[i-1][j];
    }
    for (int j = 0; j <= w-weight[i]; ++j) {// 把第 i 个物品放入背包
      if (states[i-1][j]==true) states[i][j+weight[i]] = true;
    }
  }
  for (int i = w; i >= 0; --i) { // 输出结果
    if (states[n-1][i] == true) return i;
  }
  return 0;
}


定义一个3*3的二维数组：
matrix = [[0 for i in range(3)] for i in range(3)]
'''


def dp_problem(n,w,item):
    state= [[0 for i in range(3)] for i in range(3)]
    #特殊处理第一层数据
    state[0][0]=1#第一个物品不放进去
    state[0][item[0]]=1#第1个物品放进去
    for i in range(1,n):
        for  j in range(w):#不把第i个物品放入背包
            if (state[i - 1][j] == 1):
                state[i][j] = state[i-1][j]
                pass

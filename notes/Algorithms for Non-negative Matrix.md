# 摘要
非负性矩阵分解已经被证明对于多元数据的分解是非常有效的方法。本文介绍了两种不同的非负矩阵分解算法。他们的区别仅在于使用的乘积因子有轻微的区别。其中一种算法最小化方程的最小二乘误差，另一种最小化了表达式的KL距离。而且这两种算法的收敛性都可以通过一种类似证明期望最大化算法的方法使用辅助函数得到证明。这个算法同样可以解释为是一个对对角因子进行了优化选择以确保能够收敛的对角化梯度下降。

# 1 介绍

Unsupervised learning algorithms such as principal components analysis and vector quantization  can be understood as factorizing a data matrix subject to different constraints. Depending  upon the constraints utilized, the resulting factors can be shown to have very different  representational properties. Principal components analysis enforces only a weak orthogonality  constraint, resulting in a very distributed representation that uses cancellations  to generate variability [1, 2]. On the other hand, vector quantization uses a hard winnertake-  all constraint that results in clustering the data into mutually exclusive prototypes [3].

类似主成分分析或矢量量化等无监督学习算法可以被理解为在不同约束条件下的矩阵分解。根据不同的约束条件，矩阵分解可以表现出不同的属性特点。主成分分析只有一个弱的正交约束，这导致了一个非常稀疏的表达并通过取消来生成可变性。矢量量化定义了严格的“赢家获取所有”的约束，这导致数据聚集到互斥的原型中。（其实就是一元约束）

We have previously shown that nonnegativity is a useful constraint for matrix factorization
that can learn a parts representation of the data [4, 5]. The nonnegative basis vectors that are
learned are used in distributed, yet still sparse combinations to generate expressiveness in
the reconstructions [6, 7]. In this submission, we analyze in detail two numerical algorithms
for learning the optimal nonnegative factors from data.

我们在之前已经展示了非负性约束是一个能够使矩阵分解学习到数据的某一部分表达的一种非常有效的约束。学习到的非负的基向量是在分布中使用的，但仍然是稀疏的组合用来在重建中产生表达性。本文中我们将套路两种求最优的分解因子的数值优化算法。

# 非负矩阵分解

We formally consider algorithms for solving the following problem:

我们将司考一个用来解决以下问题的方法：

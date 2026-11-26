# A270363：一个二项式和的四阶递推

Chain.Ren · 独立研究 · 2026-11-27

从 [A270363](https://oeis.org/A270363) 的二项式和定义出发，以 Catalan 幂提取系数，再换一个形式变量，把四步递推化为可逐项复算的有理函数恒等式。

[完整证明](PROOF.md) · [查新](PRIOR.md) · [公开版本](https://github.com/Asakitan/oeis-a270363/releases/tag/proof-v1.0.0) · [引用](CITATION.cff)

运行 `python -B verify.py`（需 Python 3 和 SymPy）。脚本执行精确符号恒等检验，并从原二项式和独立计算前 24 项。

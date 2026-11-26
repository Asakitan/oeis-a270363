# 从 Catalan 幂和验证 A270363 的四阶递推

**署名：** Chain.Ren · 独立研究

**版本：** [proof-v1.0.1](https://github.com/Asakitan/oeis-a270363/releases/tag/proof-v1.0.1) · 2026-11-27（Australia/Sydney）

OpenAI Codex 实质参与推导、文稿和符号复核。

[Vladimir Kruchinin 的 A270363](https://oeis.org/A270363) 定义 $a_0=0$，对 $n\ge1$ 取
$$ a_n=(n+1)\sum_{k=0}^{\lfloor(n-1)/2\rfloor}
\frac1{n-k}\binom{2n-3k-2}{n-k-1}. $$
令
$$p(n)=n(7n^2-17n-2),\quad q(n)=-35n^3+99n^2+20n-120,\quad r(n)=2(2n-5)(7n^2-3n-12).$$
**定理。** 对 $n\ge4$，R. J. Mathar 于 2016 年提出的关系成立：
$$p(n)a_n+q(n)a_{n-1}+r(n)a_{n-2}+p(n)a_{n-3}-r(n)a_{n-4}=0.$$

## 把定义化为一个对数的导数

设 $C=1+xC^2$ 是常数项为一的 Catalan 级数。拉格朗日反演作用于 $t=C-1=x(1+t)^2$ 给出
$$ [x^\ell] C(x)^m=\frac{m}{\ell+m}\binom{2\ell+m-1}{\ell}\quad (m\ge1,\ \ell\ge0).$$
具体地，对 $\ell\ge1$，系数等于 $\frac{m}{\ell}[z^{\ell-1}](1+z)^{m-1+2\ell}$；$\ell=0$ 时直接核实。取 $m=k+1,\ \ell=n-1-2k$，用二项式对称性，即得定义中的每个被加数是 $[x^{n-1-2k}]C^{k+1}/(k+1)$。所以
$$\sum_{n\ge1}\frac{a_n}{n+1}x^{n+1}=\sum_{k\ge0}\frac{(x^2 C(x))^{k+1}}{k+1}=-\log(1-x^2 C(x)).$$
形式求导，得到 $A(x)=\sum_{n\ge0}a_nx^n=(x^2C(x))'/(1-x^2C(x))$。

## 把递推验证化为有理恒等式

令 $x(t)=t/(1+t)^2$，于是 $C(x(t))=1+t$，$x'(0)=1$。代入前式并用链式法则可得
$$ A(x(t))=F(t)=\frac{t(t-2)(1+t)^2}{(t-1)(t^3+2t^2+3t+1)} .$$
Euler 算子 $x\frac{d}{dx}$ 在此变换下成为 $E=\frac{t(1+t)}{1-t}\frac{d}{dt}$，并在 $x^n$ 上乘以 $n$。定义 $c_0=p,\ c_1=q,\ c_2=r,\ c_3=p,\ c_4=-r$。因此，在 $x$ 中展开 $\sum_{j=0}^4 c_j(E)(x^j F)$，其第 $n$ 项系数就是上述递推的左端（负指标项取零）。

剩下只要进行有限的有理运算；将上述 $x(t),F,E$ 代入得到
$$
\sum_{j=0}^4 c_j(E)\bigl(x(t)^j F(t)\bigr)
=-\frac{6t(4t^4+12t^3-5t^2+12t+4)}{(1+t)^6}
=-24x(t)+24x(t)^2+126x(t)^3.
$$
[符号证书](verify.py)对每个 $j$ 从 $x^j F$ 起连用三次 $E$，以 $c_j$ 的各次系数组合结果，通分检查上式分子之差为零。因为 $x(t)$ 有可逆的线性项，该恒等式也是原变量 $x$ 的形式恒等式。右边四次及以后没有系数；取系数即证明全部 $n\ge4$，而非只核对已列出的数项。∎

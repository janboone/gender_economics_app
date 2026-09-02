# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib==3.11.1",
#     "numpy==2.5.2",
#     "pandas==3.0.5",
#     "scipy==1.18.1",
# ]
# ///
import marimo

__generated_with = "0.23.8"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is a markdown cell where you can add your own name and (optional) your teammate in the following table:

    |Name|SNR|ANR|
    |----|---|----|
    |mery ferrando|12345|u1234|
    |jan boone|67890|u6786|
    """)
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import scipy as sp

    return mo, np, pd, plt, sp


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python assignment

    The python assignment you can do either on your own or with one other student (i.e. max group size is 2 students).

    The first cell of your notebook, should contain a table with the names and SNRs and ANRs of the group members, like so

    |Name|SNR|ANR|
    |----|---|----|
    |jan boone|12345|u6786|
    |adam smith|56789|u1234|

    See [the webpage](https://janboone.github.io/Python-programming-for-economists/#final_assignment) for details of what we expect to see in this assignment.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Topic and research question

    This app is based on Mery's gender economics lecture.

    Economists have proposed several theories to explain why workers of certain groups (e.g., minorities, women) might have lower wages than workers of the majority group. One of these theories suggests that discrimination might arise if employers dislike hiring workers of certain groups. This type of discrimination is called taste discrimination.

    We will see how taste discrimination works with a simple model. We assume that the gains that employers derive from the workers include the profits of the firm and some taste parameters. Let's further assume that some employers dislike hiring workers of a certain group.

    We will show that taste discrimination leads to lower wages for the employees that the employer dislikes but actually benefits the majority group who are not disliked by employers.

    Our research question is: how does market power affect the impact of taste discrimination on wages and employment outcomes across different groups?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Motivation

    Given the persistent lower wages for women in almost all countries, understanding the determinants of the gender wage gap remains a central issue in economics.

    This app aims to contribute to this understanding by analyzing how competition in product and labor markets affects wages and employment for the group that is disadvantaged by taste discrimination. An intuition we want to analyze is that a firm with taste discrimination can be disciplined by a competing firm without any bias in a way that a monopolist cannot be restrained.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Model

    Consider a market where female and male workers are symmetric in terms of productivity and labor supply. In particular, in this market a firm's production function is given by
    $$
    y = (l_f^{\rho} + l_m^{\rho})^{\alpha/\rho}
    $$
    where $y$ denotes the firm's output and $l_f, l_m$ the number of female, male employees. With $\rho = 1$ male and female employees are perfect substitutes. Although $\rho = 1$ may be an intuitive choice, it may cause problems for the numerical solvers that we use below. To avoid these numerical problems we create a slider for $\rho$ between 0 and 1.

    For $\alpha$ we also set a slider between 0 and 1. Indeed, negative $\alpha$ does not make sense (more employees lead to lower output) and $\alpha > 1$ may cause problems with the second order conditions for profit maximization.

    For both men and women we have a labor supply curve given by $L^s(w) = a w$ where we set $a = 5$: labor supply increases with the wage $w$.

    Demand for this homogenous product is given by $p(y) = 120 e^{-0.01 * y}$. Although linear demand like $p = 120 - y$ is simpler, this function is not differentiable at $y=120$ which may cause problems for the numerical solvers that we use below.

    Finally, the profit function for a firm in the market is given by
    $$
    \pi = p y - (w_f+u) l_f - w_m l_m
    $$
    where $w_f, w_m > 0$ denote female and male wages respectively and $u \geq 0$ represents the aversion the employer feels towards workers of group $F$.

    In order to analyze how competition affects the outcomes of $u>0$ on $l_f, w_f$ compared to $l_m, w_m$ we compare two market structures. First, two firms that take prices as given and one firm has $u > 0$ while the other has $u=0$. Second, a monopoly where the firm understands both the labor market and product market effects of changing its demand for labor.

    ## Perfect competition

    The two firms maximize profits taking wages and prices as given.

    Firm $1$ is assumed to have discriminatory preferences $u>0$, while firm $2$ has $u=0$. They choose employment $l_f,l_m$ to maximize profits:
    $$
    \pi_1 = p y_1 - (w_f+u)l_{f,1} - w_m l_{m,1}
    $$
    and
    $$
    \pi_2 = p y_2 - w_f l_{f,2} - w_m l_{m,2},
    $$
    where
    $$
    y_i = (l_{f,i}^{\rho}+l_{m,i}^{\rho})^{\alpha/\rho}.
    $$

    From this maximization it follows that total output equals
    $$
    Y = y_1+y_2
    $$
    and thus the market price is
    $$
    p(Y)=120e^{-0.01Y}.
    $$

    Let firm $i \in \{1,2\}$ choose labor demand $(l_{f,i},l_{m,i})$. Aggregate labor demand determines equilibrium wages through labor supply:
    $$
    L_f^s = a w_f = l_{f,1}+l_{f,2}
    $$
    and
    $$
    L_m^s = a w_m = l_{m,1}+l_{m,2}.
    $$

    We need to find equilibrium prices $p,w_f,w_m$ such that $p=p(Y)$ with $Y=y_1 + y_2$ and labour supply equals demand on both the $F$ and $M$ markets: $L(w_f) = l_{f,1}+l_{f,2}$ and $L(w_m) = l_{m,1}+l_{m,2}$. We will create a fixed point function below to derive this equilibrium numerically.

    ## Monopoly

    Under monopoly a single firm chooses $(l_f,l_m)$ while recognizing that its hiring decisions affect both wages and product prices. A simple way to formulate this is that the monopolist chooses $w_f,w_m$ and from this follows labor supply $l_f,l_m$, total output $y$ and thus the price $p(y)$. This monopolist has taste parameter $u > 0$.

    Hence, the monopolist chooses wages to maximize
    $$
    \Pi = p(y)y - (w_f+u)L(w_f)-w_m L(w_m)
    $$
    with $y = (L(w_f)^{\rho}+L(w_m)^{\rho})^{\alpha/\rho}$.

    The comparison between these two market structures allows us to study how market power interacts with employer discrimination.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python code and explanation

    First, we create sliders for the parameters $\alpha, \rho$
    """)
    return


@app.cell
def _(mo):
    rho = mo.ui.slider(0.05,1.0,0.05, value=0.2, label="$\\rho$")
    alpha = mo.ui.slider(0.05,1.0,0.05, value=0.5, label="$\\alpha$")
    return alpha, rho


@app.cell(hide_code=True)
def _(mo):
    mo.md(f"""
    We define the production function, `output`, inverse demand function `price` and labor supply curve `labor_supply` which are relevant for both the perfect competition and monopoly models.
    """)
    return


@app.cell
def _(alpha, np, rho):
    def output(l_f,l_m):
        return (l_f**rho.value + l_m**rho.value)**(alpha.value/rho.value)

    def price(y):
        return 120 * np.exp(-0.01 * y)

    def labor_supply(w,a=5):
        return a*w

    return labor_supply, output, price


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Perfect competition

    To solve the perfect competition case we define the profit function `profit` which depends on $l_f,l_m$, the prices $p,w_f,w_m$ and the parameter $u$.

    The function `firm_choices` derives $l_f,l_m$ to maximize profits for given prices and parameter $u$. The firm returns the optimal output level, employment choices and financial profits (excluding $u$).

    It is for this optimization problem that we allow $\rho < 1$. To understand this, consider what happens with $\rho = 1$ and $u > 0$. The first order conditions for $l_f,l_m$ can be written as

    $$
    \frac{\partial y_1}{\partial l_f} = w_f + u
    $$

    and

    $$
    \frac{\partial y_1}{\partial l_m} = w_m
    $$

    When $l_f$ and $l_m$ are perfect substitutes ($\rho = 1$), the left hand side of these equations are the same, while the right hand side can differ. This leads to corner solutions where the firm employs only one type of labor unless $w_f + u = w_m$. By setting $\rho < 1$, female and male labor become imperfect substitutes, ensuring an interior solution for labor demand. The latter makes the optimization numerically more stable.

    In general, the numerical solution for the perfect competition case tends to be less stable than the monopoly outcome. The reason is that the perfect competition equilibrium involves a combination of optimization (profit maximizing firms) and solving a fixed point equation (to derive the equilibrium). Hence some parameter combinations can lead to $w_f > w_m$ which is not possible in equilibrium with the parameter values that we analyze. Also, the figures below can sometimes look a bit "wonky". In this case, this is a numerical issue that we do not worry about.

    Finally, to avoid the instability (for $\rho$ close to 1) to cause the optimizer to choose negative labor inputs during intermediate iterations, we impose non-negativity bounds on both $l_f$ and $l_m$ in the numerical optimization routine.
    """)
    return


@app.cell
def _(output, sp):
    def profit(l_f,l_m,p,w_f,w_m,u):
        return p*output(l_f,l_m) - l_f * (w_f+u) - l_m * w_m

    def firm_choices(p,w_f,w_m,u):
        sol = sp.optimize.minimize(lambda l: -profit(l[0],l[1],p,w_f,w_m,u),\
                                   [40,40],bounds = ((0, None), (0, None)))
        lf = sol.x[0]
        lm = sol.x[1]
        y = output(lf,lm)
        financial_profit = p*y - lf * w_f - lm * w_m
        return [y,lf,lm,financial_profit]

    return (firm_choices,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To derive the equilibrium, we solve a fixed point equation. In particular, we try to find the prices $p,w_f,w_m$ such that the following three equations hold:
    - the price $p$ that firms take as given (perfect competition) should equal the price that follows from the demand function $p(Y)$ where $Y$ equals total production by the two payoff maximizing firms;
    - firms total demand for female labor should equal supply at the price $w_f$: $L_f^s(w_f) = l_{f,1} + l_{f,2}$;
    - firms total demand for male labor should equal supply at the price $w_m$: $L_m^s(w_m) = l_{m,1} + l_{m,2}$.

    In the function `fixed_point` the vector `x` consists of price $p$, female wage $w_f$ and male wage $w_m$. Then `competitive_outcome` tries to find `x` such that the three equations above are satisfied.

    Below in the parameter sweep we will allow female labor supply $a_f$ to differ from male labor supply $L_m^s = a w_m$.
    """)
    return


@app.cell
def _(firm_choices, labor_supply, np, price):
    def fixed_point(x,u,af):
        p = x[0]
        wf = x[1]
        wm = x[2]
        choices1 = firm_choices(p,wf,wm,u)
        choices2 = firm_choices(p,wf,wm,0)
        Y = choices1[0]+choices2[0]
        Lf = choices1[1]+choices2[1]
        Lm = choices1[2]+choices2[2]
        return np.array([
            p - price(Y),
            labor_supply(wf,a=af) - Lf,
            labor_supply(wm) - Lm        
        ])



    return (fixed_point,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To find the competitive equilibrium, we solve the `fixed_point` equations.
    """)
    return


@app.cell
def _(fixed_point, sp):
    def competitive_outcome(u,af=5):
        sol_eq = sp.optimize.fsolve(lambda x: fixed_point(x,u,af),[90,10,10])
        return sol_eq



    return (competitive_outcome,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Monopoly

    In the monopoly/monopsony situation, the firm chooses the wages $w_f,w_m$ to maximize profits taking into account the relationships of demand $p(Y)$ on the final good market (monopoly) and supply $L^s(w)$ on the $F$ and $M$ labor markets (monopsony).

    In a sense this problem is simpler than the perfect competition problem. Here we only need to solve a maximization problem and not a fixed point problem to derive the equilibrium outcome.
    """)
    return


@app.cell
def _(labor_supply, output, price, sp):
    def profit_monop(wf,wm,u,af):
        lf = labor_supply(wf,af)
        lm = labor_supply(wm)
        y = output(lf,lm)
        return price(y) * y - lf * (wf+u) - lm * wm

    def monopoly_outcome(u,af=5):
        sol_monop = sp.optimize.minimize(lambda w:\
                    -profit_monop(w[0],w[1],u,af),\
                    [10,10],bounds = ((0, None), (0, None)))
        return sol_monop



    return (monopoly_outcome,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # App

    The following sliders allow you to set $\alpha$ and $\rho$ as the parameters of the production function.
    """)
    return


@app.cell
def _(alpha, mo, rho):
    mo.vstack([alpha,rho])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We solve the perfectly competitive outcome for `u = u_value` and the monopoly outcome for both `u = u_value` and `u = 0`. Note the use of the Python syntax `*sol_eq` to unpack the array `sol_eq` into the arguments of the function `firm_choices`.
    """)
    return


@app.cell
def _(competitive_outcome, firm_choices, monopoly_outcome):
    u_value = 2.0
    sol_eq = competitive_outcome(u_value)
    sol_monop = monopoly_outcome(u_value)
    sol_monop_no_discr = monopoly_outcome(0)

    relative_w_competition = sol_eq[1]/sol_eq[2]
    relative_w_monopoly = sol_monop.x[0]/sol_monop.x[1]
    profit_1 = firm_choices(*sol_eq,u_value)[3]
    profit_2 = firm_choices(*sol_eq,0)[3]
    return (
        profit_1,
        profit_2,
        relative_w_competition,
        relative_w_monopoly,
        sol_eq,
        sol_monop,
        sol_monop_no_discr,
        u_value,
    )


@app.cell(hide_code=True)
def _(
    alpha,
    mo,
    profit_1,
    profit_2,
    relative_w_competition,
    relative_w_monopoly,
    rho,
    sol_eq,
    sol_monop,
    sol_monop_no_discr,
):
    mo.md(f"""
    For $\\alpha$ equal to {alpha.value} and $\\rho$ equal to {rho.value} we find that in the competitive outcome women earn a wage equal to {sol_eq[1]:.2f} and men earn {sol_eq[2]:.2f}. Hence there is wage discrimination in the labor market.

    Although market competition does not eliminate discrimination, it does reduce it compared to the monopoly situation as we will see below. Another effect that can mitigate discrimination is the capital market. The discriminating firm ($u > 0$) earns profits equal to {profit_1:.2f} while the other firm (with $u = 0$) earns {profit_2:.2f}. Hence, if these firms would compete on the capital market to attract equity, the second firm is more likely to be successful.

    In the monopoly situation women earn a wage of {sol_monop.x[0]:.2f} and men earn {sol_monop.x[1]:.2f}. In the monopoly situation we can also illustrate that while women would like to abolish discrimination, men actually benefit from it: without discrimination (monopolist with $u=0$), both women and men would earn {sol_monop_no_discr.x[0]:.2f}. Hence there is no direct financial incentive for men to oppose discrimination.

    The intuition is that discrimination restricts the supply of jobs available to women, increasing demand for male labor and thereby raising male wages relative to the nondiscriminatory benchmark.

    Finally, we compare the relative wage of women $w_f/w_m$ in the competitive case, compared to the monopoly case. Under competition the relative wage equals {relative_w_competition:.2f} while under monopoly this equals {relative_w_monopoly:.2f}. Hence, the discount on female wages is larger under monopoly than under competition.

    This highlights that market structure matters for the extent of discriminatory outcomes: competition limits the ability of firms to sustain large wage gaps, even if it does not eliminate discrimination entirely.

    The following table summarizes this discussion.


    |variable|value|
    |----|---|
    |$\\alpha$| {alpha.value}|
    |$\\rho$| {rho.value} |
    | $u$ | 5 |
    | $(w_f/w_m)^c$| {relative_w_competition:.2f} |
    | $(w_f/w_m)^m$ | {relative_w_monopoly:.2f} |

    ## Parameter sweep

    The following figure shows how the competitive wage ratio $(w_f/w_m)^c$ and monopoly ratio $(w_f/w_m)^m$ vary with $u$. Click the following button to calculate the equilibria for a range of values of $u$ and $a_f$.
    """)
    return


@app.cell
def _(mo):
    calculate_button = mo.ui.run_button(
        label="Calculate equilibria"
    )



    calculate_button
    return (calculate_button,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using list comprehension we calculate the perfect equilibrium and monopoly outcomes for combinations of $u$ and the female labor supply parameter $a_f$.
    """)
    return


@app.cell
def _(
    calculate_button,
    competitive_outcome,
    mo,
    monopoly_outcome,
    np,
    pd,
    u_value,
):
    mo.stop(not calculate_button.value)

    range_u = np.linspace(0, u_value, 3)
    range_a = np.linspace(3, 5, 3)

    combinations = np.array(
        [(u, a) for u in range_u for a in range_a]
    )

    monopoly_outcomes = np.array([
        monopoly_outcome(u, af).x
        for u, af in combinations
    ])

    competitive_outcomes = np.array([
        competitive_outcome(u, af)
        for u, af in combinations
    ])

    df = pd.DataFrame({
        'u': combinations[:,0],
        'af': combinations[:,1],
        'wf_m' : monopoly_outcomes[:,0],
        'wm_m' : monopoly_outcomes[:,1],
        'p_c'  : competitive_outcomes[:,0],
        'wf_c' : competitive_outcomes[:,1],
        'wm_c' : competitive_outcomes[:,2]
    })
    return (df,)


@app.cell
def _(calculate_button, df, mo, plt):
    mo.stop(not calculate_button.value)
    plt.plot(df[df.af==5].u,df[df.af==5].wf_m/df[df.af==5].wm_m,label="monopoly")
    plt.plot(df[df.af==5].u,df[df.af==5].wf_c/df[df.af==5].wm_c,label="perfect competition")
    plt.xlabel('$u$')
    plt.ylabel('$w_f/w_m$')
    plt.title('Female-to-male wage ratio by market structure')
    plt.legend()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When $u=0$ there is no discrimination in either market configuration. As the distaste parameter $u$ increases, female relative wage falls, but it falls faster under monopoly than it does under competition. Hence, the result above that monopoly leads to more discrimination than competition does not depend on the particular choice of $u$.

    Finally, we analyze how the ratio of relative wages $(w_f/w_m)^c/(w_f/w_m)^m$ is affected by the supply elasticity of female labor supply. Above, we assumed that women and men had the same labor supply function: $a_f = a_m = a = 5$. Now we allow $a_f < 5$. One interpretation is that due to social convention women tend to face a higher outside option once children arrive in their families.
    """)
    return


@app.cell
def _(calculate_button, df, mo, plt):
    mo.stop(not calculate_button.value)

    plt.plot(df[df.af==5].u,(df[df.af==5].wf_c/df[df.af==5].wm_c)/(df[df.af==5].wf_m/df[df.af==5].wm_m),label="$a_f = 5$")
    plt.plot(df[df.af==3].u,(df[df.af==3].wf_c/df[df.af==3].wm_c)/(df[df.af==3].wf_m/df[df.af==3].wm_m),label="$a_f = 3$")

    plt.xlabel('$u$')
    plt.ylabel('$(w_f/w_m)^c/(w_f/w_m)^m$')
    plt.title('Comparing relative female-to-male wage ratios by $a_f$')
    plt.legend()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When $u=0$ we know there is no discrimination and the wage ratio $w_f/w_m$ equals 1 under both competition and monopoly. As we saw above, as $u$ increases the female wage ratio falls faster under monopoly than under competition; hence $(w_f/w_m)^c/(w_f/w_m)^m$ increases with $u$. When female labor supply becomes less elastic ($a_f$ falls), a monopolist is willing to offer a higher wage. Indeed, a given wage leads to lower labor supply and hence lower output. The monopolist is then willing to raise $w_f$. Consequently, $(w_f/w_m)^m$ does not fall as quickly relative to $(w_f/w_m)^c$ with lower $a_f$. Hence, the ratio $(w_f/w_m)^c/(w_f/w_m)^m$ decreases as $a_f$ falls.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Conclusion

    This app illustrates that taste based discrimination leads to lower wages for women compared to men. For given taste parmater $u > 0$, the female relative wage $w_f/w_m$ falls with monopoly/monopsony power. In this sense, competition has some disciplining effect on discrimination but does not necessarily eliminate it.

    As female labor supply becomes less elastic, the difference between monopoly and competitive relative wages $w_f/w_m$ becomes smaller.

    When female and male labor become closer substitutes in production ($\rho$ closer to 1.0), the outcomes in the app become less reliable as the numerical solvers become unstable.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

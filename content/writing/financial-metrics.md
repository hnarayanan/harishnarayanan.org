---
date: 2015-11-26T20:44:48Z
draft: true
title: A beginner's guide to financial performance and risk metrics
includes_math: yes
---

An introduction to classical financial metrics used to describe
performance time series, and compare different series.

{{< figure src="https://c1.staticflickr.com/9/8508/8597609828_ccbd6c740f_k.jpg" title="" >}}

As someone who's new to finance, it might be difficult to ... Summarises wikipedia, and cross-references it with zipline.

## Sharpe Ratio

The [Sharpe Ratio](http://en.wikipedia.org/wiki/Sharpe_ratio) is a way of examining the performance of an investment by adjusting for its risk. It measures the excess return of your asset with respect to some benchmark per unit deviation of your asset (usually called *risk*).

Its definition has historically undergone a few changes, but the
current form is:

$$  \begin{aligned}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} &amp; = \frac{4\pi}{c}\vec{\mathbf{j}} \\   \nabla \cdot \vec{\mathbf{E}} &amp; = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} &amp; = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} &amp; = 0 \end{aligned}
$$

        S_p =    E(R_a - R_b)
              -------------------  ,
              sqrt(var(R_a - R_b))

where E(.) = Expected value of .
      var(.) = Variance of .
      R_a = Asset return
      R_b = Benchmark return

~~~python
def sharpe_ratio(asset_volatility, asset_return, benchmark_return):
    if approx_equals(volatility, 0):
        return 0.0

    return (asset_return - benchmark_return) / asset_volatility
~~~


## Sortino Ratio

## Information Ratio

## Alpha

## Beta

## Volatility


## Excess return

## Maximum drawdown

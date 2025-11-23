"""
Visualization utilities:
- Plot conversion rates
- Plot confidence intervals
"""

import matplotlib.pyplot as plt


def plot_conversion_rates(rate_a, rate_b):
    plt.figure(figsize=(6, 4))
    plt.bar(["Variant A", "Variant B"], [rate_a, rate_b])
    plt.ylabel("Conversion Rate")
    plt.title("Conversion Rate Comparison")
    plt.tight_layout()
    plt.show()


def plot_confidence_interval(lower, upper):
    plt.figure(figsize=(6, 4))
    plt.errorbar(
        x=[0],
        y=[(lower + upper) / 2],
        yerr=[[(upper - lower)/2], [(upper - lower)/2]],
        fmt="o",
        capsize=8,
    )
    plt.xticks([0], ["Difference (B - A)"])
    plt.title("95% Confidence Interval of Conversion Difference")
    plt.tight_layout()
    plt.show()

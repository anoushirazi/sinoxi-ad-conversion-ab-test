"""
Core A/B testing logic:
- Compute conversion rates
- Run statistical hypothesis tests (z-test, chi-square)
- Calculate confidence intervals and effect sizes
"""

import numpy as np
from scipy import stats


def conversion_rate(successes, total):
    return successes / total


def z_test_proportions(success_a, total_a, success_b, total_b):
    p1 = conversion_rate(success_a, total_a)
    p2 = conversion_rate(success_b, total_b)
    p_pool = (success_a + success_b) / (total_a + total_b)

    se = np.sqrt(p_pool * (1 - p_pool) * (1/total_a + 1/total_b))
    z = (p2 - p1) / se
    p_value = 1 - stats.norm.cdf(z)

    return z, p_value


def confidence_interval_difference(success_a, total_a, success_b, total_b, alpha=0.05):
    p1 = conversion_rate(success_a, total_a)
    p2 = conversion_rate(success_b, total_b)
    diff = p2 - p1

    se = np.sqrt((p1 * (1 - p1)) / total_a + (p2 * (1 - p2)) / total_b)
    z = stats.norm.ppf(1 - alpha/2)

    lower = diff - z * se
    upper = diff + z * se
    return lower, upper

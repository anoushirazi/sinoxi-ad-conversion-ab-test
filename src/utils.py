"""
Utility helpers:
- Summary formatting
- Simple printing utilities
"""


def summarize_results(z, p_value, ci):
    lower, upper = ci
    return {
        "z_score": z,
        "p_value": p_value,
        "ci_lower": lower,
        "ci_upper": upper,
    }

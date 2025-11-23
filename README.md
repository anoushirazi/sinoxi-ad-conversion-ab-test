# Sinoxi Ad Conversion A/B Test

## Project Overview
This project evaluates whether a new ad delivery strategy improves user conversion rates in a FinTech marketing campaign compared to the existing strategy.

---

## Repository Structure

```
sinoxi-ad-conversion-ab-test/
│
├── data/
│   ├── raw/
│   │   └── ad_campaign_raw.csv
│   ├── processed/
│   │   └── ad_campaign_clean.csv
│
├── notebooks/
│   └── ab_test_analysis.ipynb
│
├── src/
│   ├── init.py
│   ├── ab_test.py
│   ├── data_preprocessing.py
│   ├── metrics.py
│   ├── utils.py
│   └── visualize.py
│
├── results/
│   ├── figures/
│   │   ├── conversion_rates.png
│   │   └── confidence_intervals.png
│   └── summary_report.md
│
├── README.md
├── requirements.txt
└── .gitignore
```


---

## Dataset
- The dataset consists of user-level records from an A/B test.
- Key fields include `user_id`, `test_group` (control "ad" vs treatment "psa"), `converted` (binary), `total_ads`, `most_ads_day`, and `most_ads_hour`.
- Raw data lives in `data/raw/` and cleaned data is in `data/processed/`.

---

## Methodology
- Data preprocessing cleans and balances the groups.
- Conversion rates by group are calculated.
- Two-proportion Z-tests and chi-square tests evaluate statistical significance.
- 95% confidence intervals are computed for conversion lifts.
- Visualizations depict conversion rates and confidence intervals.

---

## Key Results

| Metric                         | Value           |
|--------------------------------|-----------------|
| Control conversion rate        | 2.71%           |
| Treatment conversion rate      | 1.79%           |
| Conversion lift                | -0.92 percentage points |
| Statistical significance (p-value) | 0.00000 (Z-test) and 1.821e-11 (Chi-square) |

The treatment group shows a statistically significant lower conversion rate very unlikely due to chance.

---

## Business Recommendation
It is recommended to **retain the existing ad delivery strategy**, as the new approach demonstrated a statistically significant decrease in user conversion rates.

---

## Visualizations

### Conversion Rates with 95% Confidence Intervals
![conversion_rates.png](https://github.com/anoushirazi/sinoxi-ad-conversion-ab-test/blob/main/results/figures/conversion_rates.png)

### Confidence Intervals for Conversion Rates
![confidence_intervals.png](https://github.com/anoushirazi/sinoxi-ad-conversion-ab-test/blob/main/results/figures/confidence_intervals.png)

---

## Technologies Used
- Python (Pandas, NumPy)
- Statistical libraries (SciPy, Statsmodels)
- Visualization (Matplotlib, Seaborn)
- Jupyter Notebooks

---

## How to Run
1. Clone the repo.
2. Install dependencies from `requirements.txt`.
3. Run `notebooks/ab_test_analysis.ipynb` to reproduce analysis and visuals.

This project demonstrates rigorous A/B testing practices in a FinTech marketing context, showing data cleaning, statistical testing, and clear result communication.


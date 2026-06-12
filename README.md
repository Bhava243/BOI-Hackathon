# BOI Hackathon - Fraud Detection

This is my project for the BOI Hackathon. I built a fraud detection system using machine learning and a streamlit dashboard.

---

## What i did

I took a bank transaction dataset given by BOI and trained a Random Forest model to detect fraud. The target column given by BOI was `F3924` (0 = Normal, 1 = Fraud). Then i added a dashboard to show the results and a graph to visualize how money moves through mule accounts.

---

## Results

- Accuracy: 99.61%
- Precision: 100%
- Recall: 67%
- F1 Score: 80%
- Total transactions: 9082
- Fraud cases: 81
- High risk accounts found: 12

The confusion matrix shows 1801 correct normal predictions and only 16 fraud cases were missed.

---

## Charts

- `fraud_distribution.png` - shows how many normal vs fraud transactions
- `correlation_heatmap.png` - feature correlation between the 18 selected features
- `feature_importance.png` - F2737 and F3836 were the most important features
- `model_comparison.png` - compared Random Forest, Decision Tree, and Logistic Regression
- `confusion_matrix.png` - final model predictions vs actual

---

## Files

- `Fraud_dashboard.py` - streamlit dashboard
- `Fraud_analysis.ipynb` - model training notebook
- `DataSet.csv` - dataset
- `requirements.txt` - libraries needed

---

## How to run

```
pip install -r requirements.txt
streamlit run Fraud_dashboard.py
```

---

## Libraries used

- pandas
- scikit-learn
- matplotlib
- seaborn
- streamlit
- networkx

---

*Made by Bhava243 for BOI Hackathon*

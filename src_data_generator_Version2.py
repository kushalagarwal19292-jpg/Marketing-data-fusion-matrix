import numpy as np
import pandas as pd

def generate_7ps_data(n_records=1000, random_state=42):
    np.random.seed(random_state)
    df = pd.DataFrame({
        'product_usage': np.random.gamma(2, 20, n_records),
        'product_sentiment': np.random.normal(0.7, 0.1, n_records),
        'price_elasticity': np.random.uniform(0.5, 1.5, n_records),
        'competitor_pricing': np.random.normal(100, 10, n_records),
        'geo_demand': np.random.poisson(30, n_records),
        'channel_performance': np.random.uniform(0, 1, n_records),
        'promotion_ROI': np.random.normal(2, 0.5, n_records),
        'promotion_engagement': np.random.normal(0.5, 0.15, n_records),
        'crm_score': np.random.beta(2, 1, n_records),
        'customer_satisfaction': np.random.normal(0.8, 0.1, n_records),
        'funnel_efficiency': np.random.normal(0.6, 0.08, n_records),
        'process_dropoff': np.random.uniform(0, 0.3, n_records),
        'reviews_score': np.random.normal(4, 0.5, n_records),
        'ux_signal': np.random.normal(0.75, 0.12, n_records),
    })
    # Simple marketing performance metric (target)
    df['marketing_performance'] = (
        0.2*df['promotion_ROI'] + 0.15*df['funnel_efficiency'] +
        0.1*df['crm_score'] + 0.1*df['product_sentiment'] +
        0.15*df['channel_performance'] - 0.1*df['process_dropoff'] +
        np.random.normal(0, 0.1, n_records)
    )
    return df

if __name__ == "__main__":
    df = generate_7ps_data()
    df.to_csv("data/synthetic_7ps_dataset.csv", index=False)
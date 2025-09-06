import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

class FusionEngine:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.X = df.drop('marketing_performance', axis=1)
        self.y = df['marketing_performance']
        self.model = None
        self.train_model()

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        self.score = r2_score(y_test, self.model.predict(X_test))

    def correlate(self):
        # Feature importances (coefficients)
        coefs = pd.Series(self.model.coef_, index=self.X.columns)
        return coefs.sort_values(ascending=False)

    def simulate(self, feature, new_value):
        """Simulate a what-if scenario for a single feature."""
        mean_row = self.X.mean().copy()
        mean_row[feature] = new_value
        pred = self.model.predict([mean_row.values])[0]
        return pred

    def prescribe(self):
        """Suggest actions based on strongest drivers."""
        coefs = self.correlate()
        top_features = coefs.head(3).index.tolist()
        actions = {
            feat: f"Increase {feat.replace('_', ' ')} to improve performance." for feat in top_features
        }
        return actions

    def retrain(self, new_df):
        self.df = new_df
        self.X = new_df.drop('marketing_performance', axis=1)
        self.y = new_df['marketing_performance']
        self.train_model()
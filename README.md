# Supply Chain Demand Forecasting & Inventory Optimization

End-to-end ML pipeline combining time series forecasting with inventory 
optimization to minimize stockout risk under demand uncertainty.

## What This Project Does

1. Forecasts weekly demand per SKU using SARIMA, Prophet, and LSTM
2. Quantifies forecast uncertainty through prediction intervals
3. Uses that uncertainty to optimize safety stock levels and reorder points
4. Monitors for data drift and model degradation in production

## Tech Stack

| Layer | Tools |
|---|---|
| Modeling | SARIMA, Prophet, LSTM (TensorFlow) |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Monitoring | Evidently AI |
| Deployment | Streamlit Community Cloud |
| CI/CD | GitHub Actions |
| Containerization | Docker |

## Project Structure

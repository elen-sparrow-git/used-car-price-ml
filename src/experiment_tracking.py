from datetime import datetime


results = []


def log_result(
    variant,
    model_name,
    model_key,
    rmse_mean,
    rmse_std,
    mae_mean,
    mae_std,
    mape_mean,
    mape_std,
    cv,
    params=None,
):
    if params is None:
        params = {}

    results.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "variant": variant,
        "model": model_name,
        "model_key": model_key,
        "rmse_mean": rmse_mean,
        "rmse_std": rmse_std,
        "mae_mean": mae_mean,
        "mae_std": mae_std,
        "mape_mean": mape_mean,
        "mape_std": mape_std,
        "cv": cv,
        "params": params,
    })
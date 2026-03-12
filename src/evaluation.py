from sklearn.model_selection import cross_validate


def regression_cv_metrics(model, X, y, cv=5):
    scores = cross_validate(
        model,
        X,
        y,
        scoring={
            "rmse": "neg_root_mean_squared_error",
            "mae": "neg_mean_absolute_error",
            "mape": "neg_mean_absolute_percentage_error",
        },
        cv=cv,
        n_jobs=-1,
    )

    rmse_scores = -scores["test_rmse"]
    mae_scores = -scores["test_mae"]
    mape_scores = -scores["test_mape"]

    return {
        "rmse_mean": rmse_scores.mean(),
        "rmse_std": rmse_scores.std(),
        "mae_mean": mae_scores.mean(),
        "mae_std": mae_scores.std(),
        "mape_mean": mape_scores.mean(),
        "mape_std": mape_scores.std(),
    }

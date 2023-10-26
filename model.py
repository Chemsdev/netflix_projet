import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import difflib
import streamlit as st 





def get_top_recommendations(movie_title:str):
    netflix_df = pd.read_csv("movie_metadata.csv")

    selected_columns = ['num_critic_for_reviews', 'duration', 'num_voted_users', 'budget', 'title_year',
                        'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes',
                        'cast_total_facebook_likes', 'num_user_for_reviews', 'imdb_score']

    features_and_target = netflix_df[selected_columns]

    imputer = SimpleImputer(strategy='mean')
    features_and_target_imputed = imputer.fit_transform(features_and_target[selected_columns[:-1]])

    features = features_and_target_imputed
    target = features_and_target['imdb_score']

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

    param_grid = {
        'alpha': [0.0001, 0.001, 0.01, 0.1, 1],
        'penalty': ['l1', 'l2', 'elasticnet'],
    }

    sgd_reg = SGDRegressor(max_iter=1000, learning_rate='constant', eta0=0.01, random_state=42)

    grid_search = GridSearchCV(sgd_reg, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
    grid_search.fit(X_train, y_train)

    best_sgd_reg = grid_search.best_estimator_

    predictions_test = best_sgd_reg.predict(X_test)

    metrics_test = {
        'Mean Squared Error (MSE)': mean_squared_error(y_test, predictions_test),
        'Root Mean Squared Error (RMSE)': mean_squared_error(y_test, predictions_test, squared=False),
        'R-squared (R2) Score': r2_score(y_test, predictions_test),
        'Mean Absolute Error (MAE)': mean_absolute_error(y_test, predictions_test)
    }

    metrics_test_df = pd.DataFrame(list(metrics_test.items()), columns=['Metric', 'Value'])
    print("\nTest Set Evaluation Metrics:")
    print(metrics_test_df)

    netflix_df['lowercase_title'] = netflix_df['movie_title'].str.lower()
    movie_title_lower = movie_title.lower()

    closest_match = difflib.get_close_matches(movie_title_lower, netflix_df['lowercase_title'], n=1, cutoff=0.8)

    if not closest_match:
        print(f'Movie with title "{movie_title}" not found.')
        return

    matched_movie = netflix_df[netflix_df['lowercase_title'] == closest_match[0]]
    movie_features = matched_movie[selected_columns[:-1]].values

    movie_features_imputed = imputer.transform(movie_features)
    movie_features_scaled = scaler.transform(movie_features_imputed)
    movie_features_scaled_reshaped = movie_features_scaled.reshape(1, -1)
    predicted_imdb_score = best_sgd_reg.predict(movie_features_scaled_reshaped)[0]

    recommended_movies = netflix_df[netflix_df['imdb_score'] > predicted_imdb_score]

    top_recommendations = recommended_movies.sort_values(by='imdb_score', ascending=False).head(5)
    # (Predicted IMDb Score: {predicted_imdb_score}):
    print(f"Top 5 des films recommander pour '{movie_title}' ")
    st.write(top_recommendations[['movie_title', 'imdb_score']])

    netflix_df.drop('lowercase_title', axis=1, inplace=True)
    
    return top_recommendations[["movie_title"]]
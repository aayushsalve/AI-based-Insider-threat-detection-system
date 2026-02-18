import pandas as pd


def extract_features(activities_df, sensitive_df, login_df, users_df):
    """
    Extract meaningful features from raw activity data
    """
    features = pd.DataFrame()
    user_ids = users_df['user_id'].unique()

    for user_id in user_ids:
        user_features = {'user_id': user_id}

        # Activity features
        user_activities = activities_df[activities_df['user_id'] == user_id]
        user_features['total_activities'] = len(user_activities)
        user_features['failed_login_attempts'] = len(
            user_activities[user_activities['status'] == 'failed']
        )
        user_features['data_download_mb'] = user_activities[
            user_activities['activity_type'] == 'data_download'
        ]['data_volume_mb'].sum()

        # Sensitive file access features
        user_sensitive = sensitive_df[sensitive_df['user_id'] == user_id]
        user_features['sensitive_file_access_sum'] = len(user_sensitive)
        user_features['after_hours_access'] = len(
            user_sensitive[user_sensitive['is_after_hours'] is True]
        )

        # Login features
        user_login = login_df[login_df['user_id'] == user_id]
        user_features['unique_ips'] = user_login['source_ip'].nunique()
        user_features['failed_logins'] = len(
            user_login[user_login['login_status'] == 'failed']
        )

        features = pd.concat([features, pd.DataFrame([user_features])],
                             ignore_index=True)

    return features

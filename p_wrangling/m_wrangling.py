import pandas as pd
import re

def cleaning_data(df_cleaned) -> pd.DataFrame:
    """"
    Cleaning the data of the data frame.
    """

    print('Cleaning data...')

    # cleaning gender column.
    df_cleaned['gender'] = df_cleaned['gender'].astype("string").str.capitalize()
    df_cleaned['gender'] = df_cleaned['gender'].replace('Fem', 'Female')

    # cleaning age_group column.
    df_cleaned['age_group'] = df_cleaned['age_group'].replace('juvenile', '14_25')

    # cleaning age column.
    df_cleaned['age'] = df_cleaned['age'].astype("string")
    df_cleaned['age'] = df_cleaned['age'].str.replace(' years old', '')

    for x in range(1980, 2050):
        df_cleaned['age'] = df_cleaned['age'].str.replace(f'{x}', f'{2016 - x}')

    df_cleaned['age'] = df_cleaned['age'].astype('int64')

    # cleaning rural column.
    df_cleaned['rural'] = df_cleaned['rural'].str.lower()

    # cleaning dem_education_level column.
    df_cleaned['dem_education_level'] = df_cleaned['dem_education_level'].replace('no', 'no education')
    df_cleaned['dem_education_level'] = df_cleaned['dem_education_level'].fillna('no education')

    # cleaning children column column.
    df_cleaned['dem_has_children'] = df_cleaned['dem_has_children'].str.lower()

    # cleaning Q3 column.
    df_cleaned['question_bbi_2016wave4_basicincome_effect'] = \
        [re.sub(r'\‰Û_', '', x) for x in df_cleaned['question_bbi_2016wave4_basicincome_effect']]

    print('Cleaning data is done!')

    df_cleaned.to_csv('data/processed/data_cleaned.csv')

    print('data_cleaned.csv exported to data/processed folder!')

    return df_cleaned


def renaming_columns(df_renamed):
    print('Renaming columns...')
    df_renamed.rename(columns={'age': 'Age',
                               'gender': 'Gender',
                               'dem_has_children': 'Children',
                               'age_group': 'Age Group',
                               'country_code': 'Country Code',
                               'rural': 'Area',
                               'dem_education_level': 'Education Level',
                               'dem_full_time_job': 'Full Time Job',
                               'normalized_job_code': 'Job Code',
                               'question_bbi_2016wave4_basicincome_awareness': 'Q1: awareness',
                               'question_bbi_2016wave4_basicincome_vote': 'Q2: vote',
                               'question_bbi_2016wave4_basicincome_effect': 'Q3: effect',
                               'question_bbi_2016wave4_basicincome_argumentsfor': 'Q4: arguments for',
                               'question_bbi_2016wave4_basicincome_argumentsagainst': 'Q5: arguments against'},
                      inplace=True)


    print('Columns are renamed!')

    return df_renamed
import pandas as pd
from functools import reduce
from sqlalchemy import create_engine

def get_tables(path):
    """"
    :param: path of the data base
    :return: data frame with all the data, united by 'uuid'.
    """

    engine = create_engine(f'sqlite:///{path}')
    df_personal_info = pd.read_sql("SELECT * FROM personal_info", engine)
    df_country_info = pd.read_sql("SELECT * FROM country_info", engine)
    df_career_info = pd.read_sql("SELECT * FROM career_info", engine)
    df_poll_info = pd.read_sql("SELECT * FROM poll_info", engine)

    # getting the complete data frame
    dfs_list = [df_personal_info, df_country_info, df_career_info, df_poll_info]
    df_complete = reduce(lambda left, right: pd.merge(left, right, on='uuid'), dfs_list)

    # exporting the data frame to processed data folder.
    df_complete.to_csv(f'./data/processed/complete_dataframe.csv', index=True)
    return df_complete

def cleaning_data(df_complete) -> pd.DataFrame:

    print('Cleaning data...')

    # cleaning personal_info gender column.
    df_complete['gender'] = df_complete['gender'].astype("string").str.capitalize()
    df_complete['gender'] = df_complete['gender'].replace('Fem', 'Female')

    # cleaning personal_info age_group column.
    df_complete['age_group'] = df_complete['age_group'].replace('juvenile', '14_25')

    # cleaning personal_info age column.
    df_complete['age'] = df_complete['age'].astype("string")
    df_complete['age'] = df_complete['age'].str.replace(' years old', '')

    for x in range(1980, 2050):
        df_complete['age'] = df_complete['age'].str.replace(f'{x}', f'{2016 - x}')

    df_complete['age'] = df_complete['age'].astype('int64')

    # cleaning country_info rural column.
    df_complete['rural'] = df_complete['rural'].str.lower()

    # cleaning career_info dem_education_level column.
    df_complete['dem_education_level'] = df_complete['dem_education_level'].replace('no', 'no education')
    df_complete['dem_education_level'] = df_complete['dem_education_level'].fillna('no education')

    print('Cleaning data is done!')

    return df_complete

# connecting to API
def get_jobs(path, key):
    pass

# using web scraping to get the country names by the cuntry codes.
def get_country(x):
    pass


def acquire(path):
    # aquí se debe conectar todas las fuentes de datos: df_complete, api y web scraping.
    pass

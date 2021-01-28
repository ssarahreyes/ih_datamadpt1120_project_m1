import pandas as pd
from functools import reduce
from sqlalchemy import create_engine
import requests
from bs4 import BeautifulSoup
import re

def get_tables():
    """"
    from the path for the data base, we obtain a data frame
    with all the data united by 'uuid' column.
    """

    print('Connecting to the data base...')

    path = 'data/raw/raw_data_project_m1.db'
    engine = create_engine(f'sqlite:///{path}')
    df_personal_info = pd.read_sql("SELECT * FROM personal_info", engine)
    df_country_info = pd.read_sql("SELECT * FROM country_info", engine)
    df_career_info = pd.read_sql("SELECT * FROM career_info", engine)
    df_poll_info = pd.read_sql("SELECT * FROM poll_info", engine)

    # getting the complete data frame
    dfs_list = [df_personal_info, df_country_info, df_career_info, df_poll_info]
    df_info = reduce(lambda left, right: pd.merge(left, right, on='uuid'), dfs_list)

    # exporting the data frame to processed d$ata folder.
    df_info.to_csv(f'./data/processed/info_dataframe.csv', index=True)

    print('Connected to the data base.')

    return df_info

# connecting API
def get_jobs(df_api):

    print('Connecting to API...')

    # creating a dict with codes and countries
    job_code_unique = df_api['normalized_job_code'].unique()

    list_uuid_key = []
    list_title_value = []

    for code in job_code_unique:
        response = requests.get(f'http://api.dataatwork.org/v1/jobs/{code}').json()
        if list(response.keys())[0] == 'error':
            pass
        else:
            list_uuid_key.append(response['uuid'])
            list_title_value.append(response['title'])

    dict_uuid_jobs_title = dict(zip(list_uuid_key, list_title_value))

    # applying this dict to the data frame columns.
    df_api['Job Title'] = df_api['normalized_job_code']

    for uuid, title in dict_uuid_jobs_title.items():
        df_api.loc[df_api['normalized_job_code'] == uuid, 'Job Title'] = title

    # changing null values in Job Title column.
    df_api['Job Title'] = df_api['Job Title'].fillna('No job')

    print('Info of API added to data frame.')

    return df_api

# using web scraping to get the country names by the country codes.
def get_country(df_complete):

    print('Doing web scraping to extract countries info...')

    # scraping web.
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    # obtaining the data
    table = soup.find_all('div', {'class': 'mw-content-ltr'})[0]
    table_countries = table.find_all('table')
    all_info_countries = [info.text for info in table_countries]

    # cleaning the info countries.
    countries_without_spaces = [re.sub(r'\s', '', x) for x in all_info_countries]
    countries_without_symbols = [re.sub(r'\*', '', x) for x in countries_without_spaces]
    countries_without_squarebrackets = [re.sub(r'\[\d', '', x) for x in countries_without_symbols]
    countries_clean = ''.join(countries_without_squarebrackets)  # everything together to do split
    country_value = re.split(r'\(\w{0,7}\)', countries_clean)   # extract country names
    country_key = re.findall(r'\(\w{0,7}\)', countries_clean)  # extract the codes
    country_key = [re.sub(r'\(|\)', '', x) for x in country_key]  # without squarebrackets
    dic_countries = dict(zip(country_key, country_value))

    df_complete['Country'] = df_complete['country_code']

    for code, name in dic_countries.items():
        df_complete.loc[df_complete['country_code'] == code, 'Country'] = name

    print('Info of countries added to data frame.')

    return df_complete
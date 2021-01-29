
def adding_quantity(df_quantity):
    """"
    Quantity column to calculate in next functions the the number of
    people with the same job in each country that have voted.
    """

    print('Creating Quantity column...')

    df_quantity['Quantity'] = df_quantity.groupby('uuid')['uuid'].transform('count').astype("int64")

    print('Quality column added.')

    return df_quantity


def adding_percentage(df_percentage):
    """"
    Adding a percentage column with the percentage of votes for each country.
    """

    print('Creating Percentage column...')

    list_countries = df_percentage['Country'].unique().tolist()

    # adding total votes per country column to calculate percentage.
    df_percentage['Total Votes Per Country'] = 0

    for country in list_countries:
        df_percentage.loc[df_percentage['Country'] == country, 'Total Votes Per Country'] = \
            df_percentage.loc[df_percentage['Country'].str.contains(country), 'Quantity'].sum()

    df_percentage['Percentage'] = ((df_percentage['Total Votes Per Country'] /
                                   df_percentage['Total Votes Per Country'].sum())*100).round(6)

    print('Percentage column added.')

    df_percentage.to_csv('data/processed/all_data.csv')

    print('all data exported to data/processed folder!')

    return df_percentage



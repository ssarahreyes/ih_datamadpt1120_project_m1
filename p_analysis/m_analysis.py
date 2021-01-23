
def adding_quantity(df_quantity):

    print('Creating Quality column...')

    df_quantity['Quantity'] = df_quantity.groupby('uuid')['uuid'].transform('count').astype("int64")

    print('Quality column added.')

    return df_quantity


def adding_percentage(df_percentage):

    print('Creating Percentage column...')

    list_countries = df_percentage['Country'].unique().tolist()

    # adding total votes per country column to calculate percentage.
    df_percentage['Total Votes Per Country'] = 0

    for country in list_countries:
        df_percentage.loc[df_percentage['Country'] == country, 'Total Votes Per Country'] = \
            df_percentage.loc[df_percentage['Country'].str.contains(country), 'Quantity'].sum()

    df_percentage['Percentage'] = (df_percentage['Total Votes Per Country'] / df_percentage['Total Votes Per Country'].sum())
    # adding the % symbol
    df_percentage['Percentage'] = df_percentage['Percentage'].astype(float).map(lambda x: '{:.4%}'.format(x))

    print('Percentage column added.')

    return df_percentage



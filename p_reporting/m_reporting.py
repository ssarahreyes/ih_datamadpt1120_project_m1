
def export_table(df_final, country):

    print('Time to export the Data Frame...')

    # exporting the table for every country
    df_result = df_final[['Country', 'Job Title', 'Age', 'Quantity', 'Percentage']]

    list_countries = df_final['Country'].unique().tolist()

    if country == 'all countries':
        print('exporting all_countries_data.csv file...')
        df_result.to_csv('data/result/all_countries_data.csv')
        return 'file exported!'

    if country in list_countries:
        df_result_per_country = df_result[df_result['Country'] == f'{country}']
        print('exporting result_per_country.csv file')
        df_result_per_country.to_csv('data/result/result_per_country.csv')
        return 'file exported!'

    print('Data Frame exported!')
import re
import pandas as pd

def export_table(df_final, country):

    print('Time to export the Data Frame...')

    # exporting the table for all countries.
    df_result = df_final[['Country', 'Job Title', 'Age', 'Quantity', 'Percentage']].\
        groupby(['Country', 'Job Title'], as_index=False).\
        agg(Age=('Age', 'mean'), Quantity=('Quantity', 'sum'), Percentage=('Percentage', 'sum'))

    df_result = df_result.round({'Age': 2, 'Percentage': 6})

    list_countries = df_final['Country'].unique().tolist()

    if country == 'all countries':
        print('exporting all_countries_data.csv file...')
        df_result.to_csv('data/result/all_countries_data.csv')
        return 'file exported!'

    # exporting the final table for the country selected.
    if country in list_countries:
        df_result_per_country = df_result[df_result['Country'] == f'{country}']
        print('exporting result_per_country.csv file')
        df_result_per_country.to_csv(f'data/result/result_per_country_{country}.csv', index=False)
        return 'file exported!'

    print('Data Frame exported!')

# bonus 1
def export_votes(df_votes):
    """"
    Calculate total votes for pro and against arguments and exporting a table.
    """
    print("Let's calculate the number of votes...")

    # extracting data for Q4: pro arguments.
    arguments_for = [info for info in df_votes['Q4: arguments for']]
    all_arguments_for = ' '.join(arguments_for)
    arguments_pro_split_mayus = re.findall('[A-Z][^A-Z]*', all_arguments_for)
    arguments_pro_without_verticalbar = [re.sub('\ \| +', '', x) for x in arguments_pro_split_mayus]
    arguments_pro_cleaned = [re.sub(' [^ ]*$', '', x) for x in arguments_pro_without_verticalbar]

    # number of votes for each pro argument.
    more_equality = sum(map(lambda x: x == 'It creates more equality of' or \
                                      x == 'It creates more equality of opportunity',
                            arguments_pro_cleaned))
    financial_independence = sum(map(lambda x: x == 'It encourages financial independence and' or \
                                               x == 'It encourages financial independence and self-responsibility',
                                     arguments_pro_cleaned))
    household_appreciation = sum(map(lambda x: x == 'It increases appreciation for household work and' or \
                                               x == 'It increases appreciation for household work and volunteering',
                                     arguments_pro_cleaned))
    solidarity = sum(map(lambda x: x == 'It increases solidarity, because it is funded by' or \
                                   x == 'It increases solidarity, because it is funded by everyone',
                         arguments_pro_cleaned))
    reduces_anxiety = sum(map(lambda x: x == 'It reduces anxiety about financing basic' or \
                                        x == 'It reduces anxiety about financing basic needs',
                              arguments_pro_cleaned))
    reduces_boreaucracy_expenses = sum(map(lambda x: x == 'It reduces bureaucracy and administrative' or \
                                                     x == 'It reduces bureaucracy and administrative expenses',
                                           arguments_pro_cleaned))
    none_of_above = sum(map(lambda x: x == 'None of the above', arguments_pro_cleaned))

    number_pro_favor_votes = more_equality + financial_independence + household_appreciation + solidarity \
                             + reduces_anxiety + reduces_boreaucracy_expenses
    number_pro_against_votes = none_of_above

    # extracting data for Q5: against arguments.
    arguments_against = [info for info in df_votes['Q5: arguments against']]
    all_arguments_against = ' '.join(arguments_against)
    arguments_against_split_mayus = re.findall('[A-Z][^A-Z]*', all_arguments_against)
    arguments_against_without_verticalbar = [re.sub('\ \| +', '', x) for x in arguments_against_split_mayus]
    arguments_against_cleaned = [re.sub(' [^ ]*$', '', x) for x in arguments_against_without_verticalbar]

    # number of votes for each against argument.
    foreigners = sum(map(lambda x: x == 'Foreigners might come to my country and take advantage of the' or\
                                   x == 'Foreigners might come to my country and take advantage of the benefit',
                         arguments_against_cleaned))
    state_dependence = sum(map(lambda x: x == 'It increases dependence on the' or\
                                         x == 'It increases dependence on the state',
                               arguments_against_cleaned))
    against_merit = sum(map(lambda x: x == 'It is against the principle of linking merit and' or\
                                      x == 'It is against the principle of linking merit and reward',
                            arguments_against_cleaned))
    impossible_finance = sum(map(lambda x: x == 'It is impossible to' or\
                                           x == 'It is impossible to finance', arguments_against_cleaned))
    stop_working = sum(map(lambda x: x == 'It might encourage people to stop' or\
                                     x == 'It might encourage people to stop working',
                           arguments_against_cleaned))
    only_needed = sum(map(lambda x: x == 'Only the people who need it most should get something from the' or\
                                    x == 'Only the people who need it most should get something from the state',
                          arguments_against_cleaned))
    none_of_above_ag = sum(map(lambda x: x == 'None of the above', arguments_against_cleaned))

    number_cons_favor = foreigners + state_dependence + against_merit + impossible_finance \
                          + stop_working + only_needed
    number_cons_against = none_of_above_ag

    # creating the data frame.
    votes = [['In favor', number_pro_favor_votes, number_cons_favor],\
             ['Against', number_pro_against_votes, number_cons_against]]
    number_of_votes = pd.DataFrame(votes, columns=['Position', 'Number of pro arguments', 'Number of cons arguments'])

    number_of_votes.to_csv('data/result/number_of_votes.csv', index=False)

    print("Votes calculated and exported as a data frame in data/result folder!")







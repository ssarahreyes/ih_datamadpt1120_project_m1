from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre
import argparse

def argument_parser():
    """"
    parse arguments to script
    """
    parser = argparse.ArgumentParser(description='get data of basic income survey')
    parser.add_argument("-c", "--country", help="specify country for the results", default="all countries", type=str)
    args = parser.parse_args()
    return args

def main(arguments):

    print('starting process')

    tables = mac.get_tables()
    df_cleaned = mwr.cleaning_data(tables)
    df_jobs = mac.get_jobs(df_cleaned)
    df_countries = mac.get_country(df_jobs)
    df_renamed = mwr.renaming_columns(df_countries)
    df_quantity = man.adding_quantity(df_renamed)
    df_percentage = man.adding_percentage(df_quantity)

    # exporting the first table
    mre.export_table(df_percentage, arguments.country)

    # bonus 1
    df_votes = mre.export_votes(df_percentage)

    # bonus 2
    df_skills = mre.skills(df_percentage)

    print('========================= Pipeline is complete. You may find the results in the folder '
          './data/results =========================')

if __name__ == '__main__':

    my_arguments = argument_parser()
    main(my_arguments)
import pandas as pd
from p_acquisition.m_acquisition import acquire

df_personal_info = pd.read_sql_query("SELECT * FROM personal_info", engine)

if __name__ == '__main__':
    print('hola')
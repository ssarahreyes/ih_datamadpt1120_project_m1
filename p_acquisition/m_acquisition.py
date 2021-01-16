import pandas as pd
from sqlalchemy import create_engine

# creating conexion string to read the data base.

def acquire():
    sqlitedb_rel_path = '../data/raw_data_project_m1.db'
    conn_str = f'sqlite:///{sqlitedb_rel_path}'
    engine = create_engine(conn_str)
    df_personal_info = pd.read_sql_query("SELECT * FROM personal_info", engine)
    return df_personal_info
# qué parametros tengo que pasarle?


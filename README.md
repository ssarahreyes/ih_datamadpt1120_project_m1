![alt text](https://images.pexels.com/photos/3943746/pexels-photo-3943746.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260)

# :bar_chart: Data Pipeline Basic Income Survey
In this project we have created a data pipeline that unites the results of the survey from a data base with data obtained from API connection and web scraping process in order to enrich the results. 

# :fast_forward: One-liner
```
python main.py -p /data/raw/raw_data_project_m1.db -c Spain
```
# :computer: Technology stack
- Python==3.7.3
- pandas==0.24.2
- sqlalchemy==1.3.16
- requests==2.23.0
- bs4==4.9.1
- numpy==1.18.1
- argparse==3.2

# :zap: Data
There are 3 different datasources involved:
- Tables (.db) with the results of the survey. You can see the data in data/raw folder.
- API. We will use the [API](http://dataatwork.org/data/) from the Open Skills Project.
- Web Scraping. Finally, we will need to retrieve information about country codes from [Eurostat website](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes).


# :file_folder: Folder structure
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── requirements.txt
    ├── README.md
    ├── main.py
    ├── notebooks
    │   ├── notebook1.ipynb
    ├── p_acquisition
    │   ├── __init__.py
    │   └── m_acquisition.py
    ├── p_wrangling
    │   ├── __init__.py
    │   └── m_wrangling.py
    ├── p_analysis
    │   ├── __init__.py
    │   └── m_analysis.py
    ├── p_reporting
    │   ├── __init__.py
    │   └── m_reporting.py
    └── data
        ├── raw
        ├── processed
        └── results
```

# :incoming_envelope: Contact info
If you have some question, email me to sarisinhache@gmail.com!


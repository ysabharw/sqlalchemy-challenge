# sqlalchemy-challenge

---

# SQLAlchemy Climate Analysis

## Overview

This project involves analyzing weather data from Hawaii using SQLAlchemy ORM, Pandas, Matplotlib, and Flask. The dataset is stored in a SQLite database, which includes temperature and precipitation data collected from various weather stations in Hawaii. The project is divided into two parts:

1. **Climate Data Analysis**: A Jupyter notebook (`climate_starter.ipynb`) is used to analyze the climate data.
2. **Climate App**: A Flask API (`app.py`) is created to serve the analysis results as JSON objects.

## Project Structure

```
├── Resources
│   ├── hawaii.sqlite  # The main SQLite database
│   ├── hawaii_measurements.csv
│   └── hawaii_stations.csv
├── Starter_Code
│   ├── app.py  # The Flask API file for climate data analysis
│   ├── climate_starter.ipynb  # The Jupyter notebook for the climate analysis
│   └── README.md  # This README file
└── __pycache__
```

### Files:

- **`app.py`**: Contains the Flask API routes, enabling users to query the weather data and obtain results in JSON format.

  - **Note**: *This file was completed with the help of Xpert Learning Assistant, StackOverflow, and GeeksforGeeks due to issues with the original code and SQLite file corruption.*
- **`climate_starter.ipynb`**: This notebook contains climate data analysis using SQLAlchemy ORM and Python, including temperature and precipitation trends over the past year in Hawaii.
- **`hawaii.sqlite`**: The SQLite database containing the Hawaii weather station data, including temperature, precipitation, and station information.

## Instructions

### Climate Data Analysis (Jupyter Notebook)

- Open `climate_starter.ipynb` in Jupyter Notebook.
- Analyze the dataset using SQLAlchemy ORM queries, Pandas, and Matplotlib.
- Use the SQLite database (`hawaii.sqlite`) to perform the following tasks:
  1. Precipitation Analysis
  2. Station Analysis
  3. Temperature Analysis

### Flask API (app.py)

- Run the Flask application with the following command:

  ```
  python app.py
  ```
- Available API routes:

  - **`/api/v1.0/precipitation`**: Returns the precipitation data for the last year.
  - **`/api/v1.0/stations`**: Returns a list of all weather stations.
  - **`/api/v1.0/tobs`**: Returns temperature observations of the most active station for the last year.
  - **`/api/v1.0/<start>`**: Returns the minimum, average, and maximum temperatures from a given start date.
  - **`/api/v1.0/<start>/<end>`**: Returns the minimum, average, and maximum temperatures for a date range.

### Key Features:

- **Flask API**: The API provides easy access to the climate data.
- **ORM Queries**: SQLAlchemy ORM queries are used to query the SQLite database efficiently.
- **Visualization**: Plots for temperature and precipitation trends over the last year.

## Libraries and Resources Used

### Python Libraries:

- **Flask**: A micro web framework for building the API.
- **SQLAlchemy**: Python's SQL toolkit and Object Relational Mapper (ORM).
- **Pandas**: Data manipulation and analysis library.
- **Matplotlib**: Visualization library for generating plots.

### External Resources:

- **Xpert Learning Assistant**: Helped with the structure and resolution of issues regarding the `hawaii.sqlite` file.
- **StackOverflow**: Provided insights into various technical challenges encountered during development.

  - [Connecting SQLite in Flask](https://stackoverflow.com/questions/44642102/sqlalchemy-flask-and-sqlite-connection-error)
  - [Querying SQLite Databases](https://stackoverflow.com/questions/51200910/querying-sqlite-database-in-python)
  - [SQLAlchemy Reflection Issues](https://stackoverflow.com/questions/56689171/sqlalchemy-reflecting-a-sqlite-database)
  - [Serializing Python Data to JSON](https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable)
  - [Setting Flask API Routes](https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask)
  - [Creating API Endpoints in Flask](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request)
  - [Database Reflections in SQLAlchemy](https://stackoverflow.com/questions/10957961/how-do-i-reflect-tables-in-an-existing-database-with-sqlalchemy)
- **GeeksforGeeks**: Reference for building Flask APIs, using SQLAlchemy ORM, and understanding SQL queries.

  - [SQLAlchemy ORM](https://www.geeksforgeeks.org/sqlalchemy-orm-creating-sessions/)
  - [Flask API Basics](https://www.geeksforgeeks.org/python-creating-api-using-flask/)
  - [Understanding Flask Routing](https://www.geeksforgeeks.org/routing-in-flask/)
  - [Using SQLAlchemy&#39;s ORM](https://www.geeksforgeeks.org/sqlalchemy-python/)
- **W3Schools**:

  - [SQLite Introduction](https://www.w3schools.com/sql/sqlite_intro.asp)
  - [Flask Tutorial](https://www.w3schools.com/python/python_flask_getting_started.asp)
- **Real Python**:

  - [Introduction to Flask](https://realpython.com/flask-by-example/)
  - [Using SQLAlchemy ORM in Flask](https://realpython.com/python-sqlite-sqlalchemy/)
- **Official Flask Documentation**:

  - [Flask API Documentation](https://flask.palletsprojects.com/en/2.0.x/)
  - [Serving JSON in Flask](https://flask.palletsprojects.com/en/2.0.x/api/#flask.jsonify)
- **Official SQLAlchemy Documentation**:

  - [SQLAlchemy ORM Documentation](https://docs.sqlalchemy.org/en/14/orm/)
  - [Reflecting Tables in SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/extensions/automap.html)
- **TutorialsPoint**:

  - [Python Flask Tutorial](https://www.tutorialspoint.com/flask/index.htm)
  - [Handling JSON in Flask](https://www.tutorialspoint.com/flask/flask_jsonify.htm)
- **DataCamp**:

  - [SQLAlchemy ORM Tutorial](https://www.datacamp.com/community/tutorials/tutorial-sqlalchemy-python)
- **PythonAnywhere Blog**:

  - [Deploying Flask Applications](https://help.pythonanywhere.com/pages/Flask/)
- **Programiz**:

  - [Pandas Summary Statistics](https://www.programiz.com/python-programming/pandas/summary-statistics)
- **Kite**:

  - [Creating APIs in Flask](https://www.kite.com/python/answers/how-to-create-a-restful-api-with-flask-in-python)
- **CodeAcademy**:

  - [Using SQLAlchemy with Python](https://www.codecademy.com/learn/learn-sql/articles/sqlalchemy-tutorial)
- **DB Browser for SQLite**: Software used to visualize and explore the SQLite database.

  - [Official DB Browser for SQLite](https://sqlitebrowser.org/)

### Key Issues Solved:

- **Database Corruption**: Original attempts to connect to the `hawaii.sqlite` database led to recursive corruption of the file. Xpert Learning Assistant and resources from StackOverflow helped solve the issue.
- **Reflection Issues**: Difficulty in reflecting tables in SQLAlchemy was resolved using the `automap_base()` function with support from StackOverflow.
- **Serialization Issues**: Encountered problems with converting SQLAlchemy results into JSON format, especially with datetime objects. This was resolved through custom serialization methods, using guidance from StackOverflow.

### Example Comment:

In the `app.py` file, I added the following comment:

```python
# Please note that app.py has been made WITH THE HELP OF Xpert Learning Assistant AS MY ORIGINAL CODE WAS NOT FETCHING
# HAWAII.SQLITE CORRECTLY, CAUSING RECURSIVE FILE CORRUPTION. THE USE OF XPERT LEARNING ASSISTANT, STACKOVERFLOW, GEEKSFORGEEKS,
# AND OTHER RESOURCES WAS ABSOLUTELY NECESSARY TO COMPLETE THIS PROJECT. 
```

## How to Run

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/your-repo/sqlalchemy-climate-analysis.git
   ```
2. Install the necessary dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Run the Flask API:

   ```
   python app.py
   ```
4. Navigate to `http://127.0.0.1:5000/` in your browser to access the available API routes.

---

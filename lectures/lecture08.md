<img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" />

# PRG550 Lecture #8
Monday July 25, 2022

## Lecture Objective

- Understand and practice data collection, data cleaning and data exploration steps in the data science process
- Gain experience using Pandas, seaborn for analysis and visualization
- Gain understanding of feature selection

## Pre-requisites

- Python version 3.9.9 installed on your computer and on Raspberry Pi
    check Python version with `python -V`
- Jupyter notebook server successfully running on Raspberry Pi and connecting with a browser from your PC
- Your Raspberry Pi is able to connect to the internet for data downloads

## Page Contents

- [Stages in the Data Science Process](#Stages-in-the-Data-Science-Process)
    - [Data Collection](#Data-Collection)
    - [Data Cleaning](#Data-Cleaning-1)
    - [Titanic Dataset](#Titanic-Dataset)
    - [Data Exploration and Analysis](#Data-Exploration-and-Analysis)
- [PRG550 Capstone Project](#PRG550-Capstone-Project)
    - [Data Collection, Cleaning, and Exploration](#Data-Collection,-Cleaning,-and-Exploration)
- [Class Exercise A](#Class-Exercise-A)
- [Class Exercise B](#Class-Exercise-B)


----------------------------------

## Stages in the Data Science Process

<p align="center">
<img src="images/data_process.png" alt="Stages in Data Science Process" width="600" />
</p>

To gain experience in the five stages of the data science process, we will focus on the Titanic dataset to provide you with an understanding and a chance to practice with libraries such as [Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)(click on 'Titanic data' box) and [Scikit-Learn](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#openml)


The objective of the Titanic analysis will be to predict whether a passenger will survive based on their data such as `Age`, `Fare`, `Cabin`, etc.

### Data Collection

How we collect data depends on a variety of factors such as
1. What question are we trying to answer?
1. What type of data is needed?
1. Does the data already exist?
1. What data fields are needed? Is the data source reliable?
1. Do we need to create and record the data ourselves? (ie via experiments, or through surveys)
    1. How will the data be saved for later use?

Because we are analyzing a historical accident, the data already exists and we next consider the best source of the data.

In [Lab 5](https://github.com/dora-lee/seneca-prg550-2022-spring/blob/main/labs/Lab05-Jupyter-and-Pandas.ipynb), we used a version of the Titanic dataset from the Pandas library and obtained a local copy using the `curl` command:

    !curl https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv --output titanic.csv
and loaded the csv into a dataframe:
    ```
    df = pd.read_csv('titanic.csv')
    df.head(5)
    ```

There are many other sources of the dataset and different ways to obtain it - try this [Google Titanic dataset search](https://www.google.com/search?q=titanic+dataset+csv) - how many results are returned?

When evaluating pre-existing datasets, it's important to select a reliable source of trustworthy data.

[OpenML](https://www.openml.org/search?type=data&status=active) is another source where you can download a version of the Titanic dataset.

For this lecture the [the Titanic dataset from Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html) will be used.


### Data Cleaning [^1]

Data cleaning is an important step to prepare data for analysis.  If input data is poor quality, any resulting analysis will also be poor (ie garbage in, garbage out).

When data cleaning, we explore the "physical" shape of data (ie structure of the data) and ask questions to guide the steps that will be needed to create a trustworthy dataset:
- what data fields are available? what do the fields represent?
- what are the data types?
- is there missing data?
- is the data uniform?
- is there unexpected data values?  (ie outliers or meaningless values)

Some steps to take during data cleaning:
1. remove duplicate or irrelevant data
1. repair data structure
1. repair data values
1. evaluate and validate methodology


### Titanic Dataset

The Titanic data set from [Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)(click on 'Titanic data' box) is stored as CSV and consists of the following data columns:

**PassengerId**: Id of every passenger.

**Survived**: This feature have value 0 and 1. 0 for not survived and 1 for survived.

**Pclass**: There are 3 classes: Class 1, Class 2 and Class 3.

    A proxy for socio-economic status (SES)
    1st = Upper
    2nd = Middle
    3rd = Lower    
    
**Name**: Name of passenger.

**Sex**: Gender of passenger.

**Age**: Age of passenger in years.

**SibSp**: # of siblings / spouses aboard the Titanic.

    The dataset defines family relations in this way...
    Sibling = brother, sister, stepbrother, stepsister
    Spouse = husband, wife (mistresses and fiancés were ignored)    
    
**Parch**: # of parents / children aboard the Titanic.

    The dataset defines family relations in this way...
    Parent = mother, father
    Child = daughter, son, stepdaughter, stepson
    Some children travelled only with a nanny, therefore parch=0 for them.    
    
**Ticket**: Ticket number of passenger.

**Fare**: Indicating the fare.

**Cabin**: The cabin of passenger.

**Embarked**: The embarked category.  C = Cherbourg, Q = Queenstown,S = Southampton


### Data Exploration and Analysis

Explore meaning of data fields and identify fields relevant to solve the question being asked.

The [Lecture 8 Jupyter Notebook](Lecture08-Jupyter-Notes.ipynb) demonstrates data collect, data cleaning, and data exploration in detail for the Titanic dataset.


## PRG550 Capstone Project

Given the BMP280 provides real-time temperature and pressure data, we must identify a quality historical dataset that includes temperature, atmospheric pressure.  Ideally, the dataset should include labels for the observed data such as `Windy`, `Foggy`, `Rainy`, `Sunny`, etc.

The [Environment Canada's Historical Data Site](https://climate.weather.gc.ca/historical_data/search_historic_data_e.html) does provide labelled weather data for Toronto Pearson Airport.  Data is available hourly and we will be training the model using 1 month's worth of hourly data.

To search on the historical data sice, use `Station Name=TORONTO INTL A` and `Station ID=51459`

Due to the labels provided by Environment Canada, the functional diagram has been revised from [Lecture 7](lecture07.md#PRG550-CapstoneProject) to the below.  Hot/Cold has been changed to Rain/NoRain.  As new information is discovered, changes like this are typical of the data science process.

<p align="center">
<img src="../lectures/images/project_functional_diagram_revised.png" alt="Raspbery Pi Temperature Prediction Functional Diagram" width="600" />
</p>

### Data Collection, Cleaning, and Exploration

[Lab 7](../labs/lab07.md) will show you how to collect data, clean data, and explore data from [Environment Canada's Historical Data Site](https://climate.weather.gc.ca/historical_data/search_historic_data_e.html) in order to prepare data to predict whether there will be `Rain` or `NoRain` 


## Class Exercise A
What are the differences between the Titanic dataset from Pandas and the OpenML version below?
```
from sklearn.datasets import fetch_openml
titanic = fetch_openml("titanic", version=1)
titanic.data.head(5)

titanic.target
```

1. Are there differences in the data fields?
1. Are there differences in the number of rows?
1. Are there differences in column values?
    

## Class Exercise B
List other data sites that could provide labelled weather data.  What weather labels do they provide?


[^1]: https://www.springboard.com/blog/data-analytics/data-cleaning/
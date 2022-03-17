# Movie-Recommendation-Engine
tmdb-movie-dataset-analysis is an report for analyzing the TMDB movie data containing information about 50000 movies from The Movie Database (TMDB). Firstly, the report raises some questions based on the dataset needed to be researched.

# How to run code
1. Open project in pycharm
2. Install "requirement.txt" file.
3. Run app.py

# We will perform Exploratory Data Analysis (EDA) in "MovieDatasetAnalysis.ipynb" notebook to find the insight according to the research questions and will draw the conclusion to illustrate these insights like...
* How have movie production trends varied over the years?
* What are the top 20 highest grossing movies? What are the top 20 most expensive movies?
* How do budgets correlate with revenues? Do higher budget movies have higher revenue?
* Do certain months of release associate with better revenues?
* Which months have seen the maximum releases?
* How do ratings correlate with commercial success (profits)?
* What run times are associated with each genre?
* Who are the top 20 directors who made highly rated films? The directors considered for should have made atleast 5 movies in the time period 1960 - 2015 represented in the dataset.
# Data Preprocessing
* We will clean the data like remove missing, duplicates, punctuations etc in  "Preprocessing.ipynb" notebook.
* We will apply some text preprossing steps like- TF-IDF, stemming , Lemmetization to clean the text
# Modelling
* We will make content based recommendation system by using Cosine-Similarity in NLP to recommend top 5 movies to a user based on their previous watch history.
* cosine similarity is a measure of similarity between two sequences of numbers. For defining it, the sequences are viewed as vectors in an inner product space, and the cosine similarity is defined as the cosine of the angle between them, that is, the dot product of the vectors divided by the product of their lengths. It follows that the cosine similarity does not depend on the magnitudes of the vectors, but only on their angle
# Model Deployment on heroku
* Wil create an interactive web app using pycharm and streamlit and deploy it to heroku app.

#Format of Data: .csv file #REQUIREMENTS #NUMPY (sudo -H pip3 install numpy) Numpy will help you to manage multi-dimensional arrays very efficiently. Maybe you won’t do that directly, but since the concept is a crucial part of data science, many other libraries (well, almost all of them) are built on Numpy. Simply put: without Numpy you won’t be able to use Pandas, Matplotlib, Scipy or Scikit-Learn. That’s why you need it on the first hand.

#Matplotlib I hope I don’t have to detail why data visualization is important. Data visualization helps you to better understand your data, discover things that you wouldn’t discover in raw format and communicate your findings more efficiently to others. The best and most well-known Python data visualization library is Matplotlib. I wouldn’t say it’s easy to use… But usually if you save for yourself the 4 or 5 most commonly used code blocks for basic line charts and scatter plots, you can create your charts pretty fast.

#Pandas (sudo apt-get install python3-pandas) To analyze data, we like to use two-dimensional tables – like in SQL and in Excel. Originally, Python didn’t have this feature. Weird, isn’t it? But that’s why Pandas is so important! I like to say, Pandas is the “SQL of Python.” (Eh, I can’t wait to see what I will get for this sentence in the comment section… ;-)) Okay, to be more precise: Pandas is the library that will help us to handle two-dimensional data tables in Python. In many senses it’s really similar to SQL, though.

#Scikit-Learn(sudo -H pip3 install scikit-learn) Without any doubt the fanciest things in Python are Machine Learning and Predictive Analytics. And the best library for that is Scikit-Learn, which simply defines itself as “Machine Learning in Python.” Scikit-Learn has several methods, basically covering everything you might need in the first few years of your data career: regression methods, classification methods, and clustering, as well as model validation and model selection. You can also use it for dimensionality reduction and feature extraction.

#Streamlit : Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. Only basic front‑end experience required to create app using streamlit.
 
The tools used in this report are Python libraries - numpy, pandas, and matplotlib, pycharm, streamlit, tmdb api. The Jupyter notebook is used to illustrate the interactive analysis.


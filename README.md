# Movie-Recommendation-Engine
tmdb-movie-dataset-analysis is an report for analyzing the TMDB movie data containing information about 50000 movies from The Movie Database (TMDB). Firstly, the report raises some questions based on the dataset needed to be researched. 
1. We will perform Exploratory Data Analysis (EDA) in "MovieDatasetAnalysis.ipynb" notebook to find the insight according to the research questions and will draw the conclusion to illustrate these insights.
2. We will clean the data like remove missing, duplicates, punctuations etc in  "Preprocessing.ipynb" notebook.
3. We will apply some text preprossing steps like- TF-IDF, stemming , Lemmetization to clean the text
4. We will create a NLP model using Cosine-Similarity to recommend top 5 movies to a user based on their previous watch history.
5. Wil create an interactive web app using pycharm and streamlit .

#Format of Data: .csv file #REQUIREMENTS #NUMPY (sudo -H pip3 install numpy) Numpy will help you to manage multi-dimensional arrays very efficiently. Maybe you won’t do that directly, but since the concept is a crucial part of data science, many other libraries (well, almost all of them) are built on Numpy. Simply put: without Numpy you won’t be able to use Pandas, Matplotlib, Scipy or Scikit-Learn. That’s why you need it on the first hand.

#Matplotlib I hope I don’t have to detail why data visualization is important. Data visualization helps you to better understand your data, discover things that you wouldn’t discover in raw format and communicate your findings more efficiently to others. The best and most well-known Python data visualization library is Matplotlib. I wouldn’t say it’s easy to use… But usually if you save for yourself the 4 or 5 most commonly used code blocks for basic line charts and scatter plots, you can create your charts pretty fast.

#Pandas (sudo apt-get install python3-pandas) To analyze data, we like to use two-dimensional tables – like in SQL and in Excel. Originally, Python didn’t have this feature. Weird, isn’t it? But that’s why Pandas is so important! I like to say, Pandas is the “SQL of Python.” (Eh, I can’t wait to see what I will get for this sentence in the comment section… ;-)) Okay, to be more precise: Pandas is the library that will help us to handle two-dimensional data tables in Python. In many senses it’s really similar to SQL, though.

#Scikit-Learn(sudo -H pip3 install scikit-learn) Without any doubt the fanciest things in Python are Machine Learning and Predictive Analytics. And the best library for that is Scikit-Learn, which simply defines itself as “Machine Learning in Python.” Scikit-Learn has several methods, basically covering everything you might need in the first few years of your data career: regression methods, classification methods, and clustering, as well as model validation and model selection. You can also use it for dimensionality reduction and feature extraction.

#Streamlit : Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. Only basic front‑end experience required to create app using streamlit.
 
The tools used in this report are Python libraries - numpy, pandas, and matplotlib, pycharm, streamlit, tmdb api. The Jupyter notebook is used to illustrate the interactive analysis.

# How to run code
1. Open project in pycharm
2. Install "requirement.txt" file.
3. Run app.py

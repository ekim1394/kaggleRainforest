# ds-dc-19

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

The Course materials for General Assembly's Data Science course in Washington D.C. (4/15/17 - 6/17/17)

## Exit Tickets

[Fill me out at the end of each class!](https://docs.google.com/forms/d/1kPJhaWTfFswgSGb2HwU1EBu9Kof0VOvNqzgcv0Hj7vk/viewform?edit_requested=true)

## Slack

You've all been invited to use [Slack](https://dsdc19.slack.com) for chat during class and the day.  Please consider this the primary way to contact other students. Office Hours are listed Weekly on Slack in the Office Hours Channel

## Your Team
 
**Lead Instructor:** [Alex Egorenkov](https://www.linkedin.com/in/aegorenkov/)
**Lead Instructor:** [Alex Sherman](https://www.linkedin.com/in/alexjmsherman)

## Schedule

| Class | Date | Topic | Instructor | Homework |
|:---:|:---:|:---|:---|:---|
| 1 | 4/15 | [What is Data Science](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson01_What_is_Data_Science) | | |
|   |      | [Exploratory Data Analysis with Pandas](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson02_EDA_with_Pandas) | Alex S. | IMDB with Pandas **[Pandas Homework](https://github.com/ga-students/ds-dc-19/blob/master/homework/pandas_homework_imdb.ipynb)** |
| 2 | 4/22 | [Git, Github, and the Command Line](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson03_Git_GitHub_and_the_CommandLine/) | Alex S. ||
|   |      | [Introduction to Machine Learning](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson04_Intro_to_Machine_Learning) | Alex E. | Command Line & First Project Presentation |
| 3 | 4/29 | [Statistics Fundamentals 1](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson05_Statistics_1) | Alex E. ||
|   |      | [Web Scraping and APIs](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson06_Web_Scraping_and_APIs) | Alex S. | Chipotle Python & Web Scraping - IMDB (Optional) |
| 4 | 5/6  | [Statistics Fundamentals 2](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson07_Statistics_2) | Alex E. ||
|   |      | [K-Nearest Neighbors (KNN)](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson08_KNN) | Alex S. | **[Final Project 2] Project Brainstorming - Project Question and Dataset Due** |
| 5 | 5/13 | [Evaluating Model Fit](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson09_Evaluating_Model_Fit) | Alex S. ||
|   |      | [Linear Regression](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson10_Linear_Regression) | Alex E. | Yelp Votes Linear Regression (Optional) |
| 6 | 5/20 | [Logistic Regression](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson11_Logistic_Regression)  | Alex S. ||
|   |      | [Introduction to Time Series](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson12_Intro_to_Time_Series) | Alex E. | **[Final Project 2] Project Outline** |
| 7 | 5/27 | [Decision Trees and Random Forests](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson13_Decision_Trees_and_Random_Forests) | Alex E. ||
|   |      | [Natural Language Processing (NLP)](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson14_NLP) | Alex S. | Naive Bayes with Yelp Review Text (Optional) & Draft Project Paper Due |
| 8 | 6/3  | [Dimensionality Reduction](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson15_Dimensionality_Reduction) | Alex E. ||
|   |      | [Unsupervised Learning - Clustering](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson16_Unsupervised_Learning) | Alex S. | **[Final Project 3] Exploratory Data Analysis** |
| 9 | 6/10 | [Advanced Sklearn] | Alex S. ||
|   |      | [Modeling Time Series Data](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson18_Modeling_Time_Series_Data) | Alex E. | **[Final Project 4] Modeling and Analysis** |
| 10| 6/17 | [Introduction to Databases](https://github.com/ga-students/ds-dc-19/tree/master/lessons/Lesson19_Introduction_to_Databases) | Alex E. ||
|   |      | [Data Science Careers] | ||
|   |      | [Final Project Presentations] |  |  **[Final Project 5] Presentationss** |


### Class 1:

**Class Resources:**
* MovieLens 100k movie ratings ([data dictionary](http://files.grouplens.org/datasets/movielens/ml-100k-README.txt), [website](http://grouplens.org/datasets/movielens/))
* Alcohol consumption by country ([article](http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/))
* Reports of UFO sightings ([website](http://www.nuforc.org/webreports.html))

**Pandas Resources:**
* Browsing or searching the Pandas [API Reference](http://pandas.pydata.org/pandas-docs/stable/api.html) is an excellent way to locate a function even if you don't know its exact name.
* To learn more Pandas, read this [three-part tutorial](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/), 
or review these two excellent (but extremely long) notebooks on Pandas: 
[introduction](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_5-Introduction-to-Pandas.ipynb) and 
[data wrangling](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_6-Data-Wrangling-with-Pandas.ipynb).
* If you want to go really deep into Pandas (and NumPy), read the book [Python for Data Analysis](http://amzn.to/1JomygU), written by the creator of Pandas.
* This notebook demonstrates the different types of [joins in Pandas](notebooks/05_pandas_merge.ipynb), for when you need to figure out how to merge two DataFrames.
* This is a nice, short tutorial on [pivot tables](https://beta.oreilly.com/learning/pivot-tables) in Pandas.

**Python Resources:**
* [Codecademy's Python course](http://www.codecademy.com/en/tracks/python): Good beginner material, including tons of in-browser exercises.
* [DataQuest](https://dataquest.io/): Similar interface to Codecademy, but focused on teaching Python in the context of data science.
* [Google's Python Class](https://developers.google.com/edu/python/): Slightly more advanced, including hours of useful lecture videos and downloadable exercises (with solutions).
* [A Crash Course in Python for Scientists](http://nbviewer.ipython.org/gist/rpmuller/5920182): Read through the Overview section for a quick introduction to Python.
* [Python for Informatics](http://www.pythonlearn.com/book.php): A very beginner-oriented book, with associated [slides](https://drive.google.com/folderview?id=0B7X1ycQalUnyal9yeUx3VW81VDg&usp=sharing) and [videos](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj4JXIwMwN1_ss1Tk8wZShEJ).
* [Python Tutor](http://pythontutor.com/): Allows you to visualize the execution of Python code.
* [My code isn't working](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/624506_orig.png) is a great flowchart explaining how to debug Python errors.
* [PEP 8](https://www.python.org/dev/peps/pep-0008/) is Python's "classic" style guide, and is worth a read if you want to write readable code that is consistent with the rest of the Python community.

**Advanced Python Material:**
* [Want to understand Python's comprehensions? Think in Excel or SQL](http://blog.lerner.co.il/want-to-understand-pythons-comprehensions-think-like-an-accountant/) may be helpful if you are still confused by list comprehensions.
* If you want to understand Python at a deeper level: Ned Batchelder's [Loop Like A Native](http://nedbatchelder.com/text/iter.html), [Python Names and Values](http://nedbatchelder.com/text/names1.html), 
Raymond Hettinger's [Transforming Code into Beautiful, Idiomatic Python](https://www.youtube.com/watch?v=OSGv2VnC0go) and [Python Epiphanies](https://www.youtube.com/watch?v=Pi9NpxAvYSs) are excellent presentations.
* [Everything is an object in Python](https://www.jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/)

**Resources:**
* For a useful look at the different types of data scientists, read [Analyzing the Analyzers](http://cdn.oreillystatic.com/oreilly/radarreport/0636920029014/Analyzing_the_Analyzers.pdf) (32 pages).
* For some thoughts on what it's like to be a data scientist, read these short posts from [Win-Vector](http://www.win-vector.com/blog/2012/09/on-being-a-data-scientist/) and [Datascope Analytics](http://datascopeanalytics.com/what-we-think/2014/07/31/six-qualities-of-a-great-data-scientist).
* [Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) 
* [Data Science vs Statistics](http://bit.ly/1FrZX80)
* [15 Books every Data Scientist Should Read](http://bit.ly/1Fs0bvW)
* [50+ Free Data Science Books](http://bit.ly/1Fs0kzr)
* [Building Data Science Teams](http://oreil.ly/1G1s6Oc)
* [Doing Data Science](http://amzn.to/1MHM1Jz)
* [Getting Started with Data Science](http://treycausey.com/getting_started.html)
* Quora has a [data science topic FAQ](https://www.quora.com/Data-Science) with lots of interesting Q&A.
* Keep up with local data-related events through the Data Community DC [event calendar](http://www.datacommunitydc.org/calendar) or [weekly newsletter](http://www.datacommunitydc.org/newsletter).
* [Stack Overflow - Developer Survey Results 2017](http://stackoverflow.com/insights/survey/2017/?utm_source=so-owned&utm_medium=hero&utm_campaign=dev-survey-2017&utm_content=hero-ind-ques)
* [Nate Silver on the Art and Science of Prediction](https://www.youtube.com/watch?v=eE4qCJBgfIk&index=22&list=LLGUFXF_Wex-mp-gpXFPYZEQ)
* [Three waves of AI](https://www.youtube.com/watch?v=-O01G3tSYpU)

**Material for Next Class:**
* [Setting up Python for machine learning: scikit-learn and IPython Notebook](https://youtu.be/IsXXlYVBt1M?t=4m57s) This videos includes an overview of Jupyter Notebook, which is used in the homework assignment.
* [Pro Git](http://git-scm.com/book/en/v2) is an excellent book for learning Git. Read the first two chapters to gain a deeper understanding of version control and basic commands.
* Work through GA's friendly [command line tutorial](http://generalassembly.github.io/prework/command-line/#/) using Terminal (Linux/Mac) or Git Bash (Windows), and then browse through this [command line reference](code/03_command_line.md).


---

### Class 2:

**Class Resources:**
Set your [Git username and email](https://help.github.com/articles/setting-your-username-in-git/)

**Command Line Resources:**
* Work through GA's friendly [command line tutorial](http://generalassembly.github.io/prework/command-line/#/) using Terminal (Linux/Mac) or Git Bash (Windows), and then browse through this [command line reference](code/03_command_line.md).
* [The Linux command line](http://courseweb.pitt.edu/bbcswebdav/institution/Pitt%20Online/MLIS_Pitt_Online/LIS%202600/Intro%20Module/LIS_2600_%20M1_Shotts%202009.pdf)
* If you want to go much deeper into the command line, [Data Science at the Command Line](http://amzn.to/1gSjcvV) is a great book. 
The [companion website](http://datascienceatthecommandline.com/) provides installation instructions for a "data science toolbox" 
(a virtual machine with many more command line tools), as well as a long reference guide to popular command line tools.
* If you want to do more at the command line with CSV files, try out [csvkit](http://csvkit.readthedocs.org/), which can be installed via `pip`.

**Git and Markdown Resources:**
* [Pro Git](http://git-scm.com/book/en/v2) is an excellent book for learning Git. Read the first two chapters to gain a deeper understanding of version control and basic commands.
* [GitHub for Beginners](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1)
* If you want to practice a lot of Git (and learn many more commands), [Git Immersion](http://gitimmersion.com/) looks promising.
* If you want to understand how to contribute on GitHub, you first have to understand [forks and pull requests](http://www.dataschool.io/simple-guide-to-forks-in-github-and-git/).
* [GitRef](http://gitref.org/) is my favorite reference guide for Git commands, and [Git quick reference for beginners](http://www.dataschool.io/git-quick-reference-for-beginners/) is a shorter guide with commands grouped by workflow.
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provides a thorough set of Markdown examples with concise explanations. GitHub's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) is a simpler and more attractive guide, but is less comprehensive.
* [Introducing GitHub](http://amzn.to/1KCjWg6) is a nice intro to GitHub that reads quickly
* [Version Control with Git](http://amzn.to/1gSkBm2)
* [Cracking the Code to GitHub's Growth](https://growthhackers.com/growth-studies/github) explains why GitHub is so popular among developers.
* [How to remove .DS_Store from GitHub](https://gist.github.com/vybstat/1680bef4715bfbcb0268)


**Machine Learning Resources:**
* For a very quick summary of the key points about machine learning, watch [What is machine learning, and how does it work?](https://www.youtube.com/watch?v=elojMnjn4kk) (10 minutes) or read the associated [notebook](http://nbviewer.ipython.org/github/justmarkham/scikit-learn-videos/blob/master/01_machine_learning_intro.ipynb).
* For a more in-depth introduction to machine learning, read section 2.1 (14 pages) of Hastie and Tibshirani's excellent book, [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/). (It's a free PDF download!)
* For a really nice comparison of supervised versus unsupervised learning, plus an introduction to reinforcement learning, watch this [video](http://work.caltech.edu/library/014.html) (13 minutes) from Caltech's [Learning From Data](http://work.caltech.edu/telecourse.html) course.
* For a preview of some of the machine learning content we will cover during the course, read Sebastian Raschka's [overview of the supervised learning process](https://github.com/rasbt/pattern_classification/blob/master/machine_learning/supervised_intro/introduction_to_supervised_machine_learning.md).

----
### Git Repo setup
#### Step 1
Fork the Class repo:
![Step 1](https://github.com/ga-students/ds-dc-19/blob/master/resources/git_step1.png?raw=true)
#### Step 2
Copy the link from your new Forked Repo
![Step 2](https://github.com/ga-students/ds-dc-19/blob/master/resources/git_step2.png?raw=true)
#### Step 3
Clone your new forked repo to your computer.
'''git clone git@github.com:YOUR_USERNAME/ds-dc-19.git'''
#### Step 4
cd (change directory) into the cloned repo.
#### Step 5
'''git remote add upstream https://github.com/ga-students/ds-dc-19'''
#### Step 6
Repeat this step often to keep your Repo up to date with the Class Repo:
    git pull upstream master


-----

### Class 3:

**Class Resources:**
* APIs ([code](code/07_api.py))
    * [OMDb API](http://www.omdbapi.com/)
* Web scraping ([code](code/07_web_scraping.py))
    * [IMDb: robots.txt](http://www.imdb.com/robots.txt)
    * [Example web page](dataset/example.html)
    * [IMDb: The Shawshank Redemption](http://www.imdb.com/title/tt0111161/)

**Statistics Resources:**
* Read [How Software in Half of NYC Cabs Generates $5.2 Million a Year in Extra Tips](http://iquantny.tumblr.com/post/107245431809/how-software-in-half-of-nyc-cabs-generates-5-2) for an excellent example of exploratory data analysis.
* Read [Anscombe's Quartet, and Why Summary Statistics Don't Tell the Whole Story](http://data.heapanalytics.com/anscombes-quartet-and-why-summary-statistics-dont-tell-the-whole-story/) for a classic example of why visualization is useful.
* [What I do when I get a new data set as told through tweets](http://simplystatistics.org/2014/06/13/what-i-do-when-i-get-a-new-data-set-as-told-through-tweets/) is a fun (yet enlightening) look at the process of exploratory data analysis.

**Web Scraping Resources:**
* The [Beautiful Soup documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) is incredibly thorough, but is hard to use as a reference guide. However, the section on [specifying a parser](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#specifying-the-parser-to-use) may be helpful if Beautiful Soup appears to be parsing a page incorrectly.
* For more Beautiful Soup examples and tutorials, see [Web Scraping 101 with Python](http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/), this [notebook](http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html) from Stanford's Text As Data course, and this [notebook](http://nbviewer.ipython.org/github/cs109/2014/blob/master/lectures/2014_09_23-lecture/data_scraping_transcript.ipynb) and associated [video](http://cm.dce.harvard.edu/2015/01/14328/L07/screen_H264LargeTalkingHead-16x9.shtml) from Harvard's Data Science course.
* For a much longer web scraping tutorial covering Beautiful Soup, lxml, XPath, and Selenium, watch [Web Scraping with Python](https://www.youtube.com/watch?v=p1iX0uxM1w8) (3 hours 23 minutes) from PyCon 2014. The [slides](https://docs.google.com/presentation/d/1uHM_esB13VuSf7O1ScGueisnrtu-6usGFD3fs4z5YCE/edit#slide=id.p) and [code](https://github.com/kjam/python-web-scraping-tutorial) are also available.
* For more complex web scraping projects, [Scrapy](http://scrapy.org/) is a popular application framework that works with Python. It has excellent [documentation](http://doc.scrapy.org/en/1.0/index.html), and here's a [tutorial](https://github.com/rdempsey/ddl-data-wrangling) with detailed slides and code.
* [robotstxt.org](http://www.robotstxt.org/robotstxt.html) has a concise explanation of how to write (and read) the `robots.txt` file.
* [import.io](https://import.io/) and [Kimono](https://www.kimonolabs.com/) claim to allow you to scrape websites without writing any code.
* [How a Math Genius Hacked OkCupid to Find True Love](http://www.wired.com/2014/01/how-to-hack-okcupid/all/) and [How Netflix Reverse Engineered Hollywood](http://www.theatlantic.com/technology/archive/2014/01/how-netflix-reverse-engineered-hollywood/282679/?single_page=true) are two fun examples of how web scraping has been used to build interesting datasets.
* [Be Suspicious Of Online Movie Ratings, Especially Fandango’s](https://fivethirtyeight.com/features/fandango-movies-ratings/) is a interesting example on the application of web scraping from FiveThirtyEight

**API Resources:**
* [Mashape](https://www.mashape.com/explore) and [Apigee](https://apigee.com/providers) allow you to explore tons of different APIs. Alternatively, a [Python API wrapper](http://www.pythonforbeginners.com/api/list-of-python-apis) is available for many popular APIs.
* [API Integration in Python](https://realpython.com/blog/python/api-integration-in-python/) provides a very readable introduction to REST APIs.
* Microsoft's [Face Detection API](https://www.projectoxford.ai/demo/face#detection), which powers [How-Old.net](http://how-old.net/), is a great example of how a machine learning API can be leveraged to produce a compelling web application.

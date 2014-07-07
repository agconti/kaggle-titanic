###Kaggle-titanic
This is a tutorial in an IPython Notebook for the Kaggle competition, Titanic Machine Learning From Disaster. The goal of this repository is to provide an example of a competitive analysis for those interested in getting into the field of data analytics or using python for Kaggle's Data Science competitions .

Quick Start: [View](http://nbviewer.ipython.org/urls/raw.github.com/agconti/kaggle-titanic/master/Titanic.ipynb) a static version of the notebook in the comfort of your own web browser.

###Installation:

To run this notebook interactively:

1. Download this repository in a zip file by clicking on this [link](https://github.com/agconti/kaggle-titanic/archive/master.zip) or execute this from the terminal:
`git clone https://github.com/agconti/kaggle-titanic.git`
2. Install [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation).
3. Navigate to the directory where you unzipped or cloned the repo and create a virtual environment with `virturalenv env`.
4. Activate the environment with `source env/bin/activate`
5. Install the required dependencies with `pip install -r requirements.txt`.
6. Execute `ipython notebook` from the command line or terminal.
7. Click on `Titanic.ipynb` on the IPython Notebook dasboard and enjoy!
8. When you're done deactivate the virtual environment with `deactivate`.


####Dependencies:
* [NumPy](http://www.numpy.org/)
* [IPython](http://ipython.org/)
* [Pandas](http://pandas.pydata.org/)
* [SciKit-Learn](http://scikit-learn.org/stable/)
* [SciPy](http://www.scipy.org/)
* [StatsModels](http://statsmodels.sourceforge.net/)
* [Patsy](http://patsy.readthedocs.org/en/latest/)
* [Matplotlib](http://matplotlib.org/)


###Kaggle Competition | Titanic Machine Learning from Disaster

>The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew.  This sensational tragedy shocked the international community and led to better safety regulations for ships.

>One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew.  Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.

>In this contest, we ask you to complete the analysis of what sorts of people were likely to survive.  In particular, we ask you to apply the tools of machine learning to predict which passengers survived the tragedy.

>This Kaggle Getting Started Competition provides an ideal starting place for people who may not have a lot of experience in data science and machine learning."

From the competition [homepage](http://www.kaggle.com/c/titanic-gettingStarted).

###Goal for this Notebook:
Show a simple example of an analysis of the Titanic disaster in Python using a full complement of PyData utilities. This is aimed for those looking to get into the field or those who are already in the field and looking to see an example of an analysis done with Python.

####This Notebook will show basic examples of:
####Data Handling
*   Importing Data with Pandas
*   Cleaning Data
*   Exploring Data through Visualizations with Matplotlib

####Data Analysis
*    Supervised Machine learning Techniques:
    +   Logit Regression Model
    +   Plotting results
    +   Support Vector Machine (SVM) using 3 kernels
    +   Basic Random Forest
    +   Plotting results

####Valuation of the Analysis
*   K-folds cross validation to valuate results locally
*   Output the results from the IPython Notebook to Kaggle


###Benchmark Scripts
To find the basic scripts for the competition benchmarks look in the "Python Examples" folder. These scripts are based on the originals provided by Astro Dave but have been reworked so that they are easier to understand for new comers.

Competition Website: http://www.kaggle.com/c/titanic-gettingStarted

import pandas as pd
import numpy as np
import math
import sklearn.datasets
import ipywidgets as widgets
from scipy import stats



##Seaborn for fancy plots. 
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = (8,8)

class edaDF:
    """
    A class used to perform common EDA tasks

    ...

    Attributes
    ----------
    data : dataframe
        a dataframe on which the EDA will be performed
    target : str
        the name of the target column
    cat : list
        a list of the names of the categorical columns
    num : list
        a list of the names of the numerical columns

    Methods
    -------
    setCat(catList)
        sets the cat variable listing the categorical column names to the list provided in the argument catList
        
        Parameters
        ----------
        catlist : list
            The list of column names that are categorical

    setNum(numList)
        sets the cat variable listing the categorical column names to the list provided in the argument catList
        
        Parameters
        ----------
        numlist : list
            The list of column names that are numerical

    countPlots(self, splitTarg=False, show=True)
        generates countplots for the categorical variables in the dataset 

        Parameters
        ----------
        splitTarg : bool
            If true, use the hue function in the countplot to split the data by the target value
        show : bool
            If true, display the graphs when the function is called. Otherwise the figure is returned.
    
    histPlots(self, splitTarg=False, show=True)
        generates countplots for the categorical variables in the dataset 

        Parameters
        ----------
        splitTarg : bool
            If true, use the hue function in the countplot to split the data by the target value
        show : bool
            If true, display the graphs when the function is called. Otherwise the figure is returned. 

    fullEDA()
        Displays the full EDA process. 
    """
    def __init__(self, data, target):
        self.data = data
        self.target = target
        self.cat = []
        self.num = []

    def info(self):
        return self.data.info()

    def giveTarget(self):
        return self.target
        
    def setCat(self, catList):
        self.cat = catList
    
    def setNum(self, numList):
        self.num = numList

    def countPlots(self, splitTarg=False, show=True):
        n = len(self.cat)
        cols = 2
        figure, ax = plt.subplots(math.ceil(n/cols), cols)
        r = 0
        c = 0
        for col in self.cat:
            if splitTarg == False:
                sns.countplot(data=self.data, x=col, ax=ax[r][c])
            if splitTarg == True:
                sns.countplot(data=self.data, x=col, hue=self.target, ax=ax[r][c])
            c += 1
            if c == cols:
                r += 1
                c = 0
        if show == True:
            figure.show()
        return figure

    def histPlots(self, kde=True, splitTarg=False, show=True):
        n = len(self.num)
        cols = 2
        figure, ax = plt.subplots(math.ceil(n/cols), cols)
        r = 0
        c = 0
        for col in self.num:
            #print("r:",r,"c:",c)
            if splitTarg == False:
                sns.histplot(data=self.data, x=col, kde=kde, ax=ax[r][c])
            if splitTarg == True:
                sns.histplot(data=self.data, x=col, hue=self.target, kde=kde, ax=ax[r][c])
            c += 1
            if c == cols:
                r += 1
                c = 0
        if show == True:
            figure.show()
        return figure

    def statistics(self):
        return self.data.describe()
    
    def outliers(self):
        threshold=3
        columns= self.data.select_dtypes(include=['int','float']).columns
        for column in columns:
            z_score= np.abs(stats.zscore(self.data[column]))
            outlier = np.where(z_score> threshold)
            print (outlier)
    def boxplot(self):
        return self.data.boxplot(grid= False, rot= 45, fontsize =15)
    

    def valuecounts(self):
        for column in self.cat:
            print (self.data[column].value_counts())
            print('\n')

    def missing(self):
        return self.data.isnull().sum()

    def pairplot(self):
        return sns.pairplot(self.data)

    def heatmap(self):
        corr = self.data.corr()
        heatmap= sns.heatmap(corr, annot= True)
        return heatmap
    
  



    def fullEDA(self):
        out1 = widgets.Output()
        out2 = widgets.Output()
        out3 = widgets.Output()
        out4 = widgets.Output()
        out5 = widgets.Output()
        out6 = widgets.Output()
        out7 = widgets.Output()
        out8 = widgets.Output()
        out9 = widgets.Output()
        out10 = widgets.Output()
        

        tab = widgets.Tab(children = [out1, out2, out3,out4,out5,out6,out7,out8,out9,out10])
        tab.set_title(0, 'Info')
        tab.set_title(1, 'Categorical')
        tab.set_title(2, 'Numerical')
        tab.set_title(3, 'Basic stats')
        tab.set_title(4, 'Outliers')
        tab.set_title(5, 'Boxplot')
        tab.set_title(6, 'Value Counts')
        tab.set_title(7, 'Missing values')
        tab.set_title(8, 'Pairplot')
        tab.set_title(9, 'Heatmap')

        display(tab)

        with out1:
            self.info()


        with out2:
            fig2 = self.countPlots(splitTarg=True, show=False)
            plt.show(fig2)
        
        with out3:
            fig3 = self.histPlots(kde=True, show=False)
            plt.show(fig3)

    

        with out4:
            print(self.statistics())
        
        with out5:
            print(self.outliers())

        with out6:
            fig7= self.boxplot()
            plt.show(fig7)
        
        with out7:
            print(self.valuecounts())
        
        with out8:
            print(self.missing())
        
        with out9:
            fig9= self.pairplot()
            plt.show(fig9)

        with out10:
            fig10 = self.heatmap()
            plt.show(fig10)

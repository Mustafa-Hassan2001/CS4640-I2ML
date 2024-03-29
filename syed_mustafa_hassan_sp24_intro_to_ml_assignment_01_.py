# -*- coding: utf-8 -*-
"""SYED MUSTAFA HASSAN - SP24 - Intro to ML - Assignment 01 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15gsUQpiyq1jreVcQqD-HLdumltL-3OYi

#Problem Introduction
This exercise relates to the College data set, which can be found in
the file College.csv on the book website. It contains a number of
variables for 777 different universities and colleges in the US. The
variables are
* Private : Public/private indicator
* Apps : Number of applications received
* Accept : Number of applicants accepted
* Enroll : Number of new students enrolled
* Top10perc : New students from top 10 % of high school class
* Top25perc : New students from top 25 % of high school class
* F.Undergrad : Number of full-time undergraduates
* P.Undergrad : Number of part-time undergraduates
* Outstate : Out-of-state tuition
* Room.Board : Room and board costs
* Books : Estimated book costs
* Personal : Estimated personal spending
* PhD : Percent of faculty with Ph.D.s
* Terminal : Percent of faculty with terminal degree
* S.F.Ratio : Student/faculty ratio
* perc.alumni : Percent of alumni who donate
* Expend : Instructional expenditure per student
* Grad.Rate : Graduation rate

Before reading the data into Python, it can be viewed in Excel or a
text editor.


---

**Q.1**
Use the pd.read_csv() function to read the data into Python. Call
the loaded data college. Make sure that you have the directory
set to the correct location for the data
"""

import numpy as np
import pandas as pd

Auto = pd.read_csv('College.csv')
Auto

"""**Q.2**
Look at the data used in the notebook by creating and running
a new cell with just the code college in it. You should notice
that the first column is just the name of each university in a
column named something like Unnamed: 0. We don’t really want
pandas to treat this as data. However, it may be handy to have
these names for later. Try the following commands and similarly
look at the resulting data frames:



```
college2 = pd.read_csv('College.csv', index_col=0)
college3 = college.rename({'Unnamed: 0': 'College'},
axis=1)
college3 = college3.set_index('College')
```



This has used the first column in the file as an index for the
data frame. This means that pandas has given each row a name
corresponding to the appropriate university. Now you should see
that the first data column is Private. Note that the names of
the colleges appear on the left of the table. We also introduced
a new python object above: a dictionary, which is specified by
(key, value) pairs. Keep your modified version of the data with
the following:


```
college = college3
```



"""

# college2 = pd.read_csv('College.csv', index_col=0)
# college3 = college.rename({'Unnamed: 0': 'College'},
# axis=1)
# college3 = college3.set_index('College')

college2 = pd.read_csv('College.csv', index_col=0)

college2.index.name = 'College'

college = college2

college

"""**Q.3**
Use the describe() method of to produce a numerical summary
of the variables in the data set.
"""

datasummary = college.describe()

datasummary

"""**Q.4**
Use the pd.plotting.scatter_matrix() function to produce a
scatterplot matrix of the first columns [Top10perc, Apps, Enroll].
Recall that you can reference a list C of columns of a data frame
A using A[C].
"""

import matplotlib.pyplot as plt

pd.plotting.scatter_matrix(college[['Top10perc', 'Apps', 'Enroll']])
plt.show()

"""**Q.5**
Use the boxplot() method of college to produce side-by-side
boxplots of Outstate versus Private.
"""

college.boxplot(column='Outstate', by='Private')
plt.show()

"""**Q.6**
Create a new qualitative variable, called Elite, by binning the
Top10perc variable into two groups based on whether or not the
proportion of students coming from the top 10% of their high
school classes exceeds 50%.


```
college['Elite'] = pd.cut(college['Top10perc'],
[0,0.5,1],
labels=['No', 'Yes'])
```
Use the value_counts() method of college['Elite'] to see how
many elite universities there are. Finally, use the boxplot() method
again to produce side-by-side boxplots of Outstate versus Elite.

"""

college['Elite'] = pd.cut(college['Top10perc'], [0, 50, 100], labels=['No', 'Yes'])
elite_counts = college['Elite'].value_counts()
elite_boxplot = college.boxplot(column='Outstate', by='Elite')

plt.show()

"""**Q.7**
Use the plot.hist() method of college to produce some histograms with differing numbers of bins for a few of the quantitative variables. The command plt.subplots(2, 2) may be useful: it will divide the plot window into four regions so that four
plots can be made simultaneously. By changing the arguments
you can divide the screen up in other combinations.
"""

fig, axes = plt.subplots(2, 2)
college['Apps'].plot.hist(ax=axes[0,0], bins=10)
college['Accept'].plot.hist(ax=axes[0,1], bins=20)
college['Enroll'].plot.hist(ax=axes[1,0], bins=15)
college['Top10perc'].plot.hist(ax=axes[1,1], bins=5)
plt.show()
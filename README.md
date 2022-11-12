# NaivePy

![Read the Docs](https://img.shields.io/readthedocs/naivepy) &nbsp;
![GitHub](https://img.shields.io/github/license/prathameshdhande22/Naivepy?color=blue&style=flat-square) &nbsp;
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/naivepy?color=red&style=flat-square) &nbsp;
![PyPI - Status](https://img.shields.io/pypi/status/naivepy?color=brown&style=flat-square)
&nbsp;
![PyPI - Format](https://img.shields.io/pypi/format/naivepy?color=blueviolet&style=flat-square) &nbsp;
![GitHub last commit](https://img.shields.io/github/last-commit/prathameshdhande22/naivepy?color=success&style=flat-square)
&nbsp;
![GitHub Release Date](https://img.shields.io/github/release-date/prathameshdhande22/naivepy?color=blue&style=flat-square)
&nbsp;
![GitHub Repo stars](https://img.shields.io/github/stars/prathameshdhande22/naivepy?style=social)
</br>

![GitHub Repo stars](https://img.shields.io/badge/Made_with-Python-blue?style=for-the-badge)

</br>

# Naive Bayes :
## About Naive Bayes :
<p align="Justify">
Naïve Bayes algorithm is a supervised learning algorithm, which is based on Bayes theorem and used for solving classification problems.</br>
It is mainly used in text classification that includes a high-dimensional training dataset.</br>
Naïve Bayes Classifier is one of the simple and most effective Classification algorithms which helps in building the fast machine learning models that can make quick predictions.</br>
It is a probabilistic classifier, which means it predicts on the basis of the probability of an object.</br>
Some popular examples of Naïve Bayes Algorithm are spam filtration, Sentimental analysis, and classifying articles.
</p>

## Formula Of Naive Bayes :
<p align="justify">
Bayes' theorem is also known as Bayes' Rule or Bayes' law, which is used to determine the probability of a hypothesis with prior knowledge. It depends on the conditional probability.
The formula for Bayes' theorem is given as:
Naïve Bayes Classifier Algorithm
Where,

**$P(A|B)$ = ${P(B|A)P(A)} \over P(B)$**

P(A|B) is Posterior probability: Probability of hypothesis A on the observed event B.

P(B|A) is Likelihood probability: Probability of the evidence given that the probability of a hypothesis is true.

P(A) is Prior Probability: Probability of hypothesis before observing the evidence.

P(B) is Marginal Probability: Probability of Evidence.
</p>

# Documentation:
Read the [Docs Here](https://naivepy.readthedocs.io/en/latest/#)

# Installation :
To Install the module
```
pip install naivepy
```

# About Module:
<p align="justify">
Naivepy module is built using python and pandas. It is and machine learning algorithm. This Module can take the target column and classifies it.

**Note** : The Target Column must have 2 Types of values other wise MaxTargetColumnException will be occured.

# Examples :

**Code** :
```
from naivepy import Naive
a = Naive()
data = a.load("2data.csv")
print(data)
print(a.classify(["Red", "SUV", "Domestic"],"Stolen"))
print(a.getans)
```

**Output** :
```
        Color    Type    Origin Stolen
   0     Red  Sports  Domestic    Yes
   1     Red  Sports  Domestic     No
   2     Red  Sports  Domestic    Yes
   3  Yellow  Sports  Domestic     No
   4  Yellow  Sports  Imported    Yes
   5  Yellow     SUV  Imported     No
   6  Yellow     SUV  Imported    Yes
   7  Yellow     SUV  Domestic     No
   8     Red     SUV  Imported     No
   9     Red  Sports  Imported    Yes
   No
   0.072
```

<h3>If you have any issue regarding the code or module you can contact me <a href="mailto:prathameshdhande534@gmail.com">My Mail Id</a></h3>
</br>

# Author : Prathamesh Dhande

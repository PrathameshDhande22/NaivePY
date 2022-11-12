import pandas as pd
from .exceptions import *


class Naive:
    """Naive Bayes Algorithm which can take only two values from a targeted column label
"""

    def load(self, filename: str):
        """Loads the File to classify the model.

        Args:
            filename (str): filename should be in the csv format

        Raises:
            FormatNotSupported: Exception if the filename is not in .csv format

        Returns:
            dataframe: returns filename.csv file loaded in pandas dataframe.
        """
        self.__filename = filename
        try:
            if not self.__filename.endswith(".csv"):
                raise FormatNotSupported(self.__filename)
            else:
                self.__data = pd.read_csv(filename)
                return self.__data
        except FileNotFoundError:
            raise FormatNotSupported(self.__filename)

    def __cal_prob(self, target: str):
        if target not in self.__data.columns:
            raise WrongTargetColumnException(self.__filename)
        pc1 = self.__data.value_counts(subset=target)
        if len(pc1) > 2:
            raise MaxTargetValueException(len(pc1))
        total = self.__data[target].count()
        return pc1[0]/total, pc1[1]/total, pc1[0], pc1[1]

    def classify(self, sample: list, target_column: str):
        """Classifies the model from the loaded file.

        But make sure that the targeted column must be in the last column of the dataset.csv

        Args:
            sample (list): List of the values to compare
            target_column (str): targeted column from the filename.csv

        Returns:
            Str : returns the label from the targeted column 
        """
        pc1, pc2, c1, c2 = self.__cal_prob(target_column)
        ansc1, ansc2 = self.__calculate(sample, target_column, [c1, c2])
        if ansc1*pc1 < ansc2*pc2:
            self.__ans = ansc2*pc2
            return self.__target_values[1]
        else:
            self.__ans = ansc1*pc1
            return self.__target_values[0]

    def __calculate(self, sample: list, target_column: str, classvalues: list):
        ansc1 = 1
        ansc2 = 1
        self.__target_values = self.__data[target_column].value_counts(
        ).index.to_list()
        for i in range(2):
            for j in range(len(sample)):
                newdata = self.__data.loc[self.__data[self.__data.columns[j]] == sample[j]
                                          ].loc[self.__data[target_column] == self.__target_values[i]].count(axis=1).count()
                self.__verify(
                    sample[j], self.__data[self.__data.columns[j]].tolist())
                if i == 0:
                    ansc1 = ansc1*(newdata/classvalues[i])
                elif i == 1:
                    ansc2 = ansc2*(newdata/classvalues[i])
        return ansc1, ansc2

    @property
    def getans(self):
        """Returns the ans of the classified model

        Returns:
            float : returns the ans of the model.
        """
        return self.__ans

    def __verify(self, compare1, compare2):
        if compare1 not in compare2:
            raise ValueNotFoundException(self.__filename, compare1)

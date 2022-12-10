import pandas as pd
from .exceptions import *


class Naive:
    """Naive Bayes Algorithm which can take only two values from a targeted column label

        Parameters:
        filename : name of the file must be in csv format
        sample_list : list of tuples want to compare
        target_column : Target column is single only or comparing column
"""

    def __init__(self, filename: str, sample_list: list, target_column: str) -> None:
        self.__filename = filename
        self.__list = sample_list
        self.__target_c = target_column
        self.__return_data = self.__load(self.__filename)
        self.__returned_label = self.__classify(self.__list, self.__target_c)

    def __load(self, filename: str) -> pd.DataFrame:
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

    def __classify(self, sample: list, target_column: str) -> str:
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
    def getans(self) -> float:
        """Returns the ans of the classified model

        Returns:
            float : returns the ans of the model.
        """
        return self.__ans

    def __verify(self, compare1, compare2):
        if compare1 not in compare2:
            raise ValueNotFoundException(self.__filename, compare1)

    @property
    def getdata(self)->pd.DataFrame:
        """Returns the Loaded filename data.

        Returns:
            Dataframe : Return data in pandas.dataframe.
        """
        return self.__return_data

    @property
    def getlabel(self)-> str:
        """Returns classified Label after comparing.

        Returns:
            str : Returns Label in String.
        """
        return self.__returned_label

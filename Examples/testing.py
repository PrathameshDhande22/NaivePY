from naivepy import Naive

n=Naive(filename="data.csv",sample_list=["red","suv","domestic"],target_column="stolen")
print(n.getans)
print(n.getdata)
print(n.getlabel)
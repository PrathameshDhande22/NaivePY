

.. toctree::
   :maxdepth: 3



Examples 
==============
Here Contains some examples of my code

Example 1:
~~~~~~~~~~~~
::

   from naivepy import Naive

   n=Naive(filename="data.csv",sample_list=["red","suv","domestic"],target_column="stolen")
   print(n.getans)
   print(n.getlabel)
   print(n.getdata)

**Output** :
::

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


Steps to Train the model
========================
1. import the module
::

   from naivepy import Naive

2. create the Object Instance of the Naive class and the parameters to it
::

   n=Naive(filename="data.csv",sample_list=["red","suv","domestic"],target_column="stolen")

3. Get The Data in Pandas Dataframe
::

   print(n.getdata)

4. Get the label after Classifying
::

   print(n.getlabel)

5. Get the Ans of the target Column 
::
   
   print(n.getans)


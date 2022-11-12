

.. toctree::
   :maxdepth: 3



Examples 
==============
Here Contains some examples of my code

Example 1:
~~~~~~~~~~~~
::

   from naivepy import Naive
   a = Naive()
   data = a.load("2data.csv")
   print(data)
   print(a.classify(["Red", "SUV", "Domestic"], "Stolen"))
   print(a.getans)

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

Example 2:
~~~~~~~~~~~
::

   from naivepy import Naive

   a=Naive()
   data=a.load("data.csv")
   print(data)
   print(a.classify(['Sunny','Hot','High',False],'Play Golf'))
   print(a.getans)

**Output** :
::

   Outlook Temperature Humidity  Windy Play Golf
   0      Rainy         Hot     High  False        No
   1      Rainy         Hot     High   True        No
   2   Overcast         Hot     High  False       Yes
   3      Sunny        Mild     High  False       Yes
   4      Sunny        Cool   Normal  False       Yes
   5      Sunny        Cool   Normal   True        No
   6   Overcast        Cool   Normal   True       Yes
   7      Rainy        Mild     High  False        No
   8      Rainy        Cool   Normal  False       Yes
   9      Sunny        Mild   Normal  False       Yes
   10     Rainy        Mild   Normal   True       Yes
   11  Overcast        Mild     High   True       Yes
   12  Overcast         Hot   Normal  False       Yes
   13     Sunny        Mild     High   True        No
   No
   0.01828571428571429 

Steps to Train the model
========================
1. import the module
::

   from naivepy import Naive

2. create the Object Instance of the Naive class

3. Load the dataset.csv
::
   
   obj=Naive()
   obj.load("filename.csv")

4. classify the model 
::

   obj.classify([samplelist],targetcolumn name)

5. Print the ans
::

   obj.getans


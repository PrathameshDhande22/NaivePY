from setuptools import setup

with open("README.md",'r') as f:
  LNG=f.read()

setup(name="naivepy",
version="0.7",
description="Naive Algorithm Module Implemented in Python",
author="Prathamesh Dhande",
author_email='prathameshdhande534@gmail.com',
long_description=LNG,
long_description_content_type='text/markdown',
packages=['naivepy'],
install_requires=['pandas'],
url="https://github.com/PrathameshDhande22/NaivePY",
keywords=['naive','naive bayes','algorithm','naive algorithm','classification','module'],
classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Education',   
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)', 
    'Natural Language :: English',  # Define that your audience are developers   # Again, pick a license   #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.10',
  ]

)
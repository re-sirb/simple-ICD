# simple-ICD

Simple-ICD is a simple Python-library without the bells and whistles for the encoding of diagnoses according to the 10th revision of the International Statistical Classification Of Diseases, German Modification (ICD-10-GM).
This Python-module emphasizes ease of use, giving clinicians and researchers an a simple tool to encode diagnoses.

## Using ICD_10.py

A quick example how to use the __ICD_10__ module.


```python
from ICD_10 import ICD_10 as icd

# search for "Humerusfraktur"
ret_list=icd.search_icd_intelligent("Humerus") 

print(ret_list)
```
The application example icd-example.py creates a simple user interface to search for ICD-10 codes using PySimpleGUI.


Have fun!

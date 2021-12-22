#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*-
import PySimpleGUI as sg   
from ICD_10 import ICD_10

icd=ICD_10() 

#ICD 10 suchen
#def lookup(input_t):
#    out_list=icd.search_icd_intelligent(str(input_t.strip()))
#    out_str=""
#    for i in out_list:
#        out_str=out_str+i[0]+" >> "+i[1]+"\n"
    
#Window
layout = [[sg.Text('Enter your search query:')],      
          [sg.Input()],      
          [sg.RButton('Search')],
          [sg.Listbox(values=('ICD-10',''), size=(100, 10), key='_OUTPUT_')],
          [sg.RButton('OK'), sg.Exit()]]      

window = sg.Window('ICD-10').Layout(layout)      

#Main-loop
while True:
	event, values=window.Read()
	if((event is None)or(event=='Exit')):
		break
	if(event == "Search"):
		#print(values[0])
		out_list=icd.search_icd_intelligent(str(values.get(0).strip()))
		window.FindElement('_OUTPUT_').Update(values=out_list)
	if(event == "OK"):
		print (values.get("_OUTPUT_"))
		
	#print(event, values)   
window.Close()

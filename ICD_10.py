# -*- coding: iso-8859-1 -*-
class ICD_10:
    icd_list=[]
        
    #intelligent search: search for every individual word without order
    def search_icd_intelligent(self, term):
        ret_list=[]
        b=term.lower()
        b_elements=b.split(" ")
        #print(b_elements)
        in_list=self.icd_list
        count_b_element=0
        for m in b_elements:
            if (count_b_element>0):
                in_list=ret_list
                ret_list=[]
                
            for n in in_list:
                temp_l=[]
                a=n[1].lower()
                a=a.replace(" ", "")
                if (a.find(m)>(-1)):
                    temp_l.append(n[0])
                    temp_l.append(n[1])
                    ret_list.append(temp_l)
                else:
                    continue
            count_b_element=count_b_element+1
            
        #return ret_list
        return sorted(ret_list, key=lambda ret: ret[1])
    
    #check for matches, return matches as list: icd-code, descr.
    def search_icd(self, term):
        ret_list=[]
        b=term.lower()
        b=b.replace(" ", "")
        for n in self.icd_list:
            temp_l=[]
            a=n[1].lower()
            a=a.replace(" ", "")
            if (a.find(b)>(-1)):
                temp_l.append(n[0])
                temp_l.append(n[1])
                ret_list.append(temp_l)
            else:
                continue
            
        #return ret_list
        return sorted(ret_list, key=lambda ret: ret[1])
        
    #load data from csv-file
    def init_data(self):
        exp_l=[]
        try:
			#insert the correct path to your csv-file and check if the seperator is correct.
            f = open("icd.csv")
            w=f.read()
        except:
            print("Database not found!") 
        finally:
            f.close()
            
        D = w.split("\n")
        for a in D:
            temp_l=[]
            b = a.split("|")
            if (b[0]==""):
                break
            
            if (int(b[0])==1):
                temp_l.append(b[3])
            elif (int(b[0])==2):
                temp_l.append(b[3]+" ; "+b[4])
            elif (int(b[0])==3):
                temp_l.append(b[3]+" ; "+b[5])
            elif (int(b[0])==4):
                temp_l.append(b[3]+" ; "+b[4]+" ; "+b[5])
            elif (int(b[0])==6):
                temp_l.append(b[3]+" ; "+b[6])
            else:
                continue
                
            temp_l.append(b[7])
            exp_l.append(temp_l)
            
        self.icd_list=exp_l

    # Initializing  
    def __init__(self): 
        self.init_data()

    # Calling destructor 
    def __del__(self): 
        #print("Destructor called") 
        pass

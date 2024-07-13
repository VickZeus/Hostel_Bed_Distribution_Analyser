import csv
class Analyser : 

    def analyse(self) :
        analyser.hostel_specific()
        
    def hostel_specific(self,i) : # Displays The total number of AC/NAC beds.
        ac,nac=0,0
        total_beds=0
        file=open("beds.csv","r")
        for k in csv.reader(file) :
            if k[0].split("\t")[1].split(" ")[-1].strip()=="NAC" and k[0].split("\t")[0]==i:
                nac+=int(k[0].split("\t")[6])
                total_beds+=int(k[0].split("\t")[6])
            elif  k[0].split("\t")[1].split(" ")[-1].strip()=="AC" and k[0].split("\t")[0]==i :
                ac+=int(k[0].split("\t")[6])
                total_beds+=int(k[0].split("\t")[6])
        print("Total NAC Beds in Hostel : ",nac)
        print("Total AC Beds in Hostel : ",ac)
        print("Total Beds --> ",total_beds)
        file.close()
        return total_beds


    def groupspecific(self,i) : # GroupSpecific Analaysis
        ac=nac=0
        grp=["Group4","Group3","Group2","Group1"]
        for d in grp :
            file=open("beds.csv","r")
            for k in csv.reader(file) :
                if k[0].split("\t")[1].split(" ")[-1].strip()=="NAC" and k[0].split("\t")[0]==i and k[0].split("\t")[-1]==d:
                    nac+=int(k[0].split("\t")[6])
                elif k[0].split("\t")[1].split(" ")[-1].strip()=="AC" and k[0].split("\t")[0]==i and k[0].split("\t")[-1]==d:
                    ac+=int(k[0].split("\t")[6])
            print("Total NAC Beds in Hostel for {0}: ".format(d),nac)
            print("Total AC Beds in Hostel for {0}: ".format(d),ac)
            print()
            analyser.bed_type_specific(i,d)
            file.seek(0)
            nac=ac=0
        file.close()

    
    def bed_type_specific(self,i,d) : # i--> hostel , d--> Group
        bed=["8 - NAC-DORMS","12 - AC-DORMS","2 - NAC-ROOM","5 - NAC-ROOM","10 - NAC-DORMS","6 - NAC-DORMS","12 - NAC-DORMS","5 - NAC-APT","4 - NAC-ROOM","8 - AC-DORMS","5 - AC-APT","5 - AC-ROOM","2 - AC-ROOM","15 - NAC-DORMS"]
        for b in bed :
            count=0
            tc=0
            file=open("beds.csv","r")
            for k in csv.reader(file) :
                if k[0].split("\t")[4].strip()==b and k[0].split("\t")[0]==i and k[0].split("\t")[-1]==d:
                    count+=1
                    tc+=int(k[0].split("\t")[6])
            print("{0} Type for {1} in {3} => {2} , Total Bed Count ==>{4} ".format(b,d,count,i,tc))
        print()
                

    def bedtypes(self) :
        file=open("beds.csv","r")
        l=[]
        for k in csv.reader(file) :
                l.append(k[0].split("\t")[4].strip())
        for j in list(set(l)) :
            print(j)
            

    def MAIN(self) :
        total=0
        for i in ["MH4","MH3","MH5","MH2","MH1","CB"] :
            print("---{0} BED ANALYSIS---".format(i))
            print()
            total+=analyser.hostel_specific(i)
            print('\n')
            analyser.groupspecific(i)
            print()
            print()
        print("Total Beds --->",total)

analyser=Analyser()
analyser.MAIN()
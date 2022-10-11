import csv

class View:
    
    def displayReloadData(self,inMemoryData):
        for count, r in enumerate(inMemoryData):
            if((count+1) % 10 == 0):
                print("Practical Project2 by Jiwon Hwang")
            print(f"{count+1} item(s) displayed")
            print(f"source       | " + r.get_source())
            print(f"latin_name   | " + r.get_latin_name())
            print(f"english_name | " + r.get_english_name())
            print(f"french_name  | " + r.get_french_name())
            print(f"year         | " + r.get_year())
            print(f"month        | " + r.get_month())
            print(f"number       | " + r.get_number())
            print()
            
    def confirmCreateNewFile(self, newFileName):
        
        print(f'{newFileName} is created successfully with records.\n')
        
    def displayOneView(self, indexNumber, inMemory):
        print("Practical Project2 by Jiwon Hwang")
        print(f"** Index {indexNumber} record is displayed...")    
        print(f"source       | " + inMemory[indexNumber].get_source())
        print(f"latin_name   | " + inMemory[indexNumber].get_latin_name())
        print(f"english_name | " + inMemory[indexNumber].get_english_name())
        print(f"french_name  | " + inMemory[indexNumber].get_french_name())
        print(f"year         | " + inMemory[indexNumber].get_year())
        print(f"month        | " + inMemory[indexNumber].get_month())
        print(f"number       | " + inMemory[indexNumber].get_number())
        print()
        

            
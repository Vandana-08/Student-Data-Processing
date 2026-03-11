class student:
    def std(self,rollno,name,stream):
        self.rollno=rollno
        self.name=name
        self.stream=stream
        print('Student details')
        for i in range(len(rollno)):
            print("RollNo:",rollno[i],"Name:",name[i],"Stream:",stream[i])
            
        

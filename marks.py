class Marks:
    def mark(self, marks):
        self.marks = marks
        print("Marks")
        for i in range(len(self.marks)):
            print(self.marks[i])
    def cal(self):
        totals = []
        percentages = []
        for row in self.marks:
            total_i = sum(row)              
            perc_i = (total_i / 500) * 100  
            totals.append(total_i)
            percentages.append(perc_i)
        return totals, percentages

    def pass_fail(self, pass_mark=35):
        result = []
        for row in self.marks:
            status = "Pass" if all(m >= pass_mark for m in row) else "Fail"
            result.append(status)
        return result

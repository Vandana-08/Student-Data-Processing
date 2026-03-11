from Student_Data import student1, marks

def main():

    rollno = [101, 102, 103,104,105,106]
    name   = ["Anita", "Bharath", "Chaitra","Naimisha","Ramani","Maimunisa"]
    stream = ["CSE", "ECE", "EEE","CIVIL","ECE","IT"]

    marks_data = [
        [78, 85, 69, 90, 81],
        [92, 66, 74, 58, 77],
        [33, 71, 80, 40, 55],
        [35, 67, 30, 78, 56],
        [56, 87, 67, 90, 76],
        [37, 56, 45, 67, 55]
    ]

    Std = student1.student()
    Std.std(rollno, name, stream)

    mk = marks.Marks()
    mk.mark(marks_data)

    totals, percentages = mk.cal()
    results = mk.pass_fail(pass_mark=35)

    print("\nFinal Report")

    for i in range(len(rollno)):
        s1, s2, s3, s4, s5 = marks_data[i]

        print(f"RollNo: {rollno[i]:<5}  Name: {name[i]:<10}  Stream: {stream[i]}")
        print(f"  Marks: {s1}, {s2}, {s3}, {s4}, {s5}")
        print(f"  Total: {totals[i]} / 500")
        print(f"  Percentage: {percentages[i]:.2f}%")
        print(f"  Result: {results[i]}")
        print("-" * 70)

    # Writing to file
    file = open("student_data.txt", "w")

    for i in range(len(name)):
        file.write(name[i] + " " +
                   str(rollno[i]) + " " +
                   stream[i] + " " +
                   str(marks_data[i]) + " " +
                   str(totals[i]) + " " +
                   str(percentages[i]) + " " +
                   results[i] + "\n")

    file.close()

    # Reading from file
    file = open("student_data.txt", "r")
    data = file.read()

    print("\nStudent Data")
    print(data)

    file.close()


if __name__ == "__main__":
    main()

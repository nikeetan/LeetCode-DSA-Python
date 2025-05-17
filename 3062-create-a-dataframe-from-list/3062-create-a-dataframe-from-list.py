import pandas as pd
'''
Student_df = { "Student_id" : [ 1, 2, 3 ], "age" : [ 10, 20 , 30]}
0 -> Student_id
1 -> age
[1, 15]
'''
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    student_df = { "student_id" : [], "age" : []}
    for data in student_data:
       
        student_df["student_id"].append(data[0])
        student_df["age"].append(data[1])
    student_df = pd.DataFrame(student_df)
    return student_df
    
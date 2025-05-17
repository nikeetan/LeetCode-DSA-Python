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
        curr_std_id, curr_std_age = data
        student_df["student_id"].append(curr_std_id)
        student_df["age"].append(curr_std_age)
    student_df = pd.DataFrame(student_df)
    return student_df
    
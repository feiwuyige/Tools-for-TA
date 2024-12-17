import pandas as pd
import numpy as np
import os

# 标准答案
ground_truth_regression = pd.read_csv(r'C:\Users\QAQ\Desktop\huigui.csv')
ground_truth_classification = pd.read_csv(r'C:\Users\QAQ\Desktop\ans.csv')
student = pd.read_excel(r'C:\Users\QAQ\Desktop\project.xlsx')
student['id'] = student['id'].astype(str)


# 同学提交
main_folder = r'C:\Users\QAQ\Desktop\testDestinate'
for student_folder in os.listdir(main_folder):
    # 根据 student_id 作为关键字选择
    student_id = student_folder[-12 : ]
    if student_id == "202411081614":
        continue
    # print(student_id)
    student_path = os.path.join(main_folder, student_folder)
    for file in os.listdir(student_path):
        if "regression" in file:
            student_file = os.path.join(student_path, file)
            if file.endswith('.excel'):
                student_submission = pd.read_excel(student_file)
            elif file.endswith(".csv"):
                student_submission = pd.read_csv(student_file)
            score = np.mean((ground_truth_regression['y'] - student_submission['y']) ** 2)
            # 得到对应行
            row_index = student[student['id'] == student_id].index
            if not row_index.empty:
                student.loc[row_index, 'regression'] = score
student.to_excel(r'C:\Users\QAQ\Desktop\project_test.xlsx',index=False)
            
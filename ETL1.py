import pandas as pd

df1 = pd.read_csv(r"C:\Users\Admin\Desktop\data1.csv")
df2 = pd.read_csv(r"C:\Users\Admin\Desktop\data2.csv")


def count_validation(df1, df2):
    try:
        if df1.count() == df2.count():
            return "Pass"
        else:
            return "Fail"
    except Exception as e:
        return e


def Data_validation(df1, df2):
    try:
        if df1.sunstract(df2) == 0 and df2.sunstract(df1) == 0:
            return "Pass"
        else:
            return "Fail"
    except Exception as e:
        return e


def Test_case_1(df1, df2):
    if count_validation(df1, df2) == "Pass":
        return "Test_Case_1 is passed - Count is matching"
    else:
        return f"Test_case_1 is failed - Count mismatch, Df1 count:{df1.count()} and Df2 count:{df2.count()}"


def Test_case_2(df1, df2):
    if Data_validation(df1, df2) == "Pass":
        return "Test_case_2 is passed - Data is matching"
    else:
        return "Test_case_2 is failed"


Test_case_1(df1, df2)
Test_case_2(df1, df2)
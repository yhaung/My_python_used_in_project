import pandas as pd

dataframe = pd.read_csv(r"D:\Programming\Python_Summary_for_OMM\Jupyter_notebook\Jupiter_Lessons\Panda_Lesson_5\Kumpula_temps_above15_june_2016.csv")

dataframe.set_index("Name",inplace=True)
hey =dataframe.loc[['Ye Htet Aung_3']]

print(hey)

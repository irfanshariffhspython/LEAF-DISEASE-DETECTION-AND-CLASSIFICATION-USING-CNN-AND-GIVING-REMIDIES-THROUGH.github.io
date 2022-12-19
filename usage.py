import pandas as pd
import os

baseDir = os.path.join(os.getcwd(), 'detail_Leaf_Image_link')
file_name =(os.path.join(baseDir, 'tomato_project_details_with_usage.csv'))

#file =('C:\\Users\\User\\Desktop\\Flask_Projet_Phase3\\Flask_Projet\\Flask_Projet\\detail_Leaf_Image_link\\tomato_project_details_with_usage.xlsx')
newData = pd.read_csv(file_name)
print(newData.loc[2,'usage'])







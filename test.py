import pandas as pd
import csv
from zipfile import ZipFile

with ZipFile('C:/Users/melissa.goodhew/S1A_IW_GRDH_1SDV_20230227T093636_20230227T093701_047419_05B158_78D5.zip', 'r') as zip_object:
    print(zip_object.namelist())
    file_names = zip_object.namelist()
    
for file_name in file_names:
    if (file_name.endswith('.xml') or
        file_name.endswith('.png')):
        zip_object.extract(file_name)

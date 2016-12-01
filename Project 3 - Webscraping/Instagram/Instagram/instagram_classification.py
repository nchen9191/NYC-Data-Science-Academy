import classify_image as CI
import pandas as pd
from sys import argv

'''
Takes two numerical values as input from the system
Puts them through the tensorflow classifier
Returns pandas dataframe
Merge_flag indicates if it is the last index and should merge all files together
'''

###### System arguments #######
num1 = int(argv[1])
num2 = int(argv[2])
mergeFLAG = argv[3]

###### specifies username and directory #######
username = 'instagram'
dir_name = 'data/' + username + '/'

###### Runs the classification #######
temp = pd.read_csv('temp.csv')
temp2 = CI.run_inference_on_image(num1,num2)
temp = pd.concat([temp,temp2], ignore_index=True)
temp.to_csv('temp.csv', index = False)

###### Merges all data into one csv #######
if mergeFLAG == 'True':
    instagram = pd.read_csv(dir_name + username + '_complete.csv')
    instagram = pd.concat([instagram, temp], axis = 1)
    instagram.to_csv('instagram_temp.csv',index = False)

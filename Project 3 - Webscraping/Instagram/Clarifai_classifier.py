import pandas as pd
from clarifai.rest import ClarifaiApp
import collections

###### Read in data #######
instagram_data = pd.read_csv('data/instagram/instagram_total.csv')

###### Initiate Clarifai API #######
app = ClarifaiApp()
model = app.models.get('general-v1.3')

###### Pull URL of image into Clarifai API #######
data = []
for i in range(instagram_data.shape[0]):
    print i
    url = instagram_data.loc[i,'image_urls']
    temp = model.predict_by_url(url)
    data.append(temp)
    if i % 200 == 0:
        temp

###### Function to convert from unicode to string #######
def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

###### Convert data to string format#######
new_data = convert(data)

###### Store top 5 classification and probabilities #######
obj1 = map(lambda item: item['outputs'][0]['data']['concepts'][0]['name'], new_data)
prob1 = map(lambda item: item['outputs'][0]['data']['concepts'][0]['value'], new_data)
obj2 = map(lambda item: item['outputs'][0]['data']['concepts'][1]['name'], new_data)
prob2 = map(lambda item: item['outputs'][0]['data']['concepts'][1]['value'], new_data)
obj3 = map(lambda item: item['outputs'][0]['data']['concepts'][2]['name'], new_data)
prob3 = map(lambda item: item['outputs'][0]['data']['concepts'][2]['value'], new_data)
obj4 = map(lambda item: item['outputs'][0]['data']['concepts'][3]['name'], new_data)
prob4 = map(lambda item: item['outputs'][0]['data']['concepts'][3]['value'], new_data)
obj5 = map(lambda item: item['outputs'][0]['data']['concepts'][4]['name'], new_data)
prob5 = map(lambda item: item['outputs'][0]['data']['concepts'][4]['value'], new_data)

###### Save to csv #######
rows_dict = {'Object 1':obj1,'Object 2':obj2,'Object 3':obj3,'Object 4':obj4,'Object 5':obj5, \
            'Prob 1':prob1,'Prob 2':prob2,'Prob 3':prob3,'Prob 4':prob4,'Prob 5':prob5}
data_pd = pd.DataFrame(rows_dict, columns = ['Object 1','Object 2','Object 3','Object 4','Object 5',\
            'Prob 1','Prob 2','Prob 3','Prob 4','Prob 5'])
instagram_data = pd.concat([instagram_data, data_pd], axis=1)
instagram_data.to_csv('data/instagram/instagram_clarifai.csv', index=False)
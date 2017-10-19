import pandas as pd

df = pd.read_csv('xyz.csv')

print(df['Name'])


names = ['arvind', 'gayu','lilly']
total = [100,200,300]
data_set = list(zip(names,total))
data_frame = pd.DataFrame(data=data_set,columns=['Name', 'Total'])
data_frame.to_csv('points.csv', index = False, header= True)
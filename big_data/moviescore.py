import  pandas as pd

unames = ['uid','age','gender','occupation','zip']
users = pd.read_table('F:\\python\\big_data\\ml-100k\\u.user',sep='|',header=None,names=unames)
print(users.head(5))

rnames = ['uid','mid','rating','timestamp']
rating = pd.read_table('F:\\python\\big_data\\ml-100k\\u.data',sep='\t',header=None,names=rnames)
print(rating[:5])

frame = pd.merge(rating,users)
print(frame[0:5])
# 四舍五入将年龄分为年龄段（args=[-1]），和性别进行分组 计算平均分
print(frame['rating'].groupby([frame['age'].apply(round,args=[-1]),frame['gender']]).mean())

# 电影数据
mnames = ['mid','title','date1','date2','url','unknown','Action','Adventure','Animation',
          'Children','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror',
          'Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']
movies = pd.read_table('F:\\python\\big_data\\ml-100k\\u.item',sep='|',header=None,names=mnames)
print(movies[:5])
# 连接几个表
frame = pd.merge(frame,movies)
print(frame[:5])
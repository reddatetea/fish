import pandas as pd

(
    pd.read_excel('https://www.gairuo.com/file/data/dataset/team.xlsx')
    .groupby('team')
    .first()
    .assign(avg=lambda x: x.mean(1))
    .reset_index()
    .set_index('name')
    .query('avg>60')
    .loc[:,['team', 'avg']]
    .pipe(print)
)


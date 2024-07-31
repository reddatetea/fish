'''
pandas 多层汇总

'''


import pandas as pd
# from faker import Faker
import random

# 三层汇总
def Statistical_summary(df,a,b):
    '''作用：三层嵌套汇总
    参数说明
    a：要汇总的值字段,列表,如：["销售金额"，'销售数量']
    b：要汇总的维度,列表,如：「"销售地区"，"销售城市"，"销售商品"]'''
    df1=(
        df.pivot_table(values=a,aggfunc='sum',margins=True,margins_name='总计',index=b).reset_index()
        .groupby(b[0]).apply(lambda x:pd.pivot_table(x,index=b[1:],values=a,aggfunc='sum',margins=True,margins_name=f'{x[b[0]].values[0]}合计')).reset_index()
        .groupby(b[:2],sort=False)
        .apply(lambda y: pd.pivot_table(y,index=b[-1],values=a,aggfunc='sum',margins=True,margins_name=f'{y[b[1]].values[0]}小计'))
    )
    return df1[~df1.index.get_level_values(-1).str.endswith(('合计小计'))]


def main():
    # fake = Faker()


    # 假设的销售地区列表
    regions = ['华北', '华东', '华南', '华中', '西北', '西南', '东北']
    # 商品示例列表
    products = ['电视', '冰箱', '洗衣机', '空调']

    # 根据地区生成对应的城市列表
    region_cities = {
        '华北': ['北京', '天津', '石家庄'],
        '华东': ['上海', '南京', '杭州'],
        '华南': ['广州', '深圳', '海口'],
        '华中': ['武汉', '长沙', '郑州'],
        '西北': ['西安', '兰州', '银川'],
        '西南': ['成都', '重庆', '昆明'],
        '东北': ['沈阳', '大连', '哈尔滨']
    }

    # 生成数据集
    def generate_data(num_records):
        data = []
        for _ in range(num_records):
            region = random.choice(regions)
            city = random.choice(region_cities[region])
            product = random.choice(products)
            amount = round(random.uniform(1000, 5000), 2)  # 生成金额
            quantity = random.randint(1, 100)  # 生成销售数量
            data.append([region, city, product, amount, quantity])
        return data

    # 使用DataFrame存储数据
    df = pd.DataFrame(generate_data(1000), columns=['销售地区', '销售城市', '销售商品', '销售金额', '销售数量'])
    print(df.shape)
    print(df.head())

    Statistical_summary(df,['销售金额','销售数量'],['销售地区','销售城市','销售商品']).head(20)

if  __name__ == "__main__":
    main()

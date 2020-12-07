import boto3
import pandas as pd

s3 = boto3.client('s3')
# s3.download_file('proyecto-bigdata', 'raw/datos-30-11-2020.csv', 'datos.csv')
s3.download_file('proyecto-bigdata', 'refined/12-03-2020/paises/part-00000-e3cf5840-2e51-4990-b863-b791ad2d94e7-c000.csv', 'part-00000-e3cf5840-2e51-4990-b863-b791ad2d94e7-c000.csv')
s3.download_file('proyecto-bigdata', 'refined/12-03-2020/recuperados_muertos_medellin/part-00000-45365fc0-6cd5-4745-a148-54faca0d7b45-c000.csv', 'part-00000-45365fc0-6cd5-4745-a148-54faca0d7b45-c000.csv')
s3.download_file('proyecto-bigdata', 'refined/12-03-2020/recuperados_y_fallecidos_departamento/part-00000-96a21701-7931-46cc-b2b5-f4518fb240eb-c000.csv', 'part-00000-96a21701-7931-46cc-b2b5-f4518fb240eb-c000.csv')
s3.download_file('proyecto-bigdata', 'refined/12-03-2020/recuperados_y_fallecidos_etapa/part-00000-545bb26c-955c-437d-8060-dcbabaccfa67-c000.csv', 'part-00000-545bb26c-955c-437d-8060-dcbabaccfa67-c000.csv')
s3.download_file('proyecto-bigdata', 'refined/12-03-2020/sexo/part-00000-bb841ab7-b3d7-4360-97e0-48532fd349d9-c000.csv', 'part-00000-bb841ab7-b3d7-4360-97e0-48532fd349d9-c000.csv')

print(pd.read_csv('part-00000-e3cf5840-2e51-4990-b863-b791ad2d94e7-c000.csv'))
print(pd.read_csv('part-00000-45365fc0-6cd5-4745-a148-54faca0d7b45-c000.csv'))
print(pd.read_csv('part-00000-96a21701-7931-46cc-b2b5-f4518fb240eb-c000.csv'))
print(pd.read_csv('part-00000-545bb26c-955c-437d-8060-dcbabaccfa67-c000.csv'))
print(pd.read_csv('part-00000-bb841ab7-b3d7-4360-97e0-48532fd349d9-c000.csv'))
import pandas as pd

class deletesDpcts():

    def __init__(self, file_name_in, list_ex, column_name):
        self.file_name_in = file_name_in
        self.list_ex = list_ex
        self.column_name = column_name

    def get_content(self):
        df = pd.read_excel(f'{self.file_name_in}', self.list_ex)
        print(df)
        return df


class noDuplcFile(deletesDpcts):

    def delete_dubl_and_push_in_file(self,  file_name_in, list_ex, column_name):
        ds = df.drop_duplicates(subset=[self.column_name], keep="first")
        print(ds)
        ds.to_csv(f'{self.file_name_in}_dell_dplc_{self.list_ex}', encoding='utf-8', index=False)


x = deletesDpcts('baze_client.xlsx', 'пром', 'Номер')
x.get_content()
y = noDuplcFile('baze_client.xlsx', 'пром', 'Номер')
y.delete_dubl_and_push_in_file('baze_client.xlsx', 'пром', 'Номер')

# file_name_in = 'baze_client.xlsx'
# list_ex = '2021'
# df = pd.read_excel(f'{file_name_in}', list_ex)
# print(df)
#
# ds = df.drop_duplicates(subset=['Номер',], keep="first")
# ds.to_csv(f'{file_name_in}_dell_dplc_{list_ex}', encoding='utf-8', index=False)
# print(ds)
#
# #  Вернуть дубликаты в файле
# ids = df["Номер"]
# dz = df[ids.isin(ids[ids.duplicated()])]
# dz.to_csv(f'{file_name_in}_duplicated_{list_ex}', encoding='utf-8', index=False)
# print(dz)
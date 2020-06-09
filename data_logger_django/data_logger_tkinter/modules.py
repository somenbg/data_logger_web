import pandas as pd


class DataFrameManagement():
    
    
    def dict_to_df(self, data_structure: dict):
        if len(data_structure) > 1:
            df = pd.concat([pd.DataFrame(data_structure[i+1], columns=list(data_structure[i+1].keys())) 
                            for i in range(len(data_structure))], ignore_index=True)
        else:
            df = pd.DataFrame(data_structure[1], columns=list(data_structure[1].keys()))
        return df
    
    
    def create_df(self):
        df = dict_to_df(user_gui.result)
        print('File updated')
        return df
    
    
    def read_csv(self, df):
        try:
            existing_data = pd.read_csv('data.csv')
        except Exception as e:
            existing_data = pd.DataFrame()
        return existing_data
    
    
    def merge_df(self, old_df, new_df):
        new_df = old_df.append(new_df, sort=False)
        return new_df
    
    
    def create_csv(self, dataframe):
        dataframe.to_csv('data.csv', index=False)
        return dataframe

        
def get_data_structure():
    data_structure = {
                    'consultancy_name': [''],
                    'pay_rate': [''],
                    'contact_number': [''],
                    'contract': [''],
                    'contract_length': [''],
                    'training_fee': [''],
                    'relocation': [''],
                    'status': [''],
                    }
    return data_structure
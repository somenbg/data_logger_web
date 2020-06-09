import tkinter as tk
import modules as modules

fields = modules.get_data_structure().keys()

class user_gui():
    result = {}
    form_number = 0

    def fetch(self, entries):
        
        self.form_number += 1
        data = {}
        
        for entry in entries:
            field = entry[0]
            text  = entry[1].get()
            entry[1].delete(0, 'end')
            data[field] = [text]
        
        if data.get('consultancy_name') == ['']:
            self.form_number -= 1
            
        if data.get('consultancy_name') != ['']:
            self.result[self.form_number] = data
        
        

    def makeform(self, root, fields):
        entries = []
        for field in fields:
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
        return entries


if __name__ == '__main__':
    root = tk.Tk()
    user_gui = user_gui()
    ents = user_gui.makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: user_gui.fetch(e)))   
    b1 = tk.Button(root, text='Submit', command=(lambda e=ents: user_gui.fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.destroy)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
    
    df_mgr = modules.DataFrameManagement()
    if len(user_gui.result) != 0:
        df = df_mgr.dict_to_df(user_gui.result)
        existing_data = df_mgr.read_csv(df)
        if existing_data.empty:
            new_df = df
        else:
            new_df = df_mgr.merge_df(existing_data, df)
        df_mgr.create_csv(new_df)
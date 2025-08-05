def process_excel(file_path,col):
    error_data=[]
    data=[]
    for i in os.listdir(file_path):
        if i.endswith('.xlsx'):
            try:
                df = pd.read_excel(file_path)
                df_data = df[col]
                data.append(df_data)
            except Exception as e:
                error_data.append(f"Error in {i}: {e}")
            
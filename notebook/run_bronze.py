from create_delta_table_bronze.read_landing_for_bronze import CreateTableDelta

def pipeline_bronze():
    res = CreateTableDelta()
    df = res.read_df()
    res.write_table(df)

if __name__=="__main__":
    pipeline_bronze() 
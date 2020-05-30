def proportionBySport(df, yr, sport, gender):
    df.set_index("Year", inplace=True)
    df = df.loc[yr]
    df.set_index("Sex", inplace=True)
    df = df.loc[gender]
    df_tot = df
    df_tot.drop_duplicates(subset="Name", keep=False, inplace=True)
    tot = df_tot.shape[0]
    df.set_index("Sport", inplace=True)
    df = df.loc[sport]
    print(df.shape[0] / tot * 100)

# from FileLoader import FileLoader
# loader = FileLoader()
# data = loader.load('../data/athlete_events.csv')
# proportionBySport(data, 2004, 'Tennis', 'F')

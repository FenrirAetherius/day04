def proportionBySport(df, yr, sport, gender):
    df.set_index("Year", inplace=True)
    df = df.loc[yr]
    df.set_index("Sex", inplace=True)
    df = df.loc[gender]
    tot = df.shape[0]
    df.set_index("Sport", inplace=True)
    df = df.loc[sport]
    print(df.shape[0] / tot * 100)

from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('athlete_events.csv')
proportionBySport(data, 2004, 'Tennis', 'F')

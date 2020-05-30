def youngestFellah(df, yr):
    young = {"m": 100, "f": 100}
    df.set_index("Year", inplace=True)
    df = df.loc[yr]
    df.set_index("Sex", inplace=True)
    dfm = df.loc["M"]
    for i in dfm["Age"]:
        if int(i) <= young["m"]:
            young["m"] = int(i)
    dff = df.loc["F"]
    for i in dff["Age"]:
        if int(i) <= young["f"]:
            young["f"] = int(i)
    print(young)

# from FileLoader import FileLoader
# loader = FileLoader()
# data = loader.load("athlete_events.csv")
# youngestFellah(data, 2006)

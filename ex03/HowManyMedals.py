def howManyMedals(df, name):
    dic = {}
    df.set_index("Name", inplace=True)
    df = df.loc[name]
    for i, a in enumerate(df["Medal"]):
        if not df["Year"][i] in dic:
            dic[df["Year"][i]] = {'G' : 0, 'S' : 0, 'B' : 0}
        if a == "Gold":
            dic[df["Year"][i]]['G'] += 1
        if a == "Silver":
            dic[df["Year"][i]]['S'] += 1
        if a == "Bronze":
            dic[df["Year"][i]]['B'] += 1
    print(dic)

# from FileLoader import FileLoader
# loader = FileLoader()
# data = loader.load('../data/athlete_events.csv')
# howManyMedals(data, 'Kjetil Andr Aamodt')

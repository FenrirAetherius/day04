import pandas


class FileLoader:

    @staticmethod
    def load(path):
        df = pandas.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
        return df

    @staticmethod
    def display(df, n):
        if n < 0:
            print(df[n:])
            n = -n
        else:
            print(df[:n])
        print(f"\n[{n} rows x {df.shape[1]} columns]")


# dat = FileLoader.load("athlete_events.csv")
# FileLoader.display(dat, -4)

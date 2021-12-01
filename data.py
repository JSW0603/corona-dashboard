import pandas as pd

#Get a information of the world
conditions = ["confirmed", "deaths", "recovered"]

daily_df = pd.read_csv("data/daily_report.csv")
totals_df = (
    daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
)
totals_df = totals_df.rename(columns={"index": "condition"})

#making groups by country
counties_df = daily_df[["Country_Region","Confirmed", "Deaths", "Recovered"]]
counties_df = counties_df.groupby("Country_Region").sum()

#make a data of the world by country
def make_country_df(country):
    def make_df(condition):
        df = pd.read_csv(f"data/time_confirmed.csv")
        df = df.loc[df["Country/Region"] == country]
        df = df.drop(columns=["Province/State","Country/Region","Lat","Long"], axis=1).sum().reset_index(name=condition)
        df = df.rename(columns={"index": "date"})
        return df
    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df

#make a data global by the date
def make_global_df():
    def make_df(condition):
        df = pd.read_csv(f"data/time_{condition}.csv")
        df = df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1).sum().reset_index(name=condition)
        df = df.rename(columns={"index": "date"})
        return df
    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df
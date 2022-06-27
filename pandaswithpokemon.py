import pandas as pd

pokemon_dataframe = pd.read_csv('pokemon_data.csv')

#shows entire dataset
print(pokemon_dataframe)

#shows first three items in dataset
print(pokemon_dataframe.head(3))

#shows the bottom three items in dataset
print(pokemon_dataframe.tail(3))

#shows us the headers of the dataset
print(pokemon_dataframe.columns)

#Calls a specific header of the dataset, in this case, the first 3 names
print(pokemon_dataframe["Name"].head(3))

#Calls multiple headers of the last 5 items in the data
print(pokemon_dataframe[["Name","Generation","HP"]].tail(5))

#If we want to look at a specific row, at a specific pokemon
print(pokemon_dataframe.iloc[1])

#Reads specific location
print(pokemon_dataframe.iloc[2,1])

#If we want data alongside index
for index, row in pokemon_dataframe.iterrows():
    print(index, ",", row["Name"], ",", row["Type 1"])

#If we want specific data of a specific header
print(pokemon_dataframe.loc[pokemon_dataframe["Type 1"] == "Ghost"])

#Sort specific values by ascending or descending
print(pokemon_dataframe.sort_values('Name', ascending = True))

#If we want to create a new header/column
pokemon_dataframe["Total"] = pokemon_dataframe["HP"] + pokemon_dataframe["Attack"] + pokemon_dataframe["Defense"] + pokemon_dataframe["Speed"] + pokemon_dataframe["Sp. Atk"] + pokemon_dataframe["Sp. Def"]

print(pokemon_dataframe.head(5))

print(pokemon_dataframe[["Name","Total"]])

#We can remove columns as well
pokemon_dataframe = pokemon_dataframe.drop(columns =["Total"])

print(pokemon_dataframe.head(5))

#This is an easier way to add columns together

pokemon_dataframe["Total"] = pokemon_dataframe.iloc[:, 4:10].sum(axis = 1)
print(pokemon_dataframe.tail(5))

#We can rearrange columns
#Easiest if  we first get columns as a list

cols = list(pokemon_dataframe.columns.values)
pokemon_dataframe = pokemon_dataframe[cols[0:4] + [cols[-1]] + cols[4:12]]

print(pokemon_dataframe.head(5))

#Save our new file

pokemon_dataframe.to_csv("New_pokemon.csv")

#multivariable conditions
print(pokemon_dataframe.loc[(pokemon_dataframe["Type 1"] == "Grass") & (pokemon_dataframe["HP"] > 40)])

#The | means "Or"
print(pokemon_dataframe.loc[(pokemon_dataframe["Type 1"] == "Water") | (pokemon_dataframe["Type 2"] == "Fighting")])

#We can create entire new dataframes

fire_pokemon_dataframe = pokemon_dataframe.loc[pokemon_dataframe["Type 1"] == "Fire"]

fire_pokemon_dataframe = fire_pokemon_dataframe.reset_index(drop = True)

print(fire_pokemon_dataframe)

fire_pokemon_dataframe.to_csv("fire_pokemon_dataframe.csv")

#We can filter our names/words in datasets, this gets us all the items that contain "Mega"
print(pokemon_dataframe.loc[pokemon_dataframe["Name"].str.contains("Mega")])

#This removes all items that contain "Mega" with ~ operator
print(pokemon_dataframe.loc[~pokemon_dataframe["Name"].str.contains("Mega")])

#We can further change our dataset with these conditions
fire_pokemon_dataframe.loc[fire_pokemon_dataframe["Type 1"] == "Fire", "Type 1"] = "Flamer"
print(fire_pokemon_dataframe)

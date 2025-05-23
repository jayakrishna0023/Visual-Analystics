import pandas as pd
import plotly.express as px

# Step 1: Load the dataset
df = pd.read_csv("/content/world_population.csv")

# Step 2: Define the columns related to population for different years
pop_columns = ['2022 Population', '2020 Population', '2015 Population',
               '2010 Population', '2000 Population', '1990 Population',
               '1980 Population', '1970 Population']

# Step 3: Reshape the data to a long format for time series visualization
df_long = pd.melt(df,
                  id_vars=['Country/Territory', 'CCA3', 'Continent', 'Area (km²)', 'Density (per km²)'],
                  value_vars=pop_columns,
                  var_name='Year',
                  value_name='Population')

# Step 4: Clean and convert the Year column to integers
df_long['Year'] = df_long['Year'].str.extract(r'(\d{4})')
df_long['Year'] = df_long['Year'].astype(int)

# Step 5: Create a choropleth map to show global population over time
fig_choropleth = px.choropleth(
    df_long,
    locations="CCA3",
    color="Population",
    hover_name="Country/Territory",
    animation_frame="Year",
    color_continuous_scale="Viridis",
    title="Global Population Over Time (1970–2022)",
    projection="natural earth"
)

# Step 6: Customize layout of the choropleth map
fig_choropleth.update_layout(
    geo=dict(showframe=False, showcoastlines=True),
    coloraxis_colorbar=dict(title="Population")
)

# Step 7: Save and display the choropleth map
fig_choropleth.write_html("choropleth_population.html")
fig_choropleth.show()

# Step 8: Filter the dataset to get the latest year data (2022)
latest_year = df_long[df_long['Year'] == 2022]

# Step 9: Create a bubble map to show population density by continent in 2022
fig_bubble = px.scatter_geo(
    latest_year,
    locations="CCA3",
    color="Continent",
    size="Density (per km²)",
    hover_name="Country/Territory",
    title="World Population Density (2022)",
    projection="natural earth"
)

# Step 10: Customize layout of the bubble map
fig_bubble.update_layout(
    geo=dict(showland=True),
    legend_title_text='Continent'
)

# Step 11: Save and display the bubble map
fig_bubble.write_html("bubble_density.html")
fig_bubble.show()

     


     

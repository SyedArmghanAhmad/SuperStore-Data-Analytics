
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import kaleido


df = pd.read_csv(r"E:\SuperStore-Data-Analytics\Data\train.csv")
output = r"E:\SuperStore-Data-Analytics\Output\Visualizations"


df.head()

df.info()

# Filling the null values in this case 11 postal codes are missing
df["Postal Code"].fillna(0,inplace = True)
df["Postal Code"] = df["Postal Code"].astype(int)

#Checking the missing values again
df.info()

# Checking for duplicates
if df.duplicated().sum() > 0:
  print("Duplicates Exists")
else:
  print("No Duplicates in this Dataset")



df.head(3)

# now most companies struggle with actual segmentation of customers they dont have any idea about different types of customers they bring they rely on presence of mind rather than actual data so here we
#will focus on customer segmentation

types_of_customers = df['Segment'].unique()
print(types_of_customers)

#now to determine number of customers
num_of_customers = df['Segment'].value_counts().reset_index()
num_of_customers = num_of_customers.rename(columns = {'Segment' : 'Type of Customers'})
print(num_of_customers)


plt.pie(num_of_customers['count'], labels = num_of_customers['Type of Customers'], autopct = '%1.1f%%')
plt.title('Customer Segmentation')
plt.savefig(f"{output}/Customer_Segmentation_by_type_pie_chart.jpg",format='jpg', dpi=300 ,bbox_inches='tight')
plt.show()

#now we'll balance resource allocation for all 3 segments of customer to maximize growth
#to gain a deeper insight we should integrate our customer data with sales_figures
#this analysis will help us identify which segment generated most sales
sales_per_segment = df.groupby('Segment')['Sales'].sum().reset_index()
sales_per_segment = sales_per_segment.rename(columns = {'Segment' : 'Type of Customer', 'Sales' : 'Total Sales'})

print(sales_per_segment)

plt.bar(sales_per_segment['Type of Customer'], sales_per_segment['Total Sales'])
plt.xlabel('Type of Customer')
plt.ylabel('Total Sales')
plt.title('Total Sales per Customer Segment')
plt.savefig(f"{output}/Total_Sales_per_customer_segment_bar_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()

# now lets calculate customer lifetime value CLTV of each segment
plt.pie(sales_per_segment['Total Sales'], labels = sales_per_segment['Type of Customer'], autopct = '%1.1f%%')
plt.title('Customer segmentation by total sales')
plt.savefig(f"{output}/Customer_segmentation_by_total_sales_pie_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()

# Group by 'Customer ID', 'Customer Name', 'Segment' and count 'Order ID'
customer_order_frequency = df.groupby(['Customer ID', 'Customer Name', 'Segment'])['Order ID'].count().reset_index()

# Rename the column correctly without using inplace
customer_order_frequency = customer_order_frequency.rename(columns={'Order ID': 'Total Orders'})

# Filter customers with at least one order
repeat_customers = customer_order_frequency[customer_order_frequency['Total Orders'] >= 1]

# Sort customers by 'Total Orders' in descending order
repeat_customers_sorted = repeat_customers.sort_values(by='Total Orders', ascending=False)

# Print the required results
print(repeat_customers_sorted.head(12).reset_index(drop=True))



#lets identify our top spending customer
customer_sales = df.groupby(['Customer ID', 'Customer Name', 'Segment'])['Sales'].sum().reset_index()
top_spender = customer_sales.sort_values(by='Sales', ascending=False)
print(top_spender.head(12).reset_index(drop=True))


# now analyzing shipping methods
shipping_models = df['Ship Mode'].value_counts().reset_index()
shipping_models = shipping_models.rename(columns = {'index' : 'Use Frequency', 'Ship Mode' : 'Mode of Shipment'})
print(shipping_models)



plt.pie(shipping_models['count'], labels = shipping_models['Mode of Shipment'], autopct = '%1.1f%%')
plt.title('Customer Segmentation by Shipping Mode')
plt.savefig(f"{output}/Customer_Segmentation_by_shipping_mode_pie_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()


# now we analyze by states
state = df['State'].value_counts().reset_index()
state = state.rename(columns = {'index' : 'State', 'State' : 'Number of Customers'})
print(state.head(20))


City = df['City'].value_counts().reset_index()
City = City.rename(columns = {'index' : 'City', 'City' : 'Number of Customers'})
print(City.head(25))


#analyzing sales by states
state_sales  = df.groupby('State')['Sales'].sum().reset_index()
top_sales = state_sales.sort_values(by = 'Sales', ascending = False)
print(top_sales.head(25).reset_index(drop = True))


#now sorting it per city
city_sales = df.groupby('City')['Sales'].sum().reset_index()
top_city_sales = city_sales.sort_values(by = 'Sales', ascending = False)
print(top_city_sales.head(25).reset_index(drop = True))


# now working with products - first we extract product categories
products = df['Category'].unique()
print(products)


df.head(100)


#on to the subcategory of product
product_subcategory = df['Sub-Category'].unique()
print(product_subcategory)


subcategory_count = df.groupby('Category')['Sub-Category'].nunique().reset_index()
subcategory_count = subcategory_count.sort_values(by = 'Sub-Category', ascending = False)
print(subcategory_count)


#now to see top performing subcategory
subcategory_count_sales = df.groupby(['Category','Sub-Category'])['Sales'].sum().reset_index()
subcategory_count_sales = subcategory_count_sales.sort_values(by = 'Sales', ascending = False)
print(subcategory_count_sales)


#now lets see top performing main category
product_category =df.groupby(['Category'])['Sales'].sum().reset_index()
top_product_category = product_category.sort_values(by = 'Sales', ascending = False)
print(top_product_category.reset_index(drop = True))


plt.pie(top_product_category['Sales'], labels = top_product_category['Category'], autopct = '%1.1f%%')
plt.title('Sales per Main Category')
plt.savefig(f"{output}/Sales_per_main_category_pie_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()


subcategory_count_sales = subcategory_count_sales.sort_values(by = 'Sales', ascending = True)
plt.barh(subcategory_count_sales['Sub-Category'], subcategory_count_sales['Sales'])
plt.xlabel('Sales')
plt.ylabel('Sub-Category')
plt.title('Sales per Sub-Category')
plt.savefig(f"{output}/Sales_per_subcategory_bar_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()

#now to calculate Yearly sales
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
yearly_sales = df.groupby(df['Order Date'].dt.year)['Sales'].sum().reset_index()
yearly_sales = yearly_sales.rename(columns = {'Order Date' : 'Year', 'Sales' : 'Total Sales'})
print(yearly_sales)



plt.bar(yearly_sales['Year'], yearly_sales['Total Sales'])
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales per Year')
plt.tight_layout()
plt.xticks(rotation = 75)
plt.savefig(f"{output}/Sales_per_year_bar_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()

plt.plot(yearly_sales['Year'], yearly_sales['Total Sales'], marker ='o', linestyle = '-')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales per Year')
plt.xticks(rotation = 75)
plt.savefig(f"{output}/Sales_per_year_line_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()

# now lets calculate quarterly sales
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
year_sales = df[df['Order Date'].dt.year == 2018]
quarterly_sales = year_sales.resample('QE', on = 'Order Date')['Sales'].sum()
quarterly_sales = quarterly_sales.reset_index()
quarterly_sales = quarterly_sales.rename(columns = {'Order Date' : 'Quarter', 'Sales' : 'Total Sales'})
print(quarterly_sales)


plt.plot(quarterly_sales['Quarter'], quarterly_sales['Total Sales'], marker ='o', linestyle = '--')
plt.xlabel('Quarter')
plt.ylabel('Sales')
plt.title('Sales per Quarter')
plt.tight_layout()
plt.xticks(rotation = 75)
plt.savefig(f"{output}/Sales_per_quarter_line_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()


#now onto monthly_sales
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
year_sales = df[df['Order Date'].dt.year == 2018]
monthly_sales = year_sales.resample('ME', on = 'Order Date')['Sales'].sum()
monthly_sales = monthly_sales.reset_index()
monthly_sales = monthly_sales.rename(columns = {'Order Date' : 'Month', 'Sales' : 'Total Sales'})
print(monthly_sales)

plt.plot(monthly_sales['Month'], monthly_sales['Total Sales'], marker ='o', linestyle = '--')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales per Month')
plt.tight_layout()
plt.xticks(rotation = 75)
plt.savefig(f"{output}/Sales_per_month_line_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()

# Now onto the Mapping
#mapping by State for Product/Services
#Creating Mapping for all 50 states
all_state_mapping ={
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI",
    "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY", "North Carolina": "NC",
    "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI",
    "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
}
#add the abbreviation column to the DataFrame
df['Abbreviation'] = df['State'].map(all_state_mapping)

#Group by state and calculate the sum of sales
sum_of_sales = df.groupby('State')['Sales'].sum().reset_index()

#Add Abbreviation to sum of sales
sum_of_sales['Abbreviation'] = sum_of_sales['State'].map(all_state_mapping)

#Create a choropleth map using plotly
fig = go.Figure(data = go.Choropleth(locations = sum_of_sales['Abbreviation'],
                                     locationmode='USA-states',
                                     z=sum_of_sales['Sales'],
                                     hoverinfo = 'location+z',
                                     showscale=True))

fig.update_geos(projection_type="albers usa")
fig.update_layout(title_text="Total Sales by U.S. State", geo_scope='usa')
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.write_image(f"{output}/Total_sales_choropleth_map.jpg")
fig.show()


#bar chart per state
#Sort the DataFrame by the 'Sales' column in descending order
sum_of_sales = sum_of_sales.sort_values(by='Sales', ascending=True)

#Create a horizantal bar graph
plt.figure(figsize=(10, 13))
plt.barh(sum_of_sales['State'], sum_of_sales['Sales'])
plt.xlabel('Total Sales')
plt.ylabel('State')
plt.title('Total Sales per State')
plt.tight_layout()
plt.savefig(f"{output}/Sales_per_state_bar_chart.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()

# now subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.subplots_adjust(hspace=0.5)

columns = ['Segment', 'Region', 'Category', 'Sub-Category']

for i, column in enumerate(columns):
  ax = axes[i // 2, i % 2]
  sns.barplot(x='Sales', y=column, data=df, ax=ax, estimator=np.sum, errorbar=None,palette='bright', hue=column)
  ax.set_xlabel('Total Sales')
  ax.set_ylabel(column)
  ax.set_title(f'Sales by {column}')

plt.tight_layout()
plt.savefig(f"{output}/Sales_per_category_and_sub_category_bar_charts.jpg",format='jpg', dpi=300, bbox_inches='tight')
plt.show()


#Summarize the Sales data by Category and Sub category
df_summary = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
#Create a nested pie chart
fig = px.sunburst(
    df_summary,
    path=['Category', 'Sub-Category'], values='Sales',
    color='Sales',
    color_continuous_scale='RdBu',
    title='Sales by Category and Sub-Category'
)

fig.update_layout(margin=dict(t=50, l=50, r=50, b=50))
fig.write_image(f"{output}/Sales_per_category_and_sub_category_sunburst_chart.jpg")

fig.show()


#Summarize the Sales data by category, Ship Mode and Category
df_summary = df.groupby(['Category', 'Ship Mode', 'Sub-Category'])['Sales'].sum().reset_index()

#Create a treemap
fig = px.treemap(df_summary, path=['Category','Ship Mode', 'Sub-Category'], values='Sales')
fig.update_layout(margin=dict(t=50, l=50, r=50, b=50))
fig.write_image(f"{output}/Sales_per_category_ship_mode_and_sub_category_treemap_chart.jpg")
fig.show()




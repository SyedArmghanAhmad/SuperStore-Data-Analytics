
# Superstore Data Analytics

This project performs data analysis and visualizations on a dataset from a retail superstore. The analysis includes customer segmentation, sales analysis by various factors like region, category, and subcategory, as well as generating various charts and maps to derive insights from the data.

## Project Overview

The goal of this project is to perform an in-depth analysis of a retail superstore's dataset, focusing on:

- Customer segmentation
- Sales analysis by segment, region, category, and subcategory
- Identifying top spending customers
- Mapping total sales by state using choropleth maps
- Time-series analysis for yearly, quarterly, and monthly sales

## Requirements

The following libraries are required to run the project:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `plotly`
- `kaleido`

You can install the required libraries using the following:

```bash
pip install numpy pandas matplotlib seaborn plotly kaleido
```

## File Structure

- `train.csv`: The dataset containing the superstore sales data.
- `visualizations/`: A directory where all the generated visualizations are saved.
- `superstore_analysis.py`: Python script that performs data cleaning, analysis, and visualization generation.

## Data Cleaning

1. The dataset is first loaded and basic checks for missing values and duplicates are performed.
2. Missing postal codes are filled with zero, and the column is cast to integer type.
3. Duplicates in the data are checked and handled.
4. The necessary columns are analyzed and processed, such as sales by customer segment, region, state, and city.

## Analysis & Visualizations

### 1. Customer Segmentation

A pie chart representing the distribution of customers across different segments.

### 2. Sales per Customer Segment

A bar chart showing total sales per customer segment.

### 3. Top Spending Customers

A table of customers with the highest total sales and their respective customer segments.

### 4. Shipping Mode Analysis

A pie chart representing the distribution of shipping modes used by customers.

### 5. Sales Analysis by State and City

Bar charts and tables showing total sales by state and city, providing insight into regional sales performance.

### 6. Product Category and Subcategory Analysis

Pie charts and bar charts showcasing total sales by product category and subcategory.

### 7. Time-Series Sales Analysis

Line charts and bar charts displaying sales trends on a yearly, quarterly, and monthly basis.

### 8. Choropleth Map for Total Sales by State

A choropleth map displaying total sales across U.S. states, providing a geographic view of sales performance.

### 9. Sales Analysis for States

A horizontal bar chart showing total sales per state, with sales sorted in descending order.

## Running the Analysis

To run the analysis, execute the following command in your terminal or IDE:

```bash
python superstore_analysis.py
```

preferably run the notebook.

This will generate visualizations that will be saved in the `Output/Visualizations` folder.

## Conclusion

The analysis and visualizations provide insights into the superstore's sales performance, customer segments, and regional trends. This helps in understanding the business's performance and optimizing strategies for growth.

## License

This project is licensed under the MIT License.

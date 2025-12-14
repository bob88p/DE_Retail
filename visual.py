import json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import pandas as pd
import numpy as np
import os
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

# -----------------------------
# 1. Create output folder
# -----------------------------
output_folder = "dashboard_outputs"
os.makedirs(output_folder, exist_ok=True)

# -----------------------------
# 2. Load JSON and clean keys
# -----------------------------
with open('frontend_data.json', 'r') as f:
    data = json.load(f)
data = {k.strip(): v for k, v in data.items()}

# Convert JSON to DataFrames
avg_spending_df       = pd.DataFrame(data.get('Average_spending', []))
best_staff_df         = pd.DataFrame(data.get('Best_staff', []))
low_stock_df          = pd.DataFrame(data.get('Products_low_stock', []))
revenue_category_df   = pd.DataFrame(data.get('Revenue_category', []))
revenue_store_df      = pd.DataFrame(data.get('Revenue_store', []))
staff_performance_df  = pd.DataFrame(data.get('Staff_Performance', []))
stores_inventory_df   = pd.DataFrame(data.get('Stores_inventory', []))
top_customers_df      = pd.DataFrame(data.get('top_customers_spending', []))
monthly_sales_df      = pd.DataFrame(data.get('Monthly_sales', []))
top_products_df       = pd.DataFrame(data.get('Top_products', []))

# -----------------------------
# 3. Set safe style
# -----------------------------
plt.style.use('seaborn-v0_8-darkgrid')  # compatible Seaborn style
sns.set_theme(style="darkgrid")
sns.set_palette("husl")

# -----------------------------
# 4. 3x3 Dashboard Figure
# -----------------------------
fig = plt.figure(figsize=(20, 15))

# --- Revenue by Store ---
ax1 = plt.subplot(3,3,1)
if not revenue_store_df.empty:
    bars1 = ax1.bar(revenue_store_df['store_name'], revenue_store_df['Revenue'],
                    color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    ax1.set_title('Revenue by Store', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Revenue ($)', fontsize=12)
    ax1.tick_params(axis='x', rotation=45)
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 50000,
                 f'${height/1000000:.1f}M', ha='center', va='bottom', fontsize=10)

# --- Revenue by Category ---
ax2 = plt.subplot(3,3,2)
if not revenue_category_df.empty:
    bars2 = ax2.barh(revenue_category_df['category_name'], revenue_category_df['Revenue_Category'],
                     color=sns.color_palette("viridis", len(revenue_category_df)))
    ax2.set_title('Revenue by Product Category', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Revenue ($)', fontsize=12)
    for i, (value, name) in enumerate(zip(revenue_category_df['Revenue_Category'], revenue_category_df['category_name'])):
        ax2.text(value + 50000, i, f'${value/1000000:.1f}M', va='center', fontsize=10)

# --- Staff Performance ---
ax3 = plt.subplot(3,3,3)
if not staff_performance_df.empty:
    bars3 = ax3.bar(staff_performance_df['full_name'], staff_performance_df['Count_order'],
                    color=sns.color_palette("coolwarm", len(staff_performance_df)))
    ax3.set_title('Staff Performance (Orders)', fontsize=14, fontweight='bold')
    ax3.set_ylabel('Number of Orders', fontsize=12)
    ax3.tick_params(axis='x', rotation=45)
    best_staff_row = staff_performance_df.head(1)
    if not best_staff_row.empty:
        bars3[0].set_color('#FFD700')

# --- Top 10 Customers by Avg Spending ---
ax4 = plt.subplot(3,3,4)
if not avg_spending_df.empty:
    top_10_avg = avg_spending_df.nlargest(10, 'avg_spending')
    bars4 = ax4.barh(top_10_avg['full_name'], top_10_avg['avg_spending'],
                     color=sns.color_palette("YlOrRd", len(top_10_avg)))
    ax4.set_title('Top 10 Customers by Avg Spending', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Average Spending ($)', fontsize=12)
    ax4.xaxis.set_major_formatter(FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# --- Top 5 Customers by Total Spending ---
ax5 = plt.subplot(3,3,5)
if not top_customers_df.empty:
    bars5 = ax5.barh(top_customers_df['full_name'], top_customers_df['spending'],
                     color=sns.color_palette("RdPu", len(top_customers_df)))
    ax5.set_title('Top 5 Customers by Total Spending', fontsize=14, fontweight='bold')
    ax5.set_xlabel('Total Spending ($)', fontsize=12)
    for i, (value, name) in enumerate(zip(top_customers_df['spending'], top_customers_df['full_name'])):
        ax5.text(value + 5000, i, f'${value/1000:.0f}K', va='center', fontsize=10)

# --- Store Inventory ---
ax6 = plt.subplot(3,3,6)
if not stores_inventory_df.empty:
    bars6 = ax6.bar(stores_inventory_df['store_name'], stores_inventory_df['quantity_product'],
                    color=['#9B59B6', '#3498DB', '#2ECC71'])
    ax6.set_title('Store Inventory Levels', fontsize=14, fontweight='bold')
    ax6.set_ylabel('Quantity in Stock', fontsize=12)
    ax6.tick_params(axis='x', rotation=45)

# --- Low Stock Products ---
ax7 = plt.subplot(3,3,7)
if not low_stock_df.empty:
    critical_stock = low_stock_df.nsmallest(10, 'quantity_product')
    critical_stock['short_name'] = critical_stock['product_name'].apply(lambda x: x[:30]+'...' if len(x)>30 else x)
    bars7 = ax7.barh(critical_stock['short_name'], critical_stock['quantity_product'],
                     color=sns.color_palette("Reds_r", len(critical_stock)))
    ax7.set_title('Critical Low Stock Products', fontsize=14, fontweight='bold')
    ax7.set_xlabel('Quantity Remaining', fontsize=12)
    for i, qty in enumerate(critical_stock['quantity_product']):
        if qty <= 10:
            bars7[i].set_color('#E74C3C')

# --- Top Selling Products ---
ax8 = plt.subplot(3,3,8)
if not top_products_df.empty:
    top_products_df['short_name'] = top_products_df['product_name'].apply(lambda x: x[:25]+'...' if len(x)>25 else x)
    bars8 = ax8.barh(top_products_df['short_name'], top_products_df['quantity_product'],
                     color=sns.color_palette("Greens", len(top_products_df)))
    ax8.set_title('Top Selling Products', fontsize=14, fontweight='bold')
    ax8.set_xlabel('Quantity Sold', fontsize=12)

# --- Orders Distribution ---
ax9 = plt.subplot(3,3,9)
if not avg_spending_df.empty:
    order_counts = avg_spending_df['count_order'].value_counts().sort_index()
    ax9.pie(np.array(order_counts.values, dtype=float), labels=[f'{k} order(s)' for k in order_counts.index],
            autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    ax9.set_title('Customer Order Frequency', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.suptitle('Sales Dashboard Overview', fontsize=18, fontweight='bold', y=1.02)

# --- Save 3x3 Dashboard as PNG ---
dashboard_path = os.path.join(output_folder, "dashboard_overview.png")
fig.savefig(dashboard_path, bbox_inches='tight', dpi=300)
plt.close(fig)
print(f"Saved 3x3 dashboard: {dashboard_path}")

# -----------------------------
# Monthly Sales Analysis
# -----------------------------
if not monthly_sales_df.empty:
    monthly_sales_filtered = monthly_sales_df[monthly_sales_df['years'] < 2080]
    monthly_sales_filtered['date'] = pd.to_datetime(
        monthly_sales_filtered['years'].astype(str) + '-' + 
        monthly_sales_filtered['months'].astype(str) + '-01'
    )
    monthly_sales_filtered = monthly_sales_filtered.sort_values('date')

    fig2, (ax21, ax22) = plt.subplots(2,1, figsize=(15,10))

    # Revenue Trend
    ax21.plot(monthly_sales_filtered['date'], monthly_sales_filtered['Revenue_Month'],
              marker='o', linewidth=2, color='#2980B9')
    ax21.fill_between(monthly_sales_filtered['date'], monthly_sales_filtered['Revenue_Month'],
                      alpha=0.3, color='#3498DB')
    ax21.set_title('Monthly Revenue Trend', fontsize=16, fontweight='bold')
    ax21.set_ylabel('Revenue ($)', fontsize=12)
    ax21.grid(True, alpha=0.3)
    ax21.yaxis.set_major_formatter(FuncFormatter(lambda x,p: f'${x/1000:.0f}K'))

    # YoY Comparison
    years = sorted(monthly_sales_filtered['years'].unique())
    colors = ['#E74C3C', '#2ECC71', '#3498DB']
    for idx, year in enumerate(years):
        year_data = monthly_sales_filtered[monthly_sales_filtered['years']==year]
        ax22.plot(range(1,13), [year_data[year_data['months']==m]['Revenue_Month'].values[0]
                                if m in year_data['months'].values else 0 for m in range(1,13)],
                  label=str(year), marker='o', linewidth=2, color=colors[idx%len(colors)])
    ax22.set_title('Year-over-Year Monthly Comparison', fontsize=16, fontweight='bold')
    ax22.set_xlabel('Month', fontsize=12)
    ax22.set_ylabel('Revenue ($)', fontsize=12)
    ax22.set_xticks(range(1,13))
    ax22.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax22.legend(title='Year')
    ax22.grid(True, alpha=0.3)
    ax22.yaxis.set_major_formatter(FuncFormatter(lambda x,p: f'${x/1000:.0f}K'))

    # Save Monthly Sales
    monthly_sales_path = os.path.join(output_folder, "monthly_sales_analysis.png")
    fig2.savefig(monthly_sales_path, bbox_inches='tight', dpi=300)
    plt.close(fig2)
    print(f"Saved monthly sales analysis: {monthly_sales_path}")

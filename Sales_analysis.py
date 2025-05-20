
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime


def analyze_sales_data(df):
    results = {}

    if 'Price' in df.columns and 'Quantity' in df.columns:
        df['Total'] = df['Price'] * df['Quantity']

    if 'Price' in df.columns:
        results['Average Price'] = df['Price'].mean()
        results['Highest Price Product'] = df.loc[df['Price'].idxmax(), ['Product', 'Price']]
        results['Lowest Price Product'] = df.loc[df['Price'].idxmin(), ['Product','Price']]

    if 'Quantity' in df.columns:
        results['Average Quantity Sold'] = df['Quantity'].mean()
        top_product = df.groupby('Product')['Quantity'].sum().idxmax()
        results['Top Selling Product'] = top_product

    if 'Profit' in df.columns:
        results['Average Profit'] = df['Profit'].mean()
        top_profit_product = df.groupby('Product')['Profit'].sum().idxmax()
        results['Most Profitable Product'] = top_profit_product

    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.dropna(subset=['Date'], inplace=True)
        df['Month'] = df['Date'].dt.to_period('M')
        monthly_profits = df.groupby('Month')['Profit'].sum()
        if not monthly_profits.empty:
            results['Best Month (Profit)'] = monthly_profits.idxmax().strftime('%Y-%m')

    if 'PaymentMethod' in df.columns:
        results['Most Used Payment Method'] = df['PaymentMethod'].mode()[0]

    if 'City' in df.columns:
        city_sales = df.groupby('City')['Quantity'].sum()
        if not city_sales.empty:
            results['Top City (Sales)'] = city_sales.idxmax()
            results['Lowest City (Sales)'] = city_sales.idxmin()

    return results, df


def save_charts(df, chart_dir):
    os.makedirs(chart_dir, exist_ok=True)

    if 'Product' in df.columns and 'Quantity' in df.columns:
        top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
        top_products.plot(kind='bar', title='Top 5 Selling Products')
        plt.ylabel('Quantity Sold')
        plt.tight_layout()
        plt.savefig(os.path.join(chart_dir, 'top_products.png'))
        plt.close()

    if 'Date' in df.columns and 'Profit' in df.columns:
        df['Month'] = df['Date'].dt.to_period('M')
        profit_per_month = df.groupby('Month')['Profit'].sum()
        profit_per_month.plot(kind='bar', title='Profit per Month')
        plt.ylabel('Total Profit')
        plt.tight_layout()
        plt.savefig(os.path.join(chart_dir, 'profit_per_month.png'))
        plt.close()

    if 'PaymentMethod' in df.columns:
        df['PaymentMethod'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Payment Methods')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig(os.path.join(chart_dir, 'payment_methods.png'))
        plt.close()

    if 'City' in df.columns and 'Quantity' in df.columns:
        df.groupby('City')['Quantity'].sum().plot(kind='bar', title='Sales by City')
        plt.ylabel('Quantity Sold')
        plt.tight_layout()
        plt.savefig(os.path.join(chart_dir, 'city_sales.png'))
        plt.close()



def save_results(results_dict, df, original_filename):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    base_folder = os.path.join("results", timestamp)
    os.makedirs(base_folder, exist_ok=True)

    # Save CSV summary
    summary_path = os.path.join(base_folder, "summary.csv")
    pd.DataFrame(results_dict.items(), columns=["Metric", "Value"]).to_csv(summary_path, index=False)

    # Save TXT summary
    txt_path = os.path.join(base_folder, "summary.txt")
    with open(txt_path, "w") as f:
        for key, value in results_dict.items():
            f.write(f"{key}: {value}\n")

    # Save charts
    chart_dir = os.path.join(base_folder, "charts")
    save_charts(df, chart_dir)

    return base_folder



def open_file_and_analyze():
    file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return

    try:
        df = pd.read_csv(file_path)
        results, clean_df = analyze_sales_data(df)
        folder_path = save_results(results, clean_df, file_path)
        messagebox.showinfo("Success", f"Analysis completed and saved in:\n{folder_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")


root = tk.Tk()
root.title("Sales Analyzer")
root.geometry("300x150")

label = tk.Label(root, text="Click below to select your sales CSV file", pady=10)
label.pack()

analyze_button = tk.Button(root, text="Select CSV File", command=open_file_and_analyze)
analyze_button.pack(pady=20)

root.mainloop()

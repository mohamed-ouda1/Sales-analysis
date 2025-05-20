**Sales Analyzer Script - Usage Guide**

---

**📄 Description:**
This script provides a simple graphical interface for analyzing sales data from a CSV file. It calculates various statistics, generates visual charts, and saves the results in a well-organized folder.

---

**📁 What the Script Can Do:**

1. Calculate:

   * Average price
   * Average quantity sold
   * Most sold product
   * Most profitable product
   * Highest/lowest priced product
   * Most used payment method *(if column exists)*
   * City with highest/lowest sales *(if column exists)*
   * Month with highest total profit *(if date column exists)*

2. Generate Charts:

   * Top 5 selling products (bar chart)
   * Profit per month (bar chart)
   * Payment method distribution (pie chart)
   * City-wise sales (bar chart)

3. Save Results:

   * `summary.csv`: table of analysis results
   * `summary.txt`: readable summary file
   * `charts/`: folder containing PNG images of generated charts
   * All saved under a timestamped folder inside a main `results/` directory

---

**⚖️ Requirements Before Running the Script:**

1. Prepare a clean CSV file with properly named columns. Recommended columns:

   * `Product`, `Price`, `Quantity`, `Profit`, `Date`, `PaymentMethod`, `City`

2. Remove:

   * Empty values
   * Outliers or invalid entries
   * Columns with inconsistent naming (make sure names are exactly as listed above)

3. Save the cleaned dataset as a new `.csv` file.

---

**🔄 How to Use the Script:**

1. Run the script by double-clicking or using your IDE.
2. A small window will appear.
3. Click the "Analyze Sales Data" button.
4. Choose your cleaned CSV file.
5. Wait for analysis to complete.
6. When finished, a pop-up will show you the path where results are saved.

---

**📂 Output Folder Structure:**

```
results/
︿ 2025-05-16_15-55-30/         <- Timestamped folder
   ├─ summary.csv             <- Key insights in table format
   ├─ summary.txt             <- Human-readable summary
   └─ charts/                <- Charts as PNG images
       ├─ top_products.png
       ├─ profit_per_month.png
       ├─ payment_methods.png
       └─ city_sales.png
```

---

**✅ Notes:**

* If some columns like `Profit` or `City` are missing, those parts will be skipped automatically.
* All dates must be in a valid format (`YYYY-MM-DD`, etc.).
* You can re-run the script multiple times with different files. Each result is saved in a new folder.

---

Created by: Mohamed Ouda
Version: 1.0
Date: May 2025

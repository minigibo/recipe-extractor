# Samsung Food Recipe Scraper

A Python script that extracts ingredients from Samsung Food app recipes and exports them to an Excel file using Selenium WebDriver.

## Features

- Extracts ingredients from Samsung Food recipe URLs
- Processes multiple recipes in batch
- Exports data to Excel format with each recipe as a separate column
- Runs in headless Chrome mode for efficient processing

## Prerequisites

### Required Software
- Python 3.x
- Google Chrome browser
- ChromeDriver

### Required Python Packages
```bash
pip install pandas selenium openpyxl
```

### ChromeDriver Setup
1. Download ChromeDriver from [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
2. Extract the ChromeDriver executable
3. Update the `chrome_driver_path` variable in the script with your ChromeDriver location

## Configuration

Before running the script, update the following variables:

```python
# Update this path to match your ChromeDriver location
chrome_driver_path = "C:/path/to/your/chromedriver.exe"

# Add your Samsung Food recipe URLs here
recipe_urls = [
    'https://app.samsungfood.com/recipes/your-recipe-id-1',
    'https://app.samsungfood.com/recipes/your-recipe-id-2',
    # Add more URLs as needed
]

# Specify your output file name
output_excel_file = 'recipes_ingredients.xlsx'
```

## Usage

1. **Clone or download the script**

2. **Install dependencies:**
   ```bash
   pip install pandas selenium openpyxl
   ```

3. **Configure ChromeDriver path and recipe URLs** (see Configuration section above)

4. **Run the script:**
   ```bash
   python samsung_food_scraper.py
   ```

5. **Check the output:** The script will create an Excel file with ingredients from all specified recipes.

## How It Works

1. **Web Scraping:** Uses Selenium WebDriver to navigate to Samsung Food recipe pages
2. **Data Extraction:** Locates ingredient elements using XPath selectors (`data-testid='recipe-ingredient'`)
3. **Data Processing:** Organizes ingredients into pandas DataFrames with each recipe as a separate column
4. **Export:** Saves the combined data to an Excel file

## Output Format

The Excel file will have the following structure:
- Each column represents a recipe (Recipe 1, Recipe 2, etc.)
- Each row contains an ingredient from the corresponding recipe
- Empty cells indicate recipes with fewer ingredients than others

## Troubleshooting

### Common Issues

**ChromeDriver not found:**
- Ensure ChromeDriver is downloaded and the path is correct in the script
- Make sure ChromeDriver version matches your Chrome browser version

**No ingredients extracted:**
- Verify that the Samsung Food URLs are accessible
- Check if the website structure has changed (XPath selectors may need updating)
- Ensure you have internet connection

**Permission errors:**
- Run the script with appropriate permissions
- Check that the output directory is writable

### Browser Options

The script runs Chrome in headless mode with these options:
- `--headless`: Runs without GUI
- `--no-sandbox`: Disables sandbox for compatibility
- `--disable-dev-shm-usage`: Prevents memory issues

## Customization

### Adding More Recipes
Simply add more URLs to the `recipe_urls` list:
```python
recipe_urls = [
    'https://app.samsungfood.com/recipes/recipe1',
    'https://app.samsungfood.com/recipes/recipe2',
    'https://app.samsungfood.com/recipes/recipe3',
]
```

### Changing Output Format
Modify the `process_recipes` function to change how data is structured in the Excel file.

### Adjusting Wait Times
Increase the `time.sleep(3)` value if recipes are loading slowly.

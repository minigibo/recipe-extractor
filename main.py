import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


chrome_driver_path = "C:/Users/Mattg/OneDrive/Documents/Coding/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(chrome_driver_path)


driver = webdriver.Chrome(service=service, options=chrome_options)

def extract_ingredients(recipe_url):
    # Navigate to the recipe page
    driver.get(recipe_url)
    time.sleep(3)

    # Find elements based on XPATH
    ingredient_spans = driver.find_elements(By.XPATH, "//span[@data-testid='recipe-ingredient']")

    print(ingredient_spans)

    # Extract text from each ingredient span
    ingredients = [span.text for span in ingredient_spans]

    return ingredients

def process_recipes(recipe_urls, output_excel_file):
    all_recipes_data = []

    for idx, recipe_url in enumerate(recipe_urls):
        print(f"Processing recipe {idx + 1}...")

        # Extract ingredients for each recipe
        ingredients = extract_ingredients(recipe_url)

        # Create a DataFrame where each ingredient is in a new row
        recipe_df = pd.DataFrame({f"Recipe {idx + 1}": ingredients})

        # Append to the list of all recipe data
        all_recipes_data.append(recipe_df)

    # Concatenate all recipe DataFrames
    final_df = pd.concat(all_recipes_data, axis=1)

    # Save the DataFrame to Excel
    final_df.to_excel(output_excel_file, index=False)
    print(f"Data saved to {output_excel_file}")

# List of recipe URLs
recipe_urls = [
    'https://app.samsungfood.com/recipes/1070190cae375bc7e2da4a09dd9ceda44fa'
]

# Output Excel file
output_excel_file = 'recipes_ingredients.xlsx'

# Process the recipes and save to Excel
process_recipes(recipe_urls, output_excel_file)

# Quit the WebDriver
driver.quit()

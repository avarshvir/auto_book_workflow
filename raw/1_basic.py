from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        # Launch a Chromium browser instance (headless=True by default)
        # To see the browser UI, change headless=False
        browser = p.chromium.launch(headless=False)
        
        # Create a new browser context (isolated session, like incognito)
        context = browser.new_context()
        
        # Create a new page (tab) in the browser context
        page = context.new_page()
        
        # Navigate to a URL
        page.goto("https://jaiho-labs.onrender.com")
        
        # Print the page title
        print(f"Page title: {page.title()}")
        
        # Take a screenshot
        page.screenshot(path="example.png")
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    main()
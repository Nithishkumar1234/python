from playwright.sync_api import sync_playwright


def open_techjays():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True to run in the background
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.techjays.com/")

        # Click on the "Services" dropdown
        services_locator = page.locator("text=Services")
        services_locator = page.locator("css=nav .services-dropdown")  # Adjust based on the actual class
        # Ensure element is visible before clicking
        services_locator.click()

        # Click on "Artificial Intelligence & Data" option
        ai_data_locator = page.locator("text=Artificial Intelligence & Data")
        ai_data_locator = page.locator(
            "//div[contains(@class, 'dropdown-link') and text()='Artificial Intelligence & Data']")
        # Ensure element is visible before clicking
    services_locator.hover()

    ai_data_locator.click()

    # Scroll to the "Book A Call To Tell Us Your Vision" section
    book_call_locator = page.locator("css=.book-call-section h2")  # Adjust the CSS selector
    book_call_locator.scroll_into_view_if_needed()

    # Keep the browser open for a few seconds before closing (optional)
    page.wait_for_timeout(5000)

    browser.close()


if __name__ == "__main__":
    open_techjays()




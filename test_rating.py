from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    """
    Tento test  se pokusí otevřít odkaz "https://www.pinoys.cz/customer/rating/" a ověří, že se do této sekce nelze dostat bez přihlášení = uživatel bude přesměrován na přihlašovací formulář.
    """
    page.goto("https://www.pinoys.cz/customer/rating/")
    page.get_by_role("button", name="Nesouhlasím").click()
    page.get_by_role("heading", name="Přihlášení zákazníka").click()
    expect(page.get_by_role("heading", name="Přihlášení zákazníka")).to_be_visible()
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    """
    Tento test:
    1. Otevře stránku https://www.pinoys.cz/customer/registration/.
    2. Odmítne cookies.
    3. Do pole "Váš email" vloží neplatnou e-mailovou adresu d@d.d.
    4. Ověří, že stránka rozpozná neplatnou adresu a vypíše text "Máte e-mail správně? Zadali jste neexistující doménu".
    """
    page.goto("https://www.pinoys.cz/customer/registration/")
    page.get_by_role("button", name="Nesouhlasím").click()
    page.get_by_role("textbox", name="Váš email").click()
    page.get_by_role("textbox", name="Váš email").fill("d@d.d")
    expect(page.get_by_text("Máte e-mail správně? Zadali jste neexistující doménu.")).to_be_visible()
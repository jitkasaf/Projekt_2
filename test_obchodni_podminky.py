from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    """
    Tento test:
    1. Otevře stránku https://www.pinoys.cz/.
    2. Odmítne cookies.
    3. Klikne na odkaz "Všeobecné obchodní podmínky".
    4. Ověří, že stránka obsahuje text "Odstoupení od Smlouvy a reklamace zboží".
    """
    page.goto("https://www.pinoys.cz/")
    page.get_by_role("button", name="Nesouhlasím").click()
    page.get_by_role("link", name="Všeobecné obchodní podmínky").click()
    page.wait_for_load_state("domcontentloaded")
    expect(page.locator("text=V. Odstoupení od Smlouvy a reklamace zboží")).to_be_visible()
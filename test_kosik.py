import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    """
    Tento test:
    1. Otevře stránku https://www.pinoys.cz/.
    2. Odmítne cookies.
    3. Vyhledá produkt "kimchi" a vloží jej do košíku.
    4. Zobrazí obsah košíku, odebere z něj produkt a ověří, že se zobrazí hláška "Žádná položka".
    """
    page.goto("https://www.pinoys.cz/")
    page.get_by_role("button", name="Nesouhlasím").click()
    page.get_by_role("searchbox", name="Vyhledat").click()
    page.get_by_label("Napište, co hledáte").fill("kimchi")
    page.locator("div").filter(has_text=re.compile(r"^Napište, co hledáteZavřít vyhledávání$")).locator("svg").first.click()
    page.get_by_role("link", name="Čerstvé korejské kimchi, krájené 150 g - Bibigo").click()
    page.get_by_role("button", name="Do košíku", exact=True).click()
    page.get_by_role("button", name="Přejít do košíku ").click()
    page.get_by_title("Odebrat produkt").click()
    expect(page.get_by_text("Žádná položka")).to_be_visible()
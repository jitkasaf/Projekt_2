# discord: jitka_saf

import re
from playwright.sync_api import Page, expect

# test obchodní podmínky:
def test_obchodni_podminky(page: Page) -> None:
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


# test registrace:
def test_registrace(page: Page) -> None:
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


# test rating:
def test_rating(page: Page) -> None:
    """
    Tento test  se pokusí otevřít odkaz "https://www.pinoys.cz/customer/rating/" a ověří, že se do této sekce nelze dostat bez přihlášení = uživatel bude přesměrován na přihlašovací formulář.
    """
    page.goto("https://www.pinoys.cz/customer/rating/")
    page.get_by_role("button", name="Nesouhlasím").click()
    page.get_by_role("heading", name="Přihlášení zákazníka").click()
    expect(page.get_by_role("heading", name="Přihlášení zákazníka")).to_be_visible()


# test košík:
def test_kosik(page: Page) -> None:
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
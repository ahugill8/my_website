import asyncio, sys
from playwright.async_api import async_playwright

BASE = "http://localhost:8000"
PAGES = ["index.html", "about.html", "publications.html", "editorial.html", "cv.html", "contact.html"]

async def main():
    errors_found = False
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        page = await browser.new_page(viewport={"width": 1280, "height": 900})
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda exc: console_errors.append(str(exc)))

        for name in PAGES:
            console_errors.clear()
            resp = await page.goto(f"{BASE}/{name}", wait_until="networkidle")
            status = resp.status if resp else "NO RESPONSE"
            print(f"--- {name} --- status={status}")

            # check broken image (naturalWidth 0)
            broken = await page.eval_on_selector_all(
                "img", "imgs => imgs.filter(i => i.complete && i.naturalWidth === 0).map(i => i.src)"
            )
            if broken:
                print(f"  BROKEN IMAGES: {broken}")
                errors_found = True

            # check internal nav links resolve (basic count)
            nav_links = await page.eval_on_selector_all(".nav__links a", "as => as.map(a => a.getAttribute('href'))")
            print(f"  nav links: {nav_links}")

            if console_errors:
                print(f"  CONSOLE ERRORS: {console_errors}")
                errors_found = True

            await page.screenshot(path=f"/root/website/scripts/screenshot_{name.replace('.html','')}.png", full_page=True)

        # Interaction test: help tab on home page
        await page.goto(f"{BASE}/index.html", wait_until="networkidle")
        tab = await page.query_selector(".help-tab")
        classes_before = await tab.get_attribute("class")
        await tab.click()
        classes_after = await tab.get_attribute("class")
        print(f"help-tab class before={classes_before!r} after={classes_after!r}")
        if "is-open" not in classes_after:
            print("  HELP TAB DID NOT OPEN")
            errors_found = True
        await page.screenshot(path="/root/website/scripts/screenshot_index_help_open.png", full_page=True)

        # Interaction test: publications orbit positioning
        await page.goto(f"{BASE}/publications.html", wait_until="networkidle")
        positions = await page.eval_on_selector_all(
            ".pub-logo", "els => els.map(e => ({left: e.style.left, top: e.style.top}))"
        )
        print(f"pub-logo positions: {positions}")
        if any(p["left"] == "" for p in positions):
            print("  PUB LOGOS NOT POSITIONED")
            errors_found = True

        # mobile viewport check for nav toggle + help tab
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.goto(f"{BASE}/index.html", wait_until="networkidle")
        await page.screenshot(path="/root/website/scripts/screenshot_index_mobile.png", full_page=True)
        toggle_visible = await page.is_visible(".nav__toggle")
        print(f"mobile nav toggle visible: {toggle_visible}")
        if not toggle_visible:
            errors_found = True

        await browser.close()

    print("\nRESULT:", "FAIL - see issues above" if errors_found else "ALL CHECKS PASSED")
    sys.exit(1 if errors_found else 0)

asyncio.run(main())

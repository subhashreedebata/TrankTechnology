import pytest
import pytest_html
from playwright.sync_api import sync_playwright
from config import base_url



@pytest.fixture(scope="session")
def page(request):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    page.goto(base_url)
    page.wait_for_load_state("load")

    yield page

    context.close()
    browser.close()
    p.stop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            from pathlib import Path
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            page.screenshot(path=str(file_name))

            extra.append(pytest_html.extras.image(str(file_name)))

        report.extra = extra
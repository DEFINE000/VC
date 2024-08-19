from playwright.sync_api import Playwright, sync_playwright, expect
import requests


def run(playwright: Playwright) -> None:
    #browser = playwright.chromium.launch(headless=False)
    #context = browser.new_context()
    #context.tracing.start(screenshots=True,sources=True,snapshots=True)#playwright show-trace trace.zip
    #page = context.new_page()
    #定位操作元素，.class，#id，什么都不加表示tag，标签;;;["herf=''""]
    #page.locator("xxx").
    #r=page.goto("https://scholar.google.com/schhp?hl=zh-CN")
    #page.wait_for_timeout(50000)
    #print(page.content())
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True,sources=True,snapshots=True)
    page = context.new_page()
    page.set_default_timeout(120000)
    page.goto("https://scholar.google.com/schhp?hl=zh-CN")
    page.get_by_role("textbox", name="搜索").fill("Haibo He")
    page.get_by_role("button", name="搜索").click()
    page.get_by_role("link", name="“Haibo He”的用户个人学术档案").click()
    page.get_by_role("heading", name="Haibo He").get_by_role("link").click()


    page.get_by_role("link", name="年份").click()
    #page.get_by_role("link", name="引用次数").click()
    page.wait_for_load_state(state="load",timeout=120000)
    papers_contexts=page.locator("#gsc_a_b > tr.gsc_a_tr > td.gsc_a_t > a").all_inner_texts()
    cites_counts=page.locator("#gsc_a_b > tr.gsc_a_tr > td.gsc_a_c > a").all_inner_texts()
    papers_dates=page.locator("#gsc_a_b > tr.gsc_a_tr > td.gsc_a_y > span").all_inner_texts()
    rpl=page.locator("#gsc_a_b > tr.gsc_a_tr > td.gsc_a_t > a").all()
    rpl[1].click()
    papers_urls=page.locator("#gsc_oci_title > a").get_attribute("href")
    page.locator("#gsc_oci_title > a").click()
    page.get_by_role("link", name="Institutional Sign In").click()
    page.get_by_role("button", name="SeamlessAccess Access Through").click()
    page.get_by_label("Search for your Institution").click()
    page.wait_for_load_state(state="load",timeout=180000)
    page.keyboard.type("Southern University of Science and Technology")
    page.get_by_role("link", name="Southern University of Science and Technology").click()
    page.locator("#username").fill("30021063")
    page.locator("#password").fill("Xs147258")
    page.get_by_role("button", name="登录").click()
    page.get_by_role("button", name="接受").click()
    page.wait_for_load_state(state="load",timeout=180000)
    page.get_by_role("link", name="PDF").click()
    
    page.wait_for_load_state(state="load",timeout=180000)
    pdf_url=page.locator("body > iframe").get_attribute("src")
    papers_cookies=context.cookies(pdf_url)
    #context.storage_state(path="cookies.json")
    #cookies=papers_cookies.get("cookies")
    cookies=dict(cookies=str(papers_cookies))
    res=requests.get(url=pdf_url,cookies=cookies)
    with open("paper_download.pdf","wb") as file:
        file.write(res.content)
    page.wait_for_timeout(50000)
    # ---------------------
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
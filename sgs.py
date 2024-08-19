from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://web.sanguosha.com/login/index.html")
    page.locator("#toggleThirdLogin").click()
    page.get_by_role("link", name="QQ登录").click()
    page.frame_locator("iframe[name=\"ptlogin_iframe\"]").get_by_role("link", name="[v]").click()
    page.get_by_role("button", name="进入游戏").click()
    page.wait_for_timeout(70000)
    page.locator("#layaCanvas").click(position={"x":1228,"y":87})
    page.wait_for_timeout(5000)
    page.locator("#layaCanvas").click(position={"x":1129,"y":87})
    page.wait_for_timeout(5000)
    page.locator("#layaCanvas").click(position={"x":1046,"y":143})
    page.wait_for_timeout(5000)
    page.locator("#layaCanvas").click(position={"x":912,"y":326})
    page.wait_for_timeout(5000)
    page.locator("#layaCanvas").click(position={"x":837,"y":311})
    page.wait_for_timeout(1000)
    page.locator("#layaCanvas").click(position={"x":837,"y":311})
    page.wait_for_timeout(5000)
    page.locator("#layaCanvas").click(position={"x":417,"y":257})
    page.wait_for_timeout(5000)
    i=0
    while i<20 :
        page.locator("#layaCanvas").click(position={"x":1166,"y":432})
        page.wait_for_timeout(5000)
        page.locator("#layaCanvas").click(position={"x":1005,"y":594})
        if i==0 :
            page.wait_for_timeout(10000)
            page.locator("#layaCanvas").click(position={"x":36,"y":552})
        else :
            pass
        page.wait_for_timeout(70000)
        page.locator("#layaCanvas").click(position={"x":649,"y":654})
        page.wait_for_timeout(5000)
        page.locator("#layaCanvas").click(position={"x":649,"y":654})
        page.wait_for_timeout(5000)
        i=i+1
        print(i)
    print("运行结束")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

from pathlib import Path
from playwright.async_api import async_playwright
#import asyncio

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
TEXT_OUTPUT_PATH = "data/chapter_1.txt"
IMG_OUTPUT_PATH = "data/chapter_1.png"

async def fetch_chapter():
    async with async_playwright() as p:
        print("Browser")
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(URL)

        print("Save screenshot") #screenshot 
        await page.screenshot(path=IMG_OUTPUT_PATH, full_page=True)

        print("Extract text of chapter")
        content = await page.inner_text("div#mw-content-text")

        Path(TEXT_OUTPUT_PATH).write_text(content, encoding="utf-8")
        print(f"Chapter text saved to {TEXT_OUTPUT_PATH}")
        await browser.close()  #browser instance close

#if __name__ == "__main__":
#    asyncio.run(fetch_chapter())

const puppeteer = require('puppeteer');

// const lol = scrapeFortune('http://www.fortunecookiemessage.com/');
// console.log(lol)

async function scrapeFortune(url) {
    // this first line starts the puppeteer browser
    const browser = await puppeteer.launch()
    const page = await browser.newPage();
    // this boots up page in browser
    await page.goto(url)

    // pulling out first item into el, destructuring
    const [el] = await page.$x('/html/body/div[1]/div[3]/div[1]/div[1]/a');
    const src = await el.getProperty('textContent');
    const srcTxt = await src.jsonValue();

    // console.log(el)
    browser.close();
    //console.log(srcTxt)'
    return srcTxt;
}

(async () => {
    console.log(await scrapeFortune('http://www.fortunecookiemessage.com/'))
})()

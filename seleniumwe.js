const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome'); 
async function searchGoogle() {
  const driver = await new Builder()
    .forBrowser('chrome')  
    .setChromeOptions(new chrome.Options()) 
    .build();
  
  try {
    await driver.get('https://www.google.com');
    const searchBox = await driver.findElement(By.name('q'));
    await searchBox.sendKeys('Selenium WebDriver', Key.RETURN); 
    await driver.wait(until.titleContains('Selenium WebDriver'), 10000);

    console.log('Search completed!');

  } finally {
    await driver.quit();
  }
}
searchGoogle();
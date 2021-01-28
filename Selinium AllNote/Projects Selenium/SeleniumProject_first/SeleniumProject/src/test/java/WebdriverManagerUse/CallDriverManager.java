package WebdriverManagerUse;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

public class CallDriverManager
{

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		WebDriverManager.chromedriver().setup();
		
//System.setProperty("webdriver.chrome.driver","C:\\Users\\vrshr\\workspace\\SeleniumProject\\src\\test\\resources\\chromedriver.exe");
		
		WebDriver browser = new ChromeDriver();
		
		browser.quit();
		
		//firefox, opera, chromium, internet explorer
		
		/*WebDriverManager.chromiumdriver().setup();
		WebDriverManager.firefoxdriver().setup();
		WebDriverManager.iedriver().setup();
		WebDriverManager.operadriver().setup();*/
	}

}

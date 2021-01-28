import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class StartAndOpenBrowser 
{

	public static void main(String[] args) 
	{
		//JVM - java virtual machine
		//print hello
		//print 2
		//print 3
		//call method1()
		
		System.setProperty("webdriver.chrome.driver", 
				"C:\\Users\\vrshr\\workspace\\SeleniumProject\\src\\test\\resources\\chromedriver.exe");
		
		WebDriver driver = new ChromeDriver();
		
		driver.manage().window().maximize();
		//open url
		driver.get("http://www.myntra.com");
		driver.quit();
		//u can also use driver.close() to close the current window
	}
	
	public void method1()
	{
		//code logics
	}

}


//another way to set property
		//System.setProperty("webdriver.chrome.driver", System.getProperty("user.dir")+"\\src\\test\\resources\\chromedriver.exe");
		//here, in easiest way to remember this code ---->System.getProperty("user.dir")--->   will provide the path for
		/*
		 C:\\Users\\vrshr\\workspace\\SeleniumProject --> your project that you have imported here in -->Package Explorer
		 */

from trello_navigation_management import *

def testVerificationOfTheNumberOfTheCards():

	driver = webdriver.Firefox()
	logInToTrello(driver)
	time.sleep(20)
	goToTestBoard(driver)
	time.sleep(5)
	assert countTheCardsInBoard(driver) == 2
	driver.close()

def testVerificationThatCommentsArePresent():

	driver = webdriver.Firefox()
	logInToTrello(driver)
	time.sleep(20)
	goToTestBoard(driver)
	time.sleep(5)
	assert countTheCommentsInBoard(driver) > 0
	driver.close()
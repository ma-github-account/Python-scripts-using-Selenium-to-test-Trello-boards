
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "matestaccount124@yahoo.com"
password = "DifficultTrelloPassword1234"
board_url = "https://trello.com/b/TTcLa5K7/testboard1"

def logInToTrello(driver):

	driver.get("https://trello.com/")
	driver.find_element_by_link_text("Log in").click()
	
	user_field = driver.find_element_by_id('user')
	user_field.clear()
	user_field.send_keys(user)
	password_field = driver.find_element_by_id('password')
	password_field.clear()
	password_field.send_keys(password)
	password_field.send_keys(Keys.RETURN)

	time.sleep(5)

	password_field = driver.find_element_by_id('password')
	password_field.clear()
	password_field.send_keys(password)
	login_submit_button = driver.find_element_by_id('login-submit')
	login_submit_button.send_keys(Keys.RETURN)

def goToTestBoard(driver):

	driver.get(board_url)

def countTheCardsInBoard(driver):

	count = len(driver.find_elements_by_class_name('list-card-title'))
	return count

def countTheCommentsInBoard(driver):

	count = len(driver.find_elements_by_xpath('//*[@title="Comments"]'))
	return count
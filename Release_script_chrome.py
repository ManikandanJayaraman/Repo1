import sys
import serial, string
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import lxml.html

class Releaseversion (object):
    driver = webdriver.Chrome()
    driver.get("https://acsjira-qa.honeywell.com/projects/JUEX?selectedItem=com.honeywell.softco.jira.plugin.jira-extensions-contour-integration:versions-projectpanel")
    element = driver.find_element_by_xpath("//INPUT[@id='login-form-username']").send_keys("e483203");
    element = driver.find_element_by_xpath("//INPUT[@id='login-form-password']/self::INPUT").send_keys("");
    element = driver.find_element_by_xpath("//INPUT[@id='login-form-submit']").click();
    element = driver.find_element_by_xpath("//BUTTON[@class='aui-button aui-button-subtle']/self::BUTTON").click()
    print ("open version settings")
    time.sleep(15)
    element = driver.find_element_by_xpath(".//*[@id='project-config-versions-custom-table']/tbody[1]/tr/td[3]/input[1]").send_keys("PanelSW"+"0"+"."+"6"+"."+"3");
    print ("selected version")
    element = driver.find_element_by_xpath(".//*[@id='project-config-versions-custom-table']/tbody[1]/tr/td[4]/input[1]").send_keys("Release version")
    print ("description done")
    element = driver.find_element_by_xpath(".//*[@id='project-config-version-start-date-field']").send_keys("05/JUL/17")#d/Jul/yy
    time.sleep(5)
    print ("date selected as today")
    element = driver.find_element_by_xpath(".//*[@id='project-config-version-release-date-field']").send_keys("12/Jul/17")#d/MMM/yy
    time.sleep(3)
    print ("date selected as day")
    element = driver.find_element_by_xpath(".//*[@id='contour-project-lozenge-newrecord-multi-select']/span").click().send_keys(Keys.ENTER)
    time.sleep(4)
    print ("jama project selected")
    element = driver.find_element_by_xpath(".//*[@id='project-config-versions-custom-table']/tbody[1]/tr/td[9]/input").click()
    print ("Project added")


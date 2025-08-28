import re
import time
from collections import Counter

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from unicodedata import digit
from webdriver_manager.chrome import ChromeDriverManager


class newprograms:
    def launch_driver(self):
        options = Options()

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver = webdriver.Chrome(options=options)
        driver.get("https://www.google.com")
        print(driver.title)

        driver.find_element(By.NAME, 'q').send_keys("Naveen automation labs")
        time.sleep(2)
        promptoptions = driver.find_elements(By.XPATH, "(//ul[@role='listbox'])[1]/li")
        print(len(promptoptions))
        for eachoption in promptoptions:
            print(eachoption.text)
            if eachoption.text == 'naveen automationlabs youtube':
                eachoption.click()

        time.sleep(5)
        driver.quit()

    def copy_duplicates_to_set(self):
        name = "Jyothi sanapala"
        #print(name[0:3])
        nameset = set()
        duplicateset = set()
        for char in name:
            #     if nameset.add(char):
            #         print("nameset")
            #     else:
            #         duplicateset.add(char)
            #
            # print('kiki')
            # print("duplicateset")
            if char in nameset:
                duplicateset.add(char)
            else:
                nameset.add(char)
        print("duplicateset" + str(duplicateset))
        print("uniqueset" + str(nameset))

    def character_occurence(self, name):
        count_char = Counter(name)
        print(count_char)

    def keep_digits_insameplace_and_reversestring(self):
        extractstring = "12hkjfhsfjghsf4 @5jgdfnjkgnj78"
        print("splitted string", extractstring.split())
        outputstring = " "
        letters = (c for c in extractstring if extractstring.isalpha())
        for c in extractstring:
            if c.isalpha():
                print(extractstring.strip())
            #  outputstring+=letters.pop(0)
            #else:
            #   outputstring+=char
        print(outputstring)

    def get_substring_inmainstring(self):
        substring = "auto"
        main = "selenium 12automation45"
        i = main.find(substring)
        l = len(substring)
        li = ()
        for char in main:
            if char is digit:
                print(char)

    def extract_digits_from_string(self):
        extractstring = "12hkjfhsfjghsf4 @5jgdfnjkgnj78"
        extractedvalues = re.findall(r"\d+", extractstring)
        print(extractedvalues)

    def reverse_only_wordsofthe_string(self):
        text="Hi, How are you doing?"
        print(text + " → reverse only words")
        li = text.split()       # Split text into words
        for word in li:
            print("".join(word[::-1])) # slicing reverses string
            print(li)
newprograms().reverse_only_wordsofthe_string()

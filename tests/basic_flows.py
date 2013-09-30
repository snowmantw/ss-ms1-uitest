#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver

class TestBasicFlows(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.siteurl = "http://demo.socialstudy.tw"
        self.driver.get(self.siteurl)

    def tearDown(self):
        self.driver.close()

    def test_entryMain(self):
        btn = self.driver.find_element_by_css_selector(".btn.btn-primary.btn-large")
        assert u"按這裡開始吧！" == btn.text, "Can't find the entry button."

    def test_coursesPage(self):
        btn = self.driver.find_element_by_css_selector(".btn.btn-primary.btn-large")
        btn.click()
        self.driver.implicitly_wait(3)
        assert "%s/courses/" % self.siteurl == self.driver.current_url, "Can't navigate to the course page."

    def test_courseRow(self):
        btn = self.driver.find_element_by_css_selector(".btn.btn-primary.btn-large")
        btn.click()
        self.driver.implicitly_wait(3)
        for idx in range(1,5):
            # Select each time to prevent Stale element issue.
            row = self.driver.find_elements_by_css_selector("table.course-table tbody tr")[idx]
            row.click()
            self.driver.implicitly_wait(3)
            wells = self.driver.find_elements_by_css_selector(".well")
            assert 0 < len(wells), "Can't navigate to the right course page."
            self.driver.back()
            self.driver.implicitly_wait(3)
        assert "%s/courses/" % self.siteurl == self.driver.current_url, "Can't come back to the course page."

if __name__ == "__main__":
      unittest.main()

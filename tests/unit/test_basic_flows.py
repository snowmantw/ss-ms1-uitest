#!/usr/bin/python
# -*- coding: utf-8 -*-

from marionette_test import MarionetteTestCase
from marionette import Actions

class TestBasicFlows(MarionetteTestCase):

    def setUp(self):
        # code to execute before any tests are run
        MarionetteTestCase.setUp(self)
        self.siteurl = "http://socialstudy.tw/"
        self.site = self.marionette.navigate(self.siteurl)

    def tearDown(self):
        # code to execute after all tests are run
        MarionetteTestCase.tearDown(self)

    def test_entryMain(self):
        btn = self.marionette.find_element('css selector', ".btn.btn-primary.btn-large")
        self.assertEqual(u"按這裡開始吧！", btn.text)

        self.marionette.navigate(self.siteurl)

    def test_coursesPage(self): 
        btn = self.marionette.find_element('css selector', ".btn.btn-primary.btn-large")
        Actions(self.marionette).tap(btn).wait(3).perform()
        self.assertEqual("http://socialstudy.tw/courses/",
            self.marionette.get_url(), "Can't navigate to the course page.")

        self.marionette.navigate(self.siteurl)

    def test_courseRow(self): 
        btn = self.marionette.find_element('css selector', ".btn.btn-primary.btn-large")
        Actions(self.marionette).tap(btn).wait(3).perform()
        rows = self.marionette.find_elements('css selector', "table.course-table tbody tr")
        assert 0 < len(rows), "Can't get any course data row on the courses page."
        for row in rows[0:5]:
            Actions(self.marionette).tap(row).wait(3).perform()
            wells = self.marionette.find_elements('css selector', ".well")
            assert 0 < len(wells), "Can't navigate to the right course page."
            self.marionette.go_back()
            self.marionette.set_search_timeout('3000')
        self.assertEqual("http://socialstudy.tw/courses/",
            self.marionette.get_url(), "Can't go back to the course page.")

        self.marionette.navigate(self.siteurl)

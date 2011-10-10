import unittest
from matem.policy.tests.base import MatemPolicyTestCase

class TestSetup(MatemPolicyTestCase):

    def test_portal_title(self):
        self.assertEquals("Institute of Mathematics",
            self.portal.getProperty('title'))

    def test_portal_description(self):
        self.assertEquals("Welcome to Institute of Mathematics",
            self.portal.getProperty('description'))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
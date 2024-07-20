import unittest
from test_email_inbox import TestInbox

suite = unittest.TestLoader().loadTestsFromTestCase(TestInbox)
unittest.TextTestRunner().run(suite)
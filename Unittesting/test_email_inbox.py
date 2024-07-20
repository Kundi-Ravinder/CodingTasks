import unittest
from email_inbox import Email, Inbox

class  TestInbox(unittest.TestCase):
    def setUp(self):
    
        self.email1=Email('ggr@gmail.com','Welcome to HyperionDev!','Welcome')
        self.email2=Email('mr@gmail.com','Great work on Bootcamp',' Well done !')
        self.email2.mark_as_read()
        self.inbox = Inbox()

    def test_create_email(self):
        self.assertEqual(self.email1.email_address,'ggr@gmail.com')
        self.assertEqual(self.email1.subject_line,'Welcome to HyperionDev!')
        self.assertEqual(self.email1.email_content,'Welcome')
        self.assertFalse(self.email1.has_been_read)
    
    def test_mark_as_read(self):
        self.email1.mark_as_read()
        self.assertTrue(self.email1.has_been_read)
        
        
    def test_mark_as_unread(self):
        self.email2.mark_unread()
        self.assertFalse(self.email2.has_been_read)
             
    def test_populate_inbox(self):
        # object variable for populate the email in inbox
        new_email= Email('mm@hotmail.com','work hard','Need to do more work')
        self.inbox.populate_inbox(new_email)
        # Checking email inbox equal to list
        self.assertListEqual(self.inbox.inbox,[new_email])

                
    def test_list_read_emails(self):
        email1=Email('ggr@gmail.com','Welcome to HyperionDev!','Welcome')
        email2=Email('mr@gmail.com','Great work on Bootcamp',' Well done !')
        self.inbox.populate_inbox(email1)
        self.inbox.populate_inbox(email2)
        print("\n ______________Read email_____________")
        # Mark email as read
        self.inbox.read_email(0)
        # Return the list of the read email
        read = self.inbox.list_read_emails()
        
        self.assertEqual(read, [[0, email1]])
         
    def test_list_unread_emails(self):
        email1=Email('ggr@gmail.com','Welcome to HyperionDev!','Welcome')
        email2=Email('mr@gmail.com','Great work on Bootcamp',' Well done !')
        self.inbox.populate_inbox(email1)
        self.inbox.populate_inbox(email2)
        
        print("\n ______________Unread email_____________")
        # mark email as unread
        self.inbox.read_email(0)
        #return the list of the unread email
        unread = self.inbox.list_unread_emails()
        self.assertEqual(unread, [[1, email2]])
        

if __name__== "__main__":
    unittest.main()

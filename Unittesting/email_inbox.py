
#  Created Email class 
class Email:
    # Constructor method with instance email_address, subject_line, email_contact
    def __init__(self, email_address,subject_line,email_content) :
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    
    # Magic method __repr__ return the reprentation of the instance object
    def __repr__(self):
        string = self.subject_line 
        return string

    # Mark_as_read set and return the True value to has_been_read
    def mark_as_read(self):
        self.has_been_read = True
        return True
    
    # Mark_unread set and return the Falsa value to has_been_read
    def mark_unread(self):
        self.has_been_read = False
        return  False

    
class Inbox:
    
    def __init__(self):
        self.inbox = []
    
    # List of emails enumerate the count, value for inbox
    def list_emails(self):
        for count , value in enumerate(self.inbox):
            print(count, value) # Output: 1 Great work on Bootcamp 
            
    # Populate_inbox add emails into the inbox
    def populate_inbox(self, email):
        # Append in the inbox list
        self.inbox.append(email)
        return email
    
    # Check the index email has read
    def check_read(self, index):
        read = self.inbox[index].has_been_read
        return read
    
    # Function read_email takes 1 parameter as index number for inbox and make as read email
    def read_email(self,index):
        return self.inbox[index].mark_as_read()

    # Function unread_email takes 1 parameter as index number for inbox and make as read email
    def unread_email(self,index):
        return self.inbox[index].mark_unread()
    
    # Funtion return list of read email from inbox
    def list_read_emails(self):
        read = []
        for count, value in enumerate(self.inbox):
            if self.inbox[count].has_been_read:
                read.append([count, value])
                print(count, value)
        return read
                
    # Funtion return list of unread email from inbox           
    def list_unread_emails(self):
        unread = []
        for count, value in enumerate(self.inbox):
            if not self.inbox[count].has_been_read:
                unread.append([count, value])
                print(count, value)
        return unread

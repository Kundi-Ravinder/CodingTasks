from django.test import TestCase
from django.urls import reverse
from .models import Notes

""" Testing on Notes Create,Read, Update, Delete
    functionality is working as expected 
    Read and delete data from database with Get request
    Create and update with post request
    
    """
# Sticky_Notes tests here.
class NotesTest(TestCase):
    
    def setUp(self):
        Notes.objects.create(title= "Test for Note",
                             description = "Testing for description",
                             is_complete=False,
                             created_by = "Tester R")
        
        
    def test_note_create_has_tittle(self):
        # Checking create has add title  to data
        note = Notes.objects.get(id=1)
        self.assertTrue(note.title,"Test for Note")
        
    def test_note_create_has_description(self):
        # Checking Create has add description to data
        note = Notes.objects.get(id=1)
        self.assertTrue(note.description,"Testing for description")
        
    def test_note_create_is_complete_false(self):
        # checking on is_complete is equal to  False
        note = Notes.objects.get(id=1)
        self.assertFalse(note.is_complete,False)
        
    def test_note_create_is_complete_true(self):
        # Updating and checking is_complete as True
        note= Notes.objects.get(id=1)
        note.is_complete = True
        self.assertTrue(note.is_complete)
        
    def test_note_create_created_by(self):
        # Test on note created_by 
        note = Notes.objects.get(id=1)
        self.assertTrue(note.created_by,"Tester R")
        
        
class NotesViewTest(TestCase):
    def setUp(self):
        Notes.objects.create(title= "View Test",
                             description = "View Test is working as expected",
                             is_complete=True,
                             created_by = "Ruby")

    def test_get_all_returns_correct_notes_values(self):
        # Get all notes values return
        response = self.client.get(reverse('notes'))
        print("Response code is :",response.status_code)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"View Test")
        
        
    def test_get_returns_correct_note_values(self):
        # Get note is equal to id value
        note = Notes.objects.get(id=1)
        response = self.client.get(reverse('note',args=[note.pk]))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"View Test")
        
        
    def test_post_create_note_to_database(self):
        start_counter= Notes.objects.count()
        response = self.client.post(reverse('create_note'),{
            'title': 'Test New Note',
            'description': 'New note in database',
            'is_complete':False,
            'created_by' : 'Tester'
        })
        
        now_count=Notes.objects.count()
        self.assertEqual(response.status_code,302)
        print("Response code is :",response.status_code)
        self.assertNotEqual(start_counter,now_count)
             
   
    def test_post_update_note_title(self):
        # change the title to check update functionality
        note = Notes.objects.get(id=1)
        self.assertTrue(note.title,"View Test")
        note.title= "Update Test title"
        self.assertEqual(note.title,"Update Test title")
        
        
    def test_delete_note(self):
        # change the title to check update functionality
        note = Notes.objects.get(id=1)
        response = self.client.get(reverse('delete_note',args=[note.pk]))
        self.assertNotEqual(response.status_code,200)

        
        
        
    
        
        
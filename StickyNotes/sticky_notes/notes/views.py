from django.shortcuts import (
    render,
    redirect, 
    get_list_or_404,
    get_object_or_404)
from .models import Notes
from .forms import NotesForm

"""
Create function to call POST request
for Notesform to add new note and save

"""
def create(request):
    
    if request.method == 'POST':
        form = NotesForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('notes')
    else:
            form = NotesForm()
    
    context = {'form': form,
               'page_title': 'Creating New Note:'}
    
    return render(request,'notes_form.html',context=context)


""" 
Get_all function request to 
fetch all the  object as notes
return the objects display on all_notes html page
"""      
def get_all(request):
 
    notes = Notes.objects.all()
    
    context = {
        'notes': notes,
        'page_title' : 'All Notes'
    }   
    return render(request,'all_notes.html', context=context)


"""
Get function will send the GET request Notes
object is equal to pk=primarykey
or throw 404 status code error
return the object display on notes.html page
    
"""
def get(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    context = {
        'note': note
    }
    print(request.GET)
    return render(request, 'notes.html', context=context)


""" Update function  GET request to fetch the Notes 
    object is equal to pk=primarykey
    if object is found return the notes form
    Post request will save the update note 
"""
def update(request, pk):
    note = get_object_or_404(Notes, pk = pk)
    print(pk)
    if request.method == "POST": 
        form = NotesForm(request.POST, instance=note)

        if form.is_valid():
            note = form.save(commit = False)
            note.save()
            return redirect('notes')
    else:
            form = NotesForm(instance=note)
    
    context = {
        'form':form,
        'note':note,
        'page_title': 'Editting Note:'
    }
          
    return render(request,'notes_form.html', context=context)
    
""" Delete function request to fetch the Notes
    oject is equal to pk=primarykey
    or 404 status-code
    will delete the note 
    
"""    
def delete(request, pk):
    note = get_object_or_404(Notes, pk = pk)
    note.delete()
    return redirect('notes')
from django.shortcuts import render, redirect, get_list_or_404
from todoApp.models import Todo 
from todoApp.forms import TodoForm
from todoApp.forms import TodoSearchForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils.translation import gettext as _

def todo_list(request):
    sform = TodoSearchForm(request.GET)
    page = request.GET.get('page')
    
    todos = Todo.objects.all().order_by('-created_at')

    # if sform.is_valid():
    #     search_query = sform.cleaned_data['search_query']
    #     if search_query:
    #         todos = todos.filter(title__icontains=search_query)            

    paginator = Paginator(todos,4)
    todos = paginator.get_page(page)
    
    return render(request, 'todoApp/todo_list.html',{'todos':todos})

def todo_detail(request, pk):
    # todo = get_list_or_404(Todo, pk=pk)
    todo = Todo.objects.get(id=pk)
    return render(request, 'todoApp/todo_detail.html',{'todo':todo})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,_('Task created successfully.'))
            return redirect('todo_list')
        else:
            print("VALidation error")
    else:
        form = TodoForm()
    # return render(request, 'todoApp/todo_form.html', {'form':form})
    return render(request, 'todoApp/todo_form.html', {'form':form})

def todo_update(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        messages.error(request, _('Task not found.'))
        return redirect('todo_list')
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, _('Task updated successfully.'))
            return redirect('todo_list')
        else:
            messages.error(request, _('Task update failed. Please check the form.'))
    else:
        form = TodoForm(instance=todo)
        
    # return render(request,'todoApp/todo_form.html',{'form':form}) 
    return render(request,'todoApp/todo_form.html',{'form':form, 'todo':todo}) 

def todo_delete(request, pk):
    # todo = get_list_or_404(Todo, pk=pk)
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        messages.error(request,_('Task not found.'))
        return redirect('todo_list')
    
    if request.method == 'POST':
        todo.delete()   
        messages.success(request,_('Task delete successfully.'))
    return redirect('todo_list')
        # return render(request, 'todoApp/todo_confirm_delete.html',{'todo':todo})

def todo_update_status(request, pk):
    # todo = get_list_or_404(Todo, pk=pk)
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        messages.error(request,_('Task not found.'))
        return redirect('todo_list')
    print("todo:",todo)
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        print("woeking m", new_status)
        if new_status in [choice[0] for choice in Todo.STATUS_CHOICES]:
            todo.status = new_status
            todo.save()
            print("working n")
            messages.success(request, _('Status updated successfully.'))
        print("working")
    return redirect('todo_list')

def todo_search(request):
    query = request.GET.get('q')
    todos = Todo.objects.all().order_by('-created_at')

    if query:
        todos = Todo.objects.filter(title__icontains=query)

    page = request.GET.get('page')
    paginator = Paginator(todos,4)
    todos = paginator.get_page(page)
    print(todos)
    return render(request, 'todoApp/todo_list.html',{'todos':todos, 'query':query })


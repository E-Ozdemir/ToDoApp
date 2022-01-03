from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoAddForm, TodoUpdateForm


def home(request):
    return render(request, "todo/home.html")


def todo_list(request):
    todos = Todo.objects.all()#Model de olusturdugumuz Todo tablosunu cagirip bir degiskene atiyoruz.
    form = TodoAddForm()
    if request.method == "POST":
        form = TodoAddForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'todos' : todos,
        'form' : form,
    }
    return render(request, "todo/todo_list.html", context)


def todo_add(request):
    form = TodoAddForm() #Kullaniciya bos form gönderiyoruz.
    if request.method == "POST":
        form = TodoAddForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form': form,
    }
    return render(request, "todo/todo_add.html", context)


def todo_update(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)# Todo tablosundan objeyi cek gelmiyosa 404 ver.
    form = TodoUpdateForm(instance=todo)# instance bir objedir, db den cagirdigim update islemi icin forma yerlestirilmesi gereken data.
    if request.method == "POST":
        print(request.POST)
        form = TodoUpdateForm(request.POST, instance=todo)#update edilmeyenler instance daki veriler olsun, update dilenler request post ile gelen veriler olur.cd
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form' : form,
        'todo' : todo,
    }
    
    return render(request, "todo/todo_update.html", context)

    
def todo_delete(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        todo.delete()
        return redirect("list")
    
    context = {
        "todo" : todo,
    }
    return render(request, "todo/todo_delete.html", context)

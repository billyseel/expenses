from django.shortcuts import render, redirect

# Create your views here.
from . models import Expenses
from . forms import ExpenseModelForm


def index(request):

    expenses = Expenses.objects.all()
# this expenese was imported form models
    form = ExpenseModelForm()

    if request.method == "POST":
        # this for was imported from forms.py
        form = ExpenseModelForm(data=request.POST)
        # here request date and after write it with post command... we could not write data=request.
        # but did that to know that we are getting data and later write something
        if form.is_valid:
            form.save()
        return redirect("/expenses")
        # tabove line unecessary cos at the bottom we have return render which will take us to the index

    context = {
        'expenses': expenses,
        'form': form
    }
    return render(request, 'index.html', context)


def update(request, pk):
    expense = Expenses.objects.get(id=pk)

    form = ExpenseModelForm(instance=expense)
    # instance means to get something from database. here we get something and put in forms
    if request.method == 'POST':
        form = ExpenseModelForm(request.POST, instance=expense)
        # with post we write something and and put in the form. this form can have any name because its a
        # new variable name. not the same as the above form.
        if form.is_valid():
            form.save()
        return redirect('/expenses')

    context = {
        'form': form,
        'expense': expense
    }
    # the above form is necessary to be able to create a form on update.html please note the {{form}}
    return render(request, 'update.html', context)
    # the return context here is the above form and expense.


def delete(request, pk):
    expense = Expenses.objects.get(id=pk)

    # form = ExpenseModelForm(instance=expense)

    if request.method == 'POST':
        expense.delete()
        return redirect('/expenses')

    context = {
        # 'form': form,
        'expense': expense
    }

    return render(request, 'delete.html', context)
    # context must be a dictionary type. we could also use locals() which would include all data.
    # delete does not require to have a form. reason why i comment on form.

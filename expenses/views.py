from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from .models import Expense,Category
from .forms import ExpenseForm,CategoryForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

# ------------------------
# User Registration View
# ------------------------

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(
                request,"Registration successfull! Welcome."
            )
            return redirect("expense_list")
        else:
            messages.error(
                request,"Registration failed.Please correct the errors below."
            )

    else:
        form = UserCreationForm()
    
    return render(request,"expenses/register.html",{"form":form})

# -------------------
# User Login View
# -------------------

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(
            request,data=request.POST
        )
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request,username=username,password=password
            )

            if user is not None:
                login(request,user)
                messages.success(
                    request,f"Welcome back, {user.username}!"
                )
                return redirect("expense_list")
            else:
                messages.error(
                    request,"Invalid username or password."
                )
        else:
            messages.error(
                request,form.non_field_errors()
            )
    else:
        form = AuthenticationForm()

    return render(request,"expenses/login.html",{"form":form})

# -------------------
# User Logout View
# -------------------
def logout_view(request):
    """
    Log the user out and redirect to the login page with a success message.
    """
    logout(request)  # Log the user out
    messages.success(request, "You have been logged out.")  # Success message
    return redirect("login")  # Redirect to login page


# -------------------
# Expense List View
# -------------------
@login_required
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request,"expenses/expense_list.html",{"expenses":expenses})

# -------------------
# Expense Create View
# -------------------
@login_required
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            messages.success(request,"Expense created successfully!")
            return redirect("expense_list")
        else:
            messages.error(
                request,"Failed to create Expense. Please fix the errors below."
            )
    else:
        form = ExpenseForm()    
    
    return render(request,"expenses/expense_form.html",{"form":form})

# -------------------
# Expense Update View
# -------------------
@login_required
def expense_update(request,pk):
    expense = get_object_or_404(Expense,pk=pk)
    if request.method == "POST":
        form = ExpenseForm(
            request.POST, instance=expense
        )
        if form.is_valid():
            form.save()
            messages.success(request,"Expense updated successfully!")
            return redirect("expense_list")
        else:
            messages.error(
                request,"Failed to update task. Please fix the errors below."
            )
    else:
        form = ExpenseForm(instance=expense)

    return render(request,"expenses/expense_form.html",{"form":form})

# -------------------
# Expense Delete View
# -------------------
@login_required
def expense_delete(request,pk):
    expense = get_object_or_404(Expense,pk=pk)
    if request.method == "POST":
        expense.delete()
        messages.success(request,"Expense deleted successfully!")
        return redirect("expense_list")
    
    return render(request,"expenses/expense_confirm_delete.html",{"expense":expense})


# ---------------------
# Expense Detail View
# ---------------------
@login_required
def expense_detail(request,pk):
    expense = get_object_or_404(Expense,pk=pk)

    return render(
        request,"expenses/expense_details.html",{"expense":expense}
    )


# ---------------------
# Category List View
# ---------------------
@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request,"expenses/category_list.html",{"categories":categories})

# -------------------
# Category Create View
# -------------------
@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request,"Category created successfully!")
            return redirect("category_list")
        else:
            messages.error(
                request,"Failed to create Expense. Please fix the errors below."
            )
    else:
        form = CategoryForm()    
    
    return render(request,"expenses/category_form.html",{"form":form})

# -------------------
# Category Update View
# -------------------
@login_required
def category_update(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        form = CategoryForm(
            request.POST, instance=category
        )
        if form.is_valid():
            form.save()
            messages.success(request,"Category updated successfully!")
            return redirect("category_list")
        else:
            messages.error(
                request,"Failed to update category. Please fix the errors below."
            )
    else:
        form = CategoryForm(instance=category)

    return render(request,"expenses/category_form.html",{"form":form})

# -------------------
# Category Delete View
# -------------------
@login_required
def category_delete(request,pk):
    category = get_object_or_404(Expense,pk=pk)
    if request.method == "POST":
        category.delete()
        messages.success(request,"Expense deleted successfully!")
        return redirect("category_list")
    
    return render(request,"expenses/category_confirm_delete.html",{"category":category})


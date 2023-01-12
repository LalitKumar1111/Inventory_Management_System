from django.shortcuts import render, redirect,HttpResponseRedirect

from .forms import *

# Supplier views
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            email = forms.cleaned_data['email']
            mobile = forms.cleaned_data['mobile']
            address = forms.cleaned_data['address']
            reg = Supplier(name=name, email=email, mobile=mobile, address=address)
            reg.save()
            forms = SupplierForm()
            return redirect('supplier-list')
    else:
        forms = SupplierForm()

    return render(request, 'store/create_supplier.html', {'form': forms})

# Supplier search & views
def SupplierListView(request):
    if request.method== 'POST':
        email= request.POST.get('email')
        se=Supplier.objects.filter(email__contains=email)
        return render(request,'store/search_supplier.html',{'email':email,'se':se})
    s=Supplier.objects.all()
    return render(request, 'store/supplier_list.html',{'supplier':s})

# Edit supplier
def edit_supplier (request, id):
    if request.method == 'POST':
        pi=Supplier.objects.get(pk=id)
        fm=SupplierForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('/store/supplier-list/')
    else:
        pi=Supplier.objects.get(pk=id)
        fm=SupplierForm(instance=pi)
    return render(request,'store/edit_supplier.html', {'form': fm })
#Delete supplier
def delete_supplier(request, id):
    if request.method == 'POST':
        pi = Users.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# DEPARTMENT
# Department views
def create_department(request):
    forms = DepartmentForm()
    if request.method == 'POST':
        forms = DepartmentForm(request.POST)
        if forms.is_valid():
            deptname = forms.cleaned_data['deptname']
            email = forms.cleaned_data['email']
            mobile = forms.cleaned_data['mobile']
            address = forms.cleaned_data['address']
            reg = Dept(deptname=deptname, email=email, mobile=mobile, address=address)
            reg.save()
            forms = DepartmentForm()
            return redirect('department-list')
    else:
        forms = DepartmentForm()

    context = {
                'form': forms
            }
    return render(request, 'store/create_department.html', context)

# Department search & views
def DepartmentListView(request):
    s=Dept.objects.all()
    return render(request, 'store/department_list.html',{'Department':s})

# Edit Department
def edit_department (request, id):
    if request.method == 'POST':
        pi=Dept.objects.get(pk=id)
        fm=DepartmentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('department-list')
    else:
        pi=Dept.objects.get(pk=id)
        fm=DepartmentForm(instance=pi)
    return render(request,'store/edit_department.html', {'form': fm })

#Delete department
def delete_department(request, id):
    if request.method == 'POST':
        pi = Dept.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/store/department-list/')




# Category
# Create category
# @login_required(login_url='login')
def create_category(request):

    if request.method== 'POST':
        if request.POST.get('catname'):
            c=Category()
            c.catname = request.POST.get('catname')
            c.catdetails = request.POST.get('catdetails')
            c.save()
            return render(request,'store/create_category.html')
        if request.POST.get('uname'):
            u=Unit()
            u.uname = request.POST.get('uname')
            u.save()
            return render(request,'store/create_category.html')
    return render(request, 'store/create_category.html')


# category views
# @login_required(login_url='login')
def CategoryListView(request):
    c=Category.objects.all()
    u= Unit.objects.all()
    return render(request, 'store/category_list.html',{'category':c,'unit':u})


#Edit category
def edit_category(request, id):
    if request.method== 'POST':
        pi2=Category.objects.get(pk=id)
        fm2=CategoryForm(request.POST, instance=pi2)
        if fm2.is_valid():
            fm2.save()
        return redirect('category-list')
    else:
        pi2=Category.objects.get(pk=id)
        fm2=CategoryForm(instance=pi2)
    return render(request,'store/edit_category.html', {'form2': fm2 })

# Delete Category
def delete_category(request, id):
    if request.method == 'POST':
        pi = Category.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/store/category-list/')


#Edit unit
def edit_unit(request, id):
    if request.method== 'POST':
        pi3=Unit.objects.get(pk=id)
        fm3=UnitForm(request.POST, instance=pi3)
        if fm3.is_valid():
            fm3.save()
        return redirect('category-list')
    else:
        pi3=Unit.objects.get(pk=id)
        fm3=UnitForm(instance=pi3)
    return render(request,'store/edit_unit.html', {'form3': fm3 })

# Delete unit
def delete_unit(request, id):
    if request.method == 'POST':
        pi = Unit.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/store/category-list/')


# Product
# Product create
# @login_required(login_url='login')

def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            forms = ProductForm()
            return redirect('product-list')
    else:
        forms = ProductForm()
    return render(request, 'store/create_product.html', {'form': forms})






# Product views
# @login_required(login_url='login')
def ProductListView(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        se=Product.objects.filter(name__contains=name)
        cato=Category.objects.all()
        return render(request,'store/search_product.html',{'name':name,'se':se,'cat':cato})

    p=Product.objects.all()
    return render(request, 'store/product_list.html',{'product':p})


# Edit Product
def edit_product (request, id):
    if request.method== 'POST':
        pi=Product.objects.get(pk=id)
        fm=ProductForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('product-list')
    else:
        pi=Product.objects.get(pk=id)
        fm=ProductForm(instance=pi)
    return render(request,'store/edit_product.html', {'form': fm })




# Delete product
def delete_product(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/store/product-list/')




# PO
# Po create
# @login_required(login_url='login')
def create_po(request):
    forms = POForm()
    if request.method == 'POST':
        forms = POForm(request.POST)
        if forms.is_valid():
            forms.save()
            forms = POForm()
            return redirect('po-list')
    else:
        forms = POForm()
    p=PO.objects.all()
    return render(request, 'store/create_po.html', {'form': forms, 'po':p})

# Po search & views
# @login_required(login_url='login')
def PoListView(request):
    if request.method== 'POST':
        ponum=request.POST.get('ponum')
        se=PO.objects.filter(ponum__contains=ponum)
        return render(request,'store/search_po.html',{'ponum':ponum,'se':se})

    p=PO.objects.all()
    return render(request, 'store/po_list.html',{'po':p})


# Edit PO
def edit_po(request, id):
    if request.method== 'POST':
        pi=PO.objects.get(pk=id)
        fm=POForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('po-list')
    else:
        pi=PO.objects.get(pk=id)
        fm=POForm(instance=pi)
    return render(request,'store/edit_po.html', {'form': fm })

#delete PO
def delete_po(request,id):
    if request.method == 'POST':
        pi=PO.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/store/create-po/')



# USER
# User views
# @login_required(login_url='login')

def create_user(request):
    forms = UserForm()
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            forms = UserForm()
            return redirect('user-list')
    else:
        forms = UserForm()
    return render(request, 'store/create_user.html', {'form': forms})



# User search & views
# @login_required(login_url='login')
def UserListView(request):
    if request.method== 'POST':
        email = request.POST.get('email')
        se=Users.objects.filter(email__contains=email)
        return render(request,'store/search_user.html',{'email':email,'se':se})
    u= Users.objects.all()
    return render(request, 'store/user_list.html',{'us':u})


# Edit User
def edit_user(request, id):
    if request.method== 'POST':
        pi=Users.objects.get(pk=id)
        fm=UserForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('user-list')
    else:
        pi=Users.objects.get(pk=id)
        fm=UserForm(instance=pi)
    return render(request,'store/edit_user.html', {'form': fm })


# Delete user
def delete_user(request, id):
    if request.method == 'POST':
        pi = Users.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/store/user-list/')


#SO
# So create
# @login_required(login_url='login')


def create_so(request):
    forms = SOForm()
    if request.method == 'POST':
        forms = SOForm(request.POST)
        if forms.is_valid():
            forms.save()
            forms = SOForm()
            return redirect('so-list')
    else:
        forms = SOForm()
    s=SO.objects.all()
    return render(request, 'store/create_so.html', {'form': forms, 'so':s})


# So views
# @login_required(login_url='login')
def SoListView(request):
    if request.method== 'POST':
        sonum=request.POST.get('sonum')
        se=SO.objects.filter(sonum__contains=sonum)
        return render(request,'store/search_so.html',{'sonum':sonum,'se':se})

    s=SO.objects.all()
    return render(request, 'store/so_list.html',{'so':s})


# Edit SO
def edit_so(request, id):
    if request.method== 'POST':
        pi=SO.objects.get(pk=id)
        fm=SOForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('so-list')
    else:
        pi=SO.objects.get(pk=id)
        fm=SOForm(instance=pi)
    return render(request,'store/edit_so.html', {'form': fm })

#delete so
def delete_so(request,id):
    if request.method == 'POST':
        pi=SO.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/store/create-so/')

from django.shortcuts import render, redirect
from .forms import CategoryForm, SubCategoryForm
from .models import Category, SubCategory
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
import openpyxl
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


def view_category(request):
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    return render(request, 'category_app/category_list.html', {
        'categories': category_list, 'sub_categories': sub_category_list})


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.created_date = timezone.now()
            cat.save()
            return redirect('view_category')
    else:
        form = CategoryForm()
    return render(request, 'category_app/category_from.html', {'form': form})


def create_sub_category(request):
    if request.method == "POST":
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            sub_cat = form.save(commit=False)
            sub_cat.created_date = timezone.now()
            sub_cat.save()
            return redirect('view_category')
    else:
        form = SubCategoryForm()
    return render(request, 'category_app/sub_category_from.html', {'form': form})


def insert_excel(request):
    if request.method == 'POST' and request.FILES['myfile']:
        try:
            excel_file = request.FILES['myfile']
            if (str(excel_file).split('.')[-1] in ["xls", "xlsx"]):
                data = openpyxl.load_workbook(excel_file)
                worksheet = data["Sheet1"]
                keys = None
                for c, row in enumerate(worksheet.iter_rows()):
                    if c == 0:
                        keys = [i.value for i in row]
                    elif c == 1:
                        values = [i.value for i in row]
                        dict = {key: value for key, value in zip(keys, values)}
                        cat_obj = Category()
                        cat_obj.categories = dict.get('categories')
                        cat_obj.created_date = timezone.now()
                        cat_obj.save()
                return redirect('view_category')
            else:
                return render(request, 'category_app/excel.html', {'msg': "upload excel file"})
        except MultiValueDictKeyError:
            return redirect('view_category')
    return render(request, 'category_app/excel.html')



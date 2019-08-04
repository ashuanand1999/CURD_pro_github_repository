from django.shortcuts import render
from.forms import CreateForm,UpdateForm,DeleteForm
from.models import ProductData
from django.http.response import HttpResponse

def home_view(request):
    return render(request,'curd_home.html')

def create_view(request):
    if request.method == "POST":
        cform = CreateForm(request.POST)
        if cform.is_valid():
            product_id = request.POST.get('product_id', '')
            product_name = request.POST.get('product_name', '')
            product_color = request.POST.get('product_color', '')
            product_cost = request.POST.get('product_cost', '')
            product_class = request.POST.get('product_class', '')
            customer_name = request.POST.get('customer_name', '')
            customer_mobile = request.POST.get('customer_mobile', '')
            customer_email = request.POST.get('customer_email', '')
            data = ProductData(
                product_id=product_id,
                product_name=product_name,
                product_color=product_color,
                product_cost=product_cost,
                product_class=product_class,
                customer_name=customer_name,
                customer_mobile=customer_mobile,
                customer_email=customer_email
            )
            data.save()
            cform = CreateForm()
            return render(request,'curd_insertingform.html',{'cform': cform})
        else:
            return HttpResponse("<h1>invalid form please give data to all fields</h1>")
    else:
        cform = CreateForm()
        return render(request,'curd_insertingform.html',{'cform': cform})

def update_view(request):
    if request.method == "POST":
        uform = UpdateForm(request.POST)
        if uform.is_valid():
            product_id = request.POST.get('product_id','')
            product_cost = request.POST.get('product_cost','')

# Here i am taking product id from user that value stored inside product_id and now i am comparing
# comparing that value with the available product id from database which is stored earlier and
# that value is again stored inside the pid variable and if pid is matched  than do the update
#  the cost and again show the empty form otherwise return response that it is not available.

            pid = ProductData.objects.filter(product_id=product_id)

            if not pid:
                return HttpResponse("<h1>Product Id is not available</h1>")
            else:
                pid.update(product_cost=product_cost)
                uform = UpdateForm()
                return render(request,'curd_updatingform.html',{'uform': uform})
        else:
            return HttpResponse("<h1>inavalid form please give data to all fields</h1>")
    else:
        uform = UpdateForm()
        return render(request,'curd_updatingform.html',{'uform': uform})

def retrieve_view(request):
    product_data = ProductData.objects.all()
    return render(request,'curd_retrievingform.html',{'pdata': product_data})

def delete_view(request):
    if request.method == "POST":
        dfrom = DeleteForm(request.POST)
        if dfrom.is_valid():
# Again before deleting the data 1st we are taking the product_id from the user and than that id we
# compare with the saved database recored if that record is matched than only we delete that data
            product_id = request.POST.get('product_id','')
            pid = ProductData.objects.filter(product_id=product_id)
            if not pid:
                return HttpResponse("<h1>Sorry the given product_id is not available.</h1>")
            else:
                pid.delete()
                dfrom = DeleteForm()
                return render(request,'curd_deletingform.html',{'dform': dfrom})
    else:
        dfrom = DeleteForm()
        return render(request,'curd_deletingform.html',{'dform':dfrom})







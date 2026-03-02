from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Order
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Shipment
from .models import Supplier

from django.http import JsonResponse

from .models import StorageSpace
from .models import Item, Aisle  # Assuming you have these models

from .forms import ItemForm
from .models import StorageSpace

#for reports

from django.db.models import Sum
from django.db.models.functions import TruncDate
from django.shortcuts import render
from .models import Order, Shipment, Item








# -------------------------
# Basic Pages
# -------------------------

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def shipments(request):
    return render(request, 'shipments.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def inventory(request):
    return render(request, 'inventory.html')

@login_required
def suppliers(request):
    return render(request, 'suppliers.html')

@login_required
def reports(request):
    return render(request, 'reports.html')

# -------------------------
# Auth Views
# -------------------------

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome, {username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

# -------------------------
# Orders
# -------------------------

@login_required
def orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders.html', {'orders': orders})

@login_required
def order_create(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        employee = request.user

        Order.objects.create(product=product, quantity=quantity, status=status, employee=employee)
        messages.success(request, "Order created successfully.")
        return redirect('orders')

    return render(request, 'order_create.html', {'employee_name': request.user.username})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_detail.html', {'order': order})

@login_required
def order_delete(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    messages.success(request, "Order deleted successfully.")
    return redirect('orders')


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders_view.html', {'order': order})



#shipmetns part

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Shipment

def shipments(request):
    shipments = Shipment.objects.all()
    return render(request, 'shipments.html', {'shipments': shipments})

def edit_shipment(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        status = request.POST.get('status')

        shipment = get_object_or_404(Shipment, id=id)
        shipment.name = name
        shipment.status = status
        shipment.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def add_shipment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')

        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            quantity = 0  # Or handle error/validation as needed

        Shipment.objects.create(
            name=name,
            product=product,
            quantity=quantity,
            status=status
        )
        return redirect('shipments')  # Your shipments list URL name

    return render(request, 'shipments_create.html')


def delete_shipment(request, shipment_id):
    if request.method == 'POST':
        try:
            shipment = Shipment.objects.get(id=shipment_id)
            shipment.delete()
            return JsonResponse({'success': True})
        except Shipment.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Shipment not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


#suppliiii


def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers.html', {'suppliers': suppliers})

def add_supplier(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        company = request.POST['company']
        Supplier.objects.create(
            name=name, email=email, phone=phone, address=address, company=company
        )
        return redirect('suppliers')
    return render(request, 'add_supplier.html')

def edit_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.name = request.POST['name']
        supplier.email = request.POST['email']
        supplier.phone = request.POST['phone']
        supplier.address = request.POST['address']
        supplier.company = request.POST['company']
        supplier.save()
        return redirect('suppliers')
    return render(request, 'edit_supplier.html', {'supplier': supplier})


def delete_suppliers(request):
    if request.method == 'POST':
        ids = request.POST.getlist('supplier_ids')
        Supplier.objects.filter(id__in=ids).delete()
        return redirect('suppliers')
    suppliers = Supplier.objects.all()
    return render(request, 'delete_suppliers.html', {'suppliers': suppliers})

# inventoryyyyy


@login_required
def aisle_detail(request, aisle_id):
    aisle = get_object_or_404(Aisle, id=aisle_id)
    storage_spaces = aisle.storage_spaces.all()

    if request.method == 'POST':
        for space in storage_spaces:
            space.item_name = request.POST.get(f'item_name_{space.id}', getattr(space, 'item_name', ''))
            space.quantity = request.POST.get(f'quantity_{space.id}', getattr(space, 'quantity', 0))
            space.is_filled = f'is_filled_{space.id}' in request.POST
            space.save()
        messages.success(request, "Aisle updated successfully.")
        return redirect('aisle_detail', aisle_id=aisle.id)

    return render(request, 'aisle_detail.html', {'aisle': aisle, 'storage_spaces': storage_spaces})

@login_required
def inventory_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            storage_space = item.storage_space
            storage_space.is_filled = True
            storage_space.save()
            item.save()
            messages.success(request, "Item added successfully.")
            return redirect('inventory')
    else:
        form = ItemForm()
    return render(request, 'inventory_create.html', {'form': form})

@login_required
def inventory(request):
    aisle_data = []
    aisles = Aisle.objects.all()
    for aisle in aisles:
        total_spaces = aisle.storage_spaces.count()
        filled_spaces = aisle.storage_spaces.filter(is_filled=True).count()
        aisle_data.append({
            'aisle': aisle,
            'total_spaces': total_spaces,
            'filled_spaces': filled_spaces,
            'percentage_filled': round((filled_spaces / total_spaces) * 100) if total_spaces > 0 else 0,
        })

    return render(request, 'inventory.html', {'aisle_data': aisle_data})

@login_required
def add_aisle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        storage_capacity = request.POST.get('storage_capacity')
        if name and category and storage_capacity:
            try:
                storage_capacity = int(storage_capacity)
                Aisle.objects.create(name=name, category=category, storage_capacity=storage_capacity)
                messages.success(request, f"Aisle '{name}' added successfully.")
            except ValueError:
                messages.error(request, "Storage capacity must be an integer.")
        else:
            messages.error(request, "Please fill all fields to add an aisle.")
        return redirect('inventory')
    return redirect('inventory')

@login_required
def delete_aisle(request, aisle_id):
    if request.method == 'POST':
        aisle = get_object_or_404(Aisle, id=aisle_id)
        aisle.delete()
        messages.success(request, f"Aisle '{aisle.name}' deleted successfully.")
    return redirect('inventory')


@login_required
def view_aisle_items(request, aisle_id):
    aisle = get_object_or_404(Aisle, id=aisle_id)
    items = Item.objects.filter(aisle=aisle)  # filter by aisle, NOT storage_space
    return render(request, 'view_aisle_items.html', {'aisle': aisle, 'items': items})



#aisle add items

@login_required
def add_item_to_aisle(request, aisle_id):
    aisle = get_object_or_404(Aisle, id=aisle_id)
    storage_spaces = StorageSpace.objects.filter(aisle=aisle, is_filled=False).order_by('space_number')

    if request.method == "POST":
        name = request.POST.get("name")
        sku = request.POST.get("sku")
        quantity = request.POST.get("quantity")
        description = request.POST.get("description")

        if not (name and sku and quantity):
            messages.error(request, "Please fill all required fields.")
            return redirect('add_item_to_aisle', aisle_id=aisle.id)

        quantity = int(quantity)
        available_spaces_count = storage_spaces.count()

        if quantity > available_spaces_count:
            messages.error(request, f"Not enough empty storage spaces available. Available: {available_spaces_count}")
            return redirect('add_item_to_aisle', aisle_id=aisle.id)

        # Assign storage spaces for the quantity
        spaces_to_fill = storage_spaces[:quantity]

        for space in spaces_to_fill:
            Item.objects.create(
                storage_space=space,
                name=name,
                sku=sku,
                quantity=1,  # 1 per storage space, since each StorageSpace holds 1 item quantity?
                description=description or ""
            )
            space.is_filled = True
            space.save()

        aisle.storage_space += quantity
        aisle.save()

        messages.success(request, f"{quantity} item(s) added successfully.")
        return redirect('view_aisle_items', aisle_id=aisle.id)

    context = {
        'aisle': aisle,
    }
    return render(request, 'add_item.html', context)


#neww add asile afre i messed up

from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Aisle, StorageSpace
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def add_item(request):
    aisles = Aisle.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        sku = request.POST.get('sku')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description', '')  # optional
        category = request.POST.get('category', '')
        aisle_id = request.POST.get('aisle')
        aisle = get_object_or_404(Aisle, id=aisle_id)

        Item.objects.create(
            name=name,
            sku=sku,
            quantity=quantity,
            description=description,
            category=category,
            aisle=aisle,
        )
        return redirect('view_aisle_items', aisle_id=aisle.id)  # redirect to the aisle's item list page

    return render(request, 'add_item.html', {'aisles': aisles})

def delete_item(request, item_id):
    if request.method == 'POST':
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return HttpResponse("Item not found!", status=404)

        aisle_id = item.aisle.id
        item.delete()
        return redirect('view_aisle_items', aisle_id=aisle_id)
    else:
        return HttpResponse("Invalid request method", status=405)
    


#reportss yayyy

def reports(request):
    total_orders = Order.objects.count()
    total_shipments = Shipment.objects.count()

    orders_data_qs = (
        Order.objects
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('date')
    )
    shipments_data_qs = (
        Shipment.objects
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('date')
    )

    # Convert date objects to strings for JSON serialization
    orders_data = [
        {"date": o['date'].strftime("%Y-%m-%d") if o['date'] else '', "total_quantity": o['total_quantity']}
        for o in orders_data_qs
    ]
    shipments_data = [
        {"date": s['date'].strftime("%Y-%m-%d") if s['date'] else '', "total_quantity": s['total_quantity']}
        for s in shipments_data_qs
    ]

    total_inventory = Item.objects.aggregate(total=Sum('quantity'))['total'] or 0

    context = {
        'total_orders': total_orders,
        'total_shipments': total_shipments,
        'orders_data': orders_data,
        'shipments_data': shipments_data,
        'total_inventory': total_inventory,
    }
    return render(request, 'reports.html', context)


#dashboard connectionsssssssss


@login_required
def index(request):
    total_orders = Order.objects.count()
    total_shipments = Shipment.objects.count()
    total_suppliers = Supplier.objects.count()
    total_inventory = Item.objects.aggregate(total=Sum('quantity'))['total'] or 0

    context = {
        'total_orders': total_orders,
        'total_shipments': total_shipments,
        'total_suppliers': total_suppliers,
        'total_inventory': total_inventory,
    }
    return render(request, 'index.html', context)

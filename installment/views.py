from django.shortcuts import render, redirect, get_object_or_404
from .models import Installment
from .forms import InstallmentForm

def installment_list_view(request):
    installments = Installment.objects.all()
    return render(request, 'installment/installment_list.html', {'installments': installments})

def installment_create_view(request):
    if request.method == 'POST':
        form = InstallmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('installment_list')
    else:
        form = InstallmentForm()
    return render(request, 'installment/installment_form.html', {'form': form})

def installment_update_view(request, pk):
    installment = get_object_or_404(Installment, pk=pk)
    if request.method == 'POST':
        form = InstallmentForm(request.POST, instance=installment)
        if form.is_valid():
            form.save()
            return redirect('installment_list')
    else:
        form = InstallmentForm(instance=installment)
    return render(request, 'installment/installment_form.html', {'form': form})

def installment_delete_view(request, pk):
    installment = get_object_or_404(Installment, pk=pk)
    if request.method == 'POST':
        installment.delete()
        return redirect('installment_list')
    return render(request, 'installment/installment_confirm_delete.html', {'installment': installment})


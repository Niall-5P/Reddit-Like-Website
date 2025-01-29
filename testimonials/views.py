# testimonials/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Testimonial
from .forms import TestimonialForm

def testimonial_list(request):
    """List approved testimonials."""
    testimonials = Testimonial.objects.filter(approved=True)
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})

@login_required
def testimonial_create(request):
    """Create a new testimonial."""
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user
            # testimonial.approved = True/False depending on logic
            testimonial.save()
            messages.success(request, "Testimonial submitted successfully, awaiting approval.")
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()
    return render(request, 'testimonials/testimonial_form.html', {'form': form})

@login_required
def testimonial_update(request, pk):
    """Edit an existing testimonial."""
    testimonial = get_object_or_404(Testimonial, pk=pk, author=request.user)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimonial edited successfully, awaiting approval.")
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'testimonials/testimonial_form.html', {'form': form})

@login_required
def testimonial_delete(request, pk):
    """Delete a testimonial."""
    testimonial = get_object_or_404(Testimonial, pk=pk, author=request.user)
    if request.method == 'POST':
        testimonial.delete()
        message.success(request, "Testimonial deleted successfully")
        return redirect('testimonial_list')
    return render(request, 'testimonials/testimonial_confirm_delete.html', {'testimonial': testimonial})

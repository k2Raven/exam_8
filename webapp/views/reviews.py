from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import get_object_or_404

from webapp.models import Review, Product
from webapp.forms import UserReviewForm, ModeratorReviewForm


class CreateReviewView(CreateView):
    form_class = UserReviewForm
    model = Review
    template_name = 'review/create.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        author = self.request.user
        form.instance.author = author
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class UpdateReviewView(UpdateView):
    form_class = UserReviewForm
    model = Review
    template_name = 'review/update.html'

    def get_form_class(self):
        if self.request.user.has_perm('webapp.change_review'):
            return ModeratorReviewForm
        return UserReviewForm

    def form_valid(self, form):
        if not self.request.user.has_perm('webapp.change_review'):
            form.instance.is_moderated = False
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class DeleteReviewView(DeleteView):
    model = Review
    template_name = 'review/delete.html'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from webapp.models import Review, Product
from webapp.forms import UserReviewForm, ModeratorReviewForm


class CreateReviewView(LoginRequiredMixin, CreateView):
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


class UpdateReviewView(PermissionRequiredMixin, UpdateView):
    form_class = UserReviewForm
    model = Review
    template_name = 'review/update.html'
    permission_required = 'webapp.change_review'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

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


class DeleteReviewView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/delete.html'
    permission_required = 'webapp.delete_review'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class ListNoModeratedReviewView(PermissionRequiredMixin, ListView):
    model = Review
    template_name = 'review/no_moderated.html'
    context_object_name = 'reviews'
    permission_required = 'webapp.view_not_moderated_review'

    def get_queryset(self):
        return super().get_queryset().filter(is_moderated=False)

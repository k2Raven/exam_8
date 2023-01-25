from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.models import Product
from webapp.forms import ProductForm


class IndexView(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 3


class DetailProductView(DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.all()

        if not self.request.user.has_perm('webapp.view_not_moderated_review'):
            reviews = reviews.filter(is_moderated=True)

        context['reviews'] = reviews.order_by('-edited_at')
        return context


class CreateProductView(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'product/create.html'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})


class UpdateProductView(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product/update.html'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')

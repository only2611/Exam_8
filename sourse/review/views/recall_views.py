from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode


from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from review.forms import RecallForm
from review.models import Recall, Product




class RecallView(TemplateView):
    template_name = "recall/recall.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Recall, pk=pk)
        kwargs["task"] = task
        return super().get_context_data(**kwargs)


class CreateRecallView(LoginRequiredMixin,CreateView):
    model = Recall
    form_class = RecallForm
    template_name = "recall/create-recall.html"


    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        author = get_object_or_404(get_user_model(), pk=self.kwargs.get("pk"))
        form.instance.product = product
        form.instance.author = author
        return super().form_valid(form)

    def get_success_url(self):
       return reverse("review:product-view", kwargs={"pk": self.object.product.pk})




class UpdateRecall(LoginRequiredMixin, UpdateView):
    form_class = RecallForm
    template_name = "recall/update.html"
    model = Recall


    def get_success_url(self):
        return reverse("review:recall-view", kwargs={"pk": self.object.recall.pk})



class DeleteRecall(LoginRequiredMixin, DeleteView):
    model = Recall
    template_name = "recall/delete.html"

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("review:product-view:", kwargs={"pk": self.object.product.pk})


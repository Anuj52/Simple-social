from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from . import models

class PostList(generic.ListView):
    model = models.Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    queryset = models.Post.objects.select_related("user", "group")

class UserPostsList(generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        username = self.kwargs.get("username")
        try:
            user = models.User.objects.prefetch_related("posts").get(username__iexact=username)
        except models.User.DoesNotExist:
            raise Http404
        else:
            return user.posts.all()

class PostDetail(generic.DetailView):
    model = models.Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.kwargs.get("username")
        return queryset.filter(user__username__iexact=username)

class CreatePost(LoginRequiredMixin, generic.CreateView):
    model = models.Post
    template_name = "posts/post_form.html"
    fields = ('message', 'group')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = models.Post
    success_url = reverse_lazy("posts:all")  
    template_name = "posts/post_confirm_delete.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Post deleted successfully.")
        return super().delete(request, *args, **kwargs)

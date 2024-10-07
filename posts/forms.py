class CreatePost(LoginRequiredMixin, generic.CreateView):
    model = models.Post
    template_name = "posts/post_form.html"
    form_class = PostForm  # Use the custom PostForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the current logged-in user
        return super().form_valid(form)

from django.views.generic import TemplateView


class Success(TemplateView):
    template_name = '/accounts/registersuccess.html'

    def get_context_data(self, **kwargs):
        context = super(Success, self).get_context_data(**kwargs)
        context['title'] = 'sukces'
        return context





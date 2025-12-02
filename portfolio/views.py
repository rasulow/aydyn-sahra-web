from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Class-Based View for rendering the main portfolio page
    """
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add any additional context data here
        context['page_title'] = 'Aydyn Sahra - Portfolio'
        return context



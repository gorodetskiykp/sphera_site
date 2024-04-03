from django.shortcuts import render


def main_page(request):
    template = 'main_site/index.html'
    context = {
        'page_content': 'Hello!'
    }
    return render(request, template, context=context)

Introduction
============

django-fs-trumbowyg is the Django-related reusable app for integrating Trumbowyg WYSIWYG editor http://alex-d.github.io/Trumbowyg/.


Installation
============

1. Install ``django-fs-trumbowyg`` using ``pip``::

    $ pip install django-fs-trumbowyg

2. Add ``'trumbowyg'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'trumbowyg',
        ...
    )

3. Update your ``urls.py``::

    url(r'^trumbowyg/', include('trumbowyg.urls'))


Usage
=====

Use ``TrumbowygWidget`` in your forms::

    from django.forms import ModelForm
    from django.contrib.admin import ModelAdmin
    from trumbowyg.widgets import TrumbowygWidget
    from your_app.models import YourModel

    class YourModelAdminForm(ModelForm):
        class Meta:
            model = YourModel
            widgets = {
                'text': TrumbowygWidget(),
            }

    class YourModelAdmin(admin.ModelAdmin):
        form = YourModelAdminForm


    admin.site.register(YourModel, YourModelAdmin)


Credits
=======

`Fogstream <http://fogstream.ru/>`_
`Alex-D <http://alex-d.fr/>`_

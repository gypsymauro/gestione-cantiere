=================
Gestione-cantiere
=================

Gestione cantiere

Quick start
-----------

1. Aggiungi cantiere al tuo INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'cantiere',
    ]

2. installare le dipendenze::
     pip install reportlab # creazione delle stampe
     pip install django-crum # gestione delle modifiche
   
3. Eseguire `python manage.py migrate` per creare i modelli nel DB.

4. Avviare l'applicazione entrando nell'interfaccia di admin http://127.0.0.1:8000/admin/


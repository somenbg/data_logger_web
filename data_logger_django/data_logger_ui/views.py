from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from . import modules


# Create your views here.

def home(request):
    form = forms.getData()
    if request.method == 'POST':
        form = forms.getData(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            data = {1:{key:[value] for (key,value) in form.cleaned_data.items()}}
            dfmgr = modules.DataFrameManagement()
            df = dfmgr.dict_to_df(data)
            existing_data = dfmgr.read_csv(df)
            if existing_data.empty:
                new_df = df
            else:
                new_df = dfmgr.merge_df(existing_data, df)
            dfmgr.create_csv(new_df)
            form = forms.getData()
        html = 'Entry recieved'
    else:
        html = 'welcome to data-Logger'
    return render(request, 'home.html', {'html': html, 'form': form})
    


def crisp_home(request):
    pass
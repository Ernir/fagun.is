from django.shortcuts import render
from fagun.models import SidebarEntry

def index(request):

    sidebar_entries = SidebarEntry.objects.all()

    return render(request,"index.html", {
        "sidebar_entries": sidebar_entries
    })
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def buku(request):
    judul = ["Belajar Django", "Belajar PBO", "Belajar Python"]
    penulis = "Zul Hilmi"
    konteks = {
        'title' : judul,
        'penulis' : penulis,
    }

    # return HttpResponse('Halaman Buku')
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')
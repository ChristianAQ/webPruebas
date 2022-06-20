from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from photos.models import Photo, VISIBILITY_PUBLIC
from photos.forms import PhotoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.urls import reverse


def saludo(request):
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    return HttpResponse("Hello {0} {1}".format(nombre, apellido))


class HomeView(View):
    def get(self, request):
        """
        Renderiza el home con un listado de fotos
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # Recupera todas las fotos de la base de datos
        photos = Photo.objects.filter(visibility=VISIBILITY_PUBLIC).order_by('-created_at')
        context = {'photos_list': photos[:8]}
        return render(request, 'photos/home.html', context)


class PhotoQueryset(object):

    @staticmethod
    def get_photos_by_user(user):
        possible_photos = Photo.objects.select_related("owner")
        if not user.is_authenticated:
            possible_photos = possible_photos.filter(visibility=VISIBILITY_PUBLIC)
        elif not user.is_superuser:
            possible_photos = possible_photos.filter(Q(visibility=VISIBILITY_PUBLIC) | Q(owner=user))
        return possible_photos


class PhotoDetailView(View):
    def get(self, request, pk):
        """
            Renderiza el home con un listado de fotos
            :param request: objeto HtttpRequest con los datos de la peticion
            :param pk: clave primaria de la foto a recuperar
            :return: objeto HttpResponse con los datos de la respuesta
        """
        #es como hacer un join en la peticion a la base de datos .select_related("owner")
        possible_photos = PhotoQueryset.get_photos_by_user(request.user).filter(pk=pk).select_related("owner")
        if len(possible_photos) == 0:
            #por si no tiene foto ese id
            return HttpResponseNotFound("La imagen que buscas no existe")
        elif len(possible_photos) > 1:
            #por si tiene varias fotos
            return HttpResponse("Multiples opciones", status=300)

        photo = possible_photos[0]
        context = {'photo': photo}
        return render(request, 'photos/photo_detail.html', context)


class PhotoCreationView(View):
    @method_decorator(login_required())
    def get(self, request):
        """
            Presenta al formulario para cerar una foto
            :param request: objeto HtttpRequest con los datos de la peticion
            :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        photo_form = PhotoForm()
        context = {'form': photo_form, 'message': message}
        return render(request, 'photos/photo_creation.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
            Presenta al formulario para cerar una foto y en caso ed que la peticion sea POST la valida
            :param request: objeto HtttpRequest con los datos de la peticion
            :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        photo_with_user = Photo(owner=request.user)
        photo_form = PhotoForm(request.POST, instance=photo_with_user)
        if photo_form.is_valid():
            new_photo = photo_form.save()
            photo_form = PhotoForm()
            message = 'Foto creada satisfactoriamente <a href="{0}">Ver Foto</a>'.format(
                reverse('photos_detail', args=[new_photo.pk])
            )
        context = {'form': photo_form, 'message': message}
        return render(request, 'photos/photo_creation.html', context)


class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photos/photos_list.html'

    def get_queryset(self):
        result = super().get_queryset().filter(owner=self.request.user)
        return result








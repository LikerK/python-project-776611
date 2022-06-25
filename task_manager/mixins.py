from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import AccessMixin
from django.db.models import ProtectedError, RestrictedError


class CustomLoginRequiredMixin(AccessMixin):
    error_message = None
    redirect_url = 'users:list'

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object():
            messages.error(self.request, self.error_message)
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)


class CustomDeleteMixin(
    SuccessMessageMixin,
    LoginRequiredMixin,
    DeleteView
):
    deletion_error_message = None
    success_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(self.request, self.deletion_error_message,)
        except RestrictedError:
            messages.error(self.request, self.deletion_error_message,)
        return redirect(self.success_url)

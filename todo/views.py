from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm, CustomerModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import auth
from .models import Todo, Member, Flight
from .forms import TodoModelForm, FlightModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import FlightFilter
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


class TodoListView(ListView):
    model = Todo
    queryset = Todo.objects.filter(finish=False)  # 指定查詢條件
    template_name = 'todo/todo_list.html'  # 樣板路徑

    # 要傳遞的資料
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TodoModelForm()  # 資料模型表單
        return context


class Todo(CreateView):
    model = Todo
    form_class = TodoModelForm  # 使用的表單
    success_url = '/todo'  # 儲存成功後要導向的網址


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoModelForm  # 使用的表單類別
    template_name = 'todo/todo_update.html'  # 修改樣板
    success_url = '/todo'  # 儲存成功後要導向的網址


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'  # 刪除樣板
    success_url = '/todo'  # 刪除成功後要導向的網址


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'


class FlightListView(ListView):
    model = Flight
    queryset = Flight.objects.filter(finish=False)  # 指定查詢條件
    template_name = 'flight/flight_main.html'  # 樣板路徑

    def dispatch(self, request, *args, **kwargs):
        return super(FlightListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = FlightFilter(
            self.request.GET, queryset=self.get_queryset())  # 資料模型表單
        return context


class FlightMyListView(LoginRequiredMixin, ListView):
    model = Flight
    template_name = 'flight/flight_self.html'

    def get_queryset(self):
        return Flight.objects.filter(user=self.request.user)

    # 要傳遞的資料
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FlightModelForm()  # 資料模型表單
        return context


class FlightCreateView(CreateView):
    model = Flight
    form_class = FlightModelForm  # 使用的表單類別

    success_url = '/flight/mylist'  # 儲存成功後要導向的網址

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FlightCreateView, self).form_valid(form)


class FlightUpdateView(UpdateView):
    model = Flight
    form_class = FlightModelForm  # 使用的表單類別
    template_name = 'flight/flight_update.html'  # 修改樣板
    success_url = '/flight/mylist'  # 儲存成功後要導向的網址


class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'flight/flight_delete.html'  # 刪除樣板
    success_url = '/flight/mylist'  # 刪除成功後要導向的網址


class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flight/flight_detail.html'


# 首頁
@login_required(login_url="Login")
def index(request):
    return render(request, 'index.html')
# 註冊


def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  # 重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

# 登入


def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/flight')  # 重新導向到首頁
    context = {
        'form': form

    }
    return render(request, 'login.html', context)

# 登出


def log_out(request):
    logout(request)
    return redirect('/login')  # 重新導向到登入畫面

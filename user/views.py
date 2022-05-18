from django.http import JsonResponse
from .models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            exists_status = User.objects.filter(user_name=username).exists()
            if exists_status:
                return JsonResponse({'status':400, 'mes':'用户已存在'})
            else:
                obj = User.objects.create(user_name=username, password=password, email=email)
                obj.save()
                return JsonResponse({'status':200, 'mes': '注册成功'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': 400, 'mes': '注册失败'})

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:
                user = User.objects.get(user_name=username)
                if user.password == password:
                    status = user.user_status
                    return JsonResponse({'status': 200, 'mes': '登录成功', 'data': {'user_id': user.id,'status': status, 'email':user.email}})
                else:
                    return JsonResponse({'status': 400, 'mes': '登录失败用户名或密码错误'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': 400, 'mes': '登录成功用户名或密码错误'})


def modify(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            if id and username and password and email:
                user = User.objects.get(id=id)
                user.user_name = username
                user.password = password
                user.email = email
                user.save()
                return JsonResponse({'status': 200, 'mes': '修改成功'})
            return JsonResponse({'status': 400, 'mes': '修改失败'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': 400, 'mes': '失败'})


def show_user(request):
    user_info = User.objects.all().values()
    data_list = []
    for index, user in enumerate(user_info):
        user['index'] = index + 1
        data_list.append(user)
    return JsonResponse({'status': 200, 'data': data_list})


def show_self(request):
    user_id = request.GET.get('user_id')
    data_list = []
    user_info = User.objects.get(id=user_id)
    data = {
        'id': user_info.id,
        'user_name': user_info.user_name,
        'email': user_info.email,
    }
    data_list.append(data)
    return JsonResponse({'status': 200, 'data':data_list})


def show_user_status(request):
    user_id = request.GET.get('user_id')
    user_status = User.objects.get(id=user_id).user_status
    return JsonResponse({'status':200,'user_status': user_status})





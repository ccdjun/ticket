from django.shortcuts import render
from django.http import JsonResponse
from .models import Order, Ticket
from user.models import User
import time
import smtplib
from email.mime.text import MIMEText

def send_email(email):
    smtpserver = "smtp.qq.com"
    smtpport = 465
    from_mail = "912737790@qq.com"
    to_mail = [email]
    password = 'flevjfiiuaplbbfj'

    message = MIMEText('抢票成功请及时登录查看', 'plain', 'utf-8')
    smtp = smtplib.SMTP_SSL(smtpserver,smtpport)
    smtp.login(from_mail, password)
    smtp.sendmail(from_mail, to_mail, message.as_string())
    return

# Create your views here.
def add_ticket(requets):
    if requets.method == 'POST':
        source = requets.POST.get('source')
        target = requets.POST.get('target')
        num = requets.POST.get('num')
        ticket = Ticket.objects.create(source=source, target=target, num=num)
        ticket.save()
        return JsonResponse({'status':200})


def grab_tickets(request):
    if request.method == 'POST':
        try:
            user_id = request.POST.get('user_id')
            ticket_id = request.POST.get('ticket_id')
            ticket = Ticket.objects.get(id=ticket_id)
            source = ticket.source
            target = ticket.target
            num = ticket.num
            if int(num) > 0 and source and target:
                order = Order.objects.create(ticket_id=ticket_id, source=source, target=target, user_id=user_id, order_status=1)
                order.save()
                ticket.num = num - 1
                ticket.save()
                return JsonResponse({'status': 200, 'mes': '买票成功'})
            return JsonResponse({'status': 400, 'mes': '余票不足'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': 400, 'mes': '买票失败'})


def show_order(request):
    order_info = Order.objects.all().values()
    data_list = []
    try:
        for order in order_info:
            user = User.objects.get(id=order.get('user_id'))
            order['username'] = user.user_name
            data_list.append(order)
        return JsonResponse({'status': 200, 'data': data_list})
    except Exception as e:
        print(e)
    return JsonResponse({'status': 400, 'data': '查询失败'})


def show_ticket(request):
    tickets = Ticket.objects.all().values()
    ticket_info = []
    for index, ticket in enumerate(tickets):
        ticket['index'] = index + 1
        ticket_info.append(ticket)
    return JsonResponse({'status': 200, 'ticket_info': ticket_info})

def delete_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        obj = Order.objects.get(id=order_id)
        obj.delete()
        return JsonResponse({'status': 200, 'msg': '删除成功'})

def show_self_order(request):
    user_id = request.GET.get('user_id')
    try:
        order_info = Order.objects.filter(user_id=user_id).values()
        data_list = []
        for order in order_info:
            user = User.objects.get(id=user_id)
            order['user_name'] = user.user_name
            order['email'] = user.email
            data_list.append(order)
        return JsonResponse({'status': 200, 'data': data_list})
    except Exception as e:
        print(e)
    return JsonResponse({'status': 400, 'data': '查询失败'})

def lock_order(request):
    if request.method == 'POST':
        try:
            user_id = request.POST.get('user_id')
            ticket_id = request.POST.get('ticket_id')
            ticket = Ticket.objects.get(id=ticket_id)
            source = ticket.source
            target = ticket.target
            num = ticket.num
            if source and target:
                order = Order.objects.create(ticket_id=ticket_id, source=source, target=target, user_id=user_id, order_status=0)
                order.save()
                order_id = order.id
                for i in range(50):
                    print('开始第{}次抢票'.format(str(i)))
                    lock_ticket = Ticket.objects.get(id=ticket_id)
                    if lock_ticket.num > 0:
                        lock_ticket.num = lock_ticket.num - 1
                        lock_ticket.save()
                        order = Order.objects.get(id=order_id)
                        order.order_status = 1
                        order.save()
                        email = User.objects.get(id=user_id).email
                        send_email(email)
                        return JsonResponse({'status': 200, 'data': '抢票成功'})
                    time.sleep(4)
        except Exception as e:
            return JsonResponse({'status': 200, 'data': '抢票失败'})




import re
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *

import bcrypt

# Página de inicio
#=======================================================================================
def index(request):
    return render(request, 'index.html')

#=======================================================================================
def create_user(request):
    if request.method == "POST":

        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')

        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hash_pw
        )
        request.session['logged_user'] = new_user.id

        return redirect('/user/groups')
    return redirect('/')

#=======================================================================================
def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email = request.POST['email'])

        if user:
            log_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect('/user/groups')
        messages.error(request,'Email/password are incorrect. Please retry!')
    return redirect('/')

#=======================================================================================
def logout(request):
    request.session.flush()
    return redirect('/')

#=======================================================================================
def groups(request):
    if 'logged_user' not in request.session:
        messages.error(request, 'Please register or please log in first')
        return redirect('/')
    groups = Group.objects.all()
    lista_groups = []
    for group in groups:
        num_members = len(Member.objects.filter(group=group))
        group_complete = {
            'id': group.id,
            'name': group.name,
            'description':group.description,
            'user_create': group.user_create.first_name,
            'members': num_members
        }
        lista_groups.append(group_complete)

    context = {
        'logged_user': User.objects.get(id=request.session['logged_user']),
        'all_groups': lista_groups
    }

    return render(request,'groups.html', context)

def add_group(request):
    if 'logged_user' not in request.session:
        messages.error(request, 'Please register or please log in first')
        return redirect('/')
    

    user_create = User.objects.get(id=request.session['logged_user'])
    name = request.POST.get("name")
    description = request.POST.get("description")

    if len(name) <3:
            messages.error(request, 'Name must be at least 3 characters')
            return redirect('/user/groups')
    if len(description) <3:
            messages.error(request, 'Description must be at least 3 characters')
            return redirect('/user/groups')

    group = Group.objects.create(name=name, description=description, user_create=user_create)
    member_joined = Member.objects.create(group_id=group.id,users=user_create.id)
    return redirect('/user/groups')

def edit_group(request, group_id):
    if 'logged_user' not in request.session:
        messages.error(request, 'Please register or please log in first')
        return redirect('/')
    user_session = User.objects.get(id=request.session['logged_user'])
    group = Group.objects.get(id=group_id)
    members = Member.objects.filter(group=group)
    isJoined=False
    if request.method == "POST":
        for member in members:
            if user_session.id == member.users:
                member_joined = Member.objects.get(id=member.id)
                member_joined.delete()
                isJoined=True
                break 
        if not isJoined:
            member_joined = Member.objects.create(group_id=group_id,users=user_session.id)
        return redirect('/user/groups')
            

    else:
        user_created = 'YOU'
        if user_session != group.user_create:
            user_created =group.user_create.first_name + ' ' + group.user_create.last_name

        list_members =[]
        for member in members:
            user = User.objects.get(id=member.users)
            list_members.append(user.first_name + ' '+ user.last_name)
        is_creator=False
        if user_session == group.user_create:
            is_creator=True
        group_complete = {
            'id':group.id,
            'name': group.name,
            'description':group.description,
            'user_create': user_created,
            'members': list_members,
            'is_creator': is_creator
        }

        return render(request, 'edit.html', group_complete)

def delete_group(request, group_id):
    if 'logged_user' not in request.session:
        messages.error(request, 'Please register or please log in first')
        return redirect('/')
    group = Group.objects.get(id=group_id)
    print(group)
    group.delete()
    return redirect('/user/groups')
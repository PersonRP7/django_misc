def my_login_get(request):
    form = LoginForm()  
    return render(request, 'users/login.html', {'form':form})
	
def my_login_post(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        if not user:
            messages.info(request, "Incorrect credentials.")
            return render(request, 'users/login.html', {'form':form})
        elif user is not None:
            login(request, user)
            return redirect('users:profile')
    else:
        messages.info(request, "Form not correct.")
        return render(request, 'users/login.html', {'form':form})
		
def my_login(request):
    if request.method == 'GET':
        return my_login_get(request)
    elif request.method == 'POST':
        return my_login_post(request)
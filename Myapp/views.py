from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from Myapp.models import USERPASS, Signup, Resturant


def Login(request):

    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        if (user_name != '' and pass_word != ''):

            Usepass = USERPASS()
            Usepass.username = user_name
            Usepass.password = pass_word
            Usepass.save()

            messages.success(request, "Login Successfuly")

            return redirect('home/')

    return render(request, 'index.html')


def signup(request):

    if request.method == 'POST':
        name = request.POST.get('Name')
        mobile = request.POST.get('Number')
        user_name = request.POST.get('Username')
        pass_word = request.POST.get('Password')

        if ((name != '' and mobile != '') and (user_name != '' and pass_word != '')):

            Sign_up = Signup()
            Sign_up.Name = name
            Sign_up.Phone_Number = mobile
            Sign_up.Username = user_name
            Sign_up.Password = pass_word
            Sign_up.save()

            return redirect('Login')

    return render(request, 'Signup.html')


def Home(request):

    if request.method == 'POST':

        Restaurent_Id = request.POST.get('RasID')
        Restaurent_Name = request.POST.get('RasName')
        Restaurent_Email = request.POST.get('RasEmail')
        Restaurent_Address = request.POST.get('RasAdd')
        Restaurent_Phone = request.POST.get('RasPhone')
        Restaurent_Services = request.POST.get('RasService')

        Add_Res = Resturant()

        Add_Res.RestaurentId = Restaurent_Id
        Add_Res.RestaurentName = Restaurent_Name
        Add_Res.RestaurentEmail = Restaurent_Email
        Add_Res.RestaurentAddress = Restaurent_Address
        Add_Res.RestaurentPhone = Restaurent_Phone
        Add_Res.RestaurentServices = Restaurent_Services

        Add_Res.save()

    Rest = Resturant.objects.all()

    return render(request, 'Home.html', {'Rest': Rest})


def Delete(request, id):

    Res = Resturant.objects.get(id=id)
    Res.delete()

    return redirect('Home')

def Update(request, id):

    Res = Resturant.objects.get(id=id)
    
    if request.method == 'POST':

        Restaurent_Id = request.POST.get('RasID')
        Restaurent_Name = request.POST.get('RasName')
        Restaurent_Email = request.POST.get('RasEmail')
        Restaurent_Address = request.POST.get('RasAdd')
        Restaurent_Phone = request.POST.get('RasPhone')
        Restaurent_Services = request.POST.get('RasService')

        Add_Res = Resturant()
        id = id
        Add_Res.RestaurentId = Restaurent_Id
        Add_Res.RestaurentName = Restaurent_Name
        Add_Res.RestaurentEmail = Restaurent_Email
        Add_Res.RestaurentAddress = Restaurent_Address
        Add_Res.RestaurentPhone = Restaurent_Phone
        Add_Res.RestaurentServices = Restaurent_Services

        Add_Res.save()

    return redirect(request,'Home')
 
from django.shortcuts import render

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

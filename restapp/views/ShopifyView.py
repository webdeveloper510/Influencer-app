from rest_framework.views import View
from rest_framework.response import Response
from django.shortcuts import redirect,render
from restapi.settings import SHOPIFY_API_KEY,SHOPIFY_API_SECRET
import requests


class InstallView(View):
    def get(self, request):
        shop=request.GET.get("shop")
        scopes = ['read_orders','write_products','read_themes','write_themes','read_customers','write_customers','read_files','write_files']
        redirect_url = request.build_absolute_uri('/auth')
        install_url = f"https://{shop}/admin/oauth/authorize?client_id={SHOPIFY_API_KEY}&scope={'+'.join(scopes)}&redirect_uri={redirect_url}"
        return redirect(install_url)
    
    
    
class AuthView(View):
    def get(self, request):
        code = request.GET.get('code')
        token_url = f"https://your-store-name.myshopify.com/admin/oauth/access_token"
        data = {
            "client_id": SHOPIFY_API_KEY,
            "client_secret": SHOPIFY_API_SECRET,
            "code": code,
        }
        response = requests.post(token_url, data=data)
        response.raise_for_status()
        access_token = response.json()['access_token']
        # Store the access token in the database for later use
        return render(request, 'auth_success.html')    
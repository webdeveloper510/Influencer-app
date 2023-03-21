from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect,render
from restapi.settings import SHOPIFY_API_KEY,SHOPIFY_API_SECRET
import requests
import hmac
import hashlib
from django.http import JsonResponse



class InstallView(APIView):
    def get(self, request):
        print("enter in installl")
        # Check if the 'shop' parameter is present in the query string
        shop = request.query_params.get('shop')
        redirect_uri="https://api.myrefera.com/callback/"
        scopes = ['read_orders','write_products','read_themes','write_themes','read_customers','write_customers','read_files','write_files']
        if not shop:
            return Response({'error': 'Missing shop parameter'}, status=400)

        # Redirect the user to the Shopify authorization page
        auth_url = f"https://{shop}/admin/oauth/authorize?client_id={SHOPIFY_API_KEY}&scope={'+'.join(scopes)}&redirect_uri={redirect_uri}"
        
        return redirect(auth_url)

# class CallbackView(APIView):
#     print("enter-------------------------------")
#     def get(self, request):
#         print("enter in callback")
#         # Retrieve the temporary code from the Shopify callback
#         code = request.GET.get('code')
#         shop = request.GET.get('shop')
#         # Exchange the temporary code for an access token
        
#         token_url = 'https://{shop}/admin/oauth/access_token'
#         token_data = {
#             'client_id': SHOPIFY_API_KEY,
#             'client_secret': SHOPIFY_API_SECRET,
#             'code': code
#         }
#         response = requests.post(token_url, data=token_data)

#         # Store the access token in the session or database
#         access_token = response.json().get('access_token')
#         request.session['shopify_access_token'] = access_token

        # Redirect the user to the success page
        # return redirect('success_page')
        # return JsonResponse({'access_token': access_token})


# class InstallView(APIView):
#     def get(self, request):
#         shop = request.query_params.get('shop')
#         # redirect_uri = request.build_absolute_uri('/callback/')
#         redirect_uri="https://api.myrefera.com/callback/"
#         scopes = ['read_orders','write_products','read_themes','write_themes','read_customers','write_customers','read_files','write_files']
#         url = f"https://{shop}/admin/oauth/authorize?client_id={SHOPIFY_API_KEY}&scope={'+'.join(scopes)}&redirect_uri={redirect_uri}"
#         return Response({'url': url})

class CallbackView(APIView):
    def get(self, request):
        
        shop = request.query_params.get('shop')
        code = request.query_params.get('code')
        hmac_digest = request.query_params.get('hmac')
        print("----------------------------",hmac_digest)
        
        params=request.GET
        sorted_params='&'.join([f"{key}={params[key]}" for key in sorted(params)])
        secret = bytes(SHOPIFY_API_SECRET, 'utf-8')
        hmac_calculated = hmac.new(secret, sorted_params.encode('utf-8'), hashlib.sha256).hexdigest()
        print("hmac_calculated",hmac_calculated)
        print("-0-0-0-0-0",hmac_calculated ==hmac_digest)
        if not(request.GET,hmac_calculated):
           
            print("hmac_digest",hmac_digest)
            return Response({'error': 'Invalid HMAC'})
        
        access_token = self.get_access_token(shop, code)
        print("token",access_token.text)
        return Response({'access_token': access_token})

    def validate_hmac(self, params, hmac_digest):
        print('Entered')
        print("hmac_diii",hmac_digest)
        sorted_params = '&'.join([f"{key}={params[key]}" for key in sorted(params)])
      
        secret = bytes(SHOPIFY_API_SECRET, 'utf-8')
        hmac_calculated = hmac.new(secret, sorted_params.encode('utf-8'), hashlib.sha256).hexdigest()
        print("hmac_calculated",hmac_calculated)
        print("-0-0-0-0-0",hmac_calculated ==hmac_digest)
        return hmac_calculated == hmac_digest

    def get_access_token(self, shop, code):
        url = f"https://{shop}/admin/oauth/access_token"
        payload = {
            "client_id": SHOPIFY_API_KEY,
            "client_secret": SHOPIFY_API_SECRET,
            "code": code,
        }
        response = requests.post(url, json=payload)
        return response




































# #INSTALL APP IN SHOPIFY API
# class InstallView(View):
#     def get(self, request):
#         shop=request.GET.get("shop")
#         scopes = ['read_orders','write_products','read_themes','write_themes','read_customers','write_customers','read_files','write_files']
#         redirect_url = request.build_absolute_uri('/auth')
#         install_url = f"https://{shop}/admin/oauth/authorize?client_id={SHOPIFY_API_KEY}&scope={'+'.join(scopes)}&redirect_uri={redirect_url}"
#         return redirect(install_url)
    
    
    

# # AUTHENTICATE APP API
# class AuthView(View):
#     def get(self, request):
#         shop=request.GET.get("shop")
#         code = request.GET.get('code')
#         token_url = f"https://{shop}/admin/oauth/access_token"
#         print(token_url)
#         data = {
#             "client_id": SHOPIFY_API_KEY,
#             "client_secret": SHOPIFY_API_SECRET,
#             "code": code,
#         }
#         response = requests.post(token_url, data=data)
#         print("-------",response)
#         response.raise_for_status()
#         access_token = response.json()['access_token']
#         # Store the access token in the database for later use
#         return render(request, 'auth_success.html')    
    
    
    
    
# def authenticate(request):
#     shop_url = request.GET.get('shop')
#     if shop_url:
#         params = {
#             'client_id': SHOPIFY_API_KEY,
#             'scope': 'read_products',
#             'redirect_uri': 'https://your-app-url.com/auth/callback',
#             'state': 'your-unique-state-token',
#         }
#         auth_url = f'https://{shop_url}/admin/oauth/authorize?{urllib.parse.urlencode(params)}'
#         return redirect(auth_url)

# def callback(request):
#     code = request.GET.get('code')
#     state = request.GET.get('state')
#     hmac_param = request.GET.get('hmac')
#     if hmac_param and code and state:
#         hmac_digest = hmac.new(
#             key=SHOPIFY_API_SECRET.encode('utf-8'),
#             msg=f'state={state}&code={code}'.encode('utf-8'),
#             digestmod=hashlib.sha256
#         ).hexdigest()
#         if hmac_digest == hmac_param:
#             params = {
#                 'client_id': SHOPIFY_API_KEY,
#                 'client_secret': SHOPIFY_API_SECRET,
#                 'code': code
#             }
#             access_token_url = f'https://{request.GET["shop"]}/admin/oauth/access_token'
#             response = requests.post(access_token_url, data=params)
#             access_token = json.loads(response.text)['access_token']
#             return HttpResponse(f'Access token: {access_token}')
#     return HttpResponse('Invalid request')


# urlpatterns = [
#     path('auth', authenticate, name='authenticate'),
#     path('auth/callback', callback, name='callback'),
# ]
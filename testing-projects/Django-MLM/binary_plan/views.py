from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from binary_plan.models import BinaryUserInstence, BinaryTreeQueue
from binary_plan.models import BinaryWallet, TransactionLog

def profile(request):
    return render(request, 'binaryPlan/profile.html')

@login_required
def dashboard(request):
    item = BinaryTreeQueue.objects.first()
    item_erlier = BinaryTreeQueue.objects.earliest('pk')
    print(item, item_erlier)
    try:
        user_instance = BinaryUserInstence.objects.get(user=request.user)
        print(f"Number of children: {user_instance.count_child_nodes()}")
        context = {
            'user' : {
                'business_volume': user_instance.business_volume,
                'direct_income': user_instance.direct_income,
                'step_income': user_instance.step_income,
                'binary_income': user_instance.binary_income,
                'gift_and_rewards': user_instance.gift_and_rewards,
                },
            'number_of_referrals': user_instance.number_of_referrals
            }
        return render(request, 'binaryPlan/dashboard.html', context)
    
    except BinaryUserInstence.DoesNotExist:
        return HttpResponse('You are not a member of the binary plan!')
    
def bvlog(request):
    return render(request, 'binaryPlan/bvLog.html')

@login_required
def referrals(request):
    user = request.user
    if user:
        try:
            user_instance = BinaryUserInstence.objects.get(user=user)
            referrals = BinaryUserInstence.objects.filter(refferal=user_instance)
            context = {
                'referrals': referrals
            }
            return render(request, 'binaryPlan/referrels.html', context)
        except BinaryUserInstence.DoesNotExist:
            return HttpResponse('You are not a member of the binary plan!')

    return render(request, 'binaryPlan/referrels.html')

def twoFA(request):
    return render(request, 'binaryPlan/2fa.html')

def buy_product(request, product_id):
    return HttpResponse(f'Buy product {product_id}')

@login_required  
def withdraw(request):
    wallet = BinaryWallet.objects.filter(user=request.user)

    if wallet.exists():
        wallet.first().withdraw(10)

    return render(request, 'binaryPlan/withdraw.html')

@login_required             
def deposit(request):
    wallet = BinaryWallet.objects.filter(user=request.user)
    
    if wallet.exists():
        wallet.first().deposit(10, 'direct')

    return render(request, 'binaryPlan/deposit.html')

def transaction_history(request):
    wallet = BinaryWallet.objects.filter(user=request.user)
    if wallet.exists():
        wallet = wallet.first()
        transactions = TransactionLog.objects.filter(wallet=wallet)
        if transactions.exists():
            transactions = transactions.all()
            context = {
                'transactions': transactions
            }
            return render(request, 'binaryPlan/transections.html', context)
    return render(request, 'binaryPlan/transections.html')

def support(request):
    return render(request, 'binaryPlan/supportTicket.html')
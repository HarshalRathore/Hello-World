from binary_plan.models import BinaryWallet

def get_balance(request):
    wallet = BinaryWallet.objects.filter(user=request.user)
    if wallet.exists():
        return {'get_balance': wallet.first().balance}
    return {'get_balance': 'xxxx'}
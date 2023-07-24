from django.urls import path
from binary_plan import views

urlpatterns = [
    path('dashboard/', view=views.dashboard, name='binary-dashboard'),
    path('bvlog', view=views.bvlog, name='binary-bvlog'),
    path('profile/', view=views.profile, name='profile'),
    path('referrals/', view=views.referrals, name='binary-referrals'),
    path('2fA/', view=views.twoFA, name='binary-2fA'),
    path('withdraw/', view=views.withdraw, name='binary-withdraw'),
    path('trasaction-history/', view=views.transaction_history, name='binary-transaction-history'),
    path('support/', view=views.support, name='binary-support'),
    path('deposit/', view=views.deposit, name='binary-deposit'),
    path('withdraw/', view=views.withdraw, name='binary-withdraw'),
    path('buy-product/<int:product_id>/', view=views.buy_product, name='binary-buy-product'),
]

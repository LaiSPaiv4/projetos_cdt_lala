from flask import Blueprint, render_template, abort
from app.models.user import FinancialProfile
from app.services.finance_service import FinanceService

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/resultado/<int:profile_id>')
def result(profile_id):
    # CORREÇÃO: O termo correto é get_or_404
    perfil = FinancialProfile.query.get_or_404(profile_id)
    
    # Calcula as fatias 50-30-20
    plano = perfil.calcular_plano_503020()
    
    # Busca as dicas específicas do Nubank/Inter
    recomendacoes = FinanceService.recomendar_investimento(perfil.banco_principal, perfil.meta)
    
    return render_template('dashboard.html', 
                           perfil=perfil, 
                           plano=plano, 
                           recomendacoes=recomendacoes)
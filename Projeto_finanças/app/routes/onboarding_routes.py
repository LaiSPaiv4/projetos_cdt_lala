from flask import Blueprint, render_template, request, redirect, url_for
from app.models.user import FinancialProfile
from app import db

onboarding = Blueprint('onboarding', __name__)

@onboarding.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pega os dados que virão do HTML (que faremos depois)
        novo_perfil = FinancialProfile(
            nome=request.form.get('nome'),
            meta=request.form.get('meta'),
            renda_mensal=float(request.form.get('renda')),
            banco_principal=request.form.get('banco')
        )
        db.session.add(novo_perfil)
        db.session.commit()
        
        # Manda para a página de resultado que você criou!
        return redirect(url_for('dashboard.result', profile_id=novo_perfil.id))
    
    return render_template('onboarding.html')
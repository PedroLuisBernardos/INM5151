# routes.py
# défini les routes de l'application
from datetime import date, datetime
from flask import render_template, flash, redirect, url_for, request, session
from flask_login import logout_user, current_user, login_required
from app import app, db
from app.forms import EditProfileForm, FactureForm, ContactForm, CompanyProfilForm, SelectCompanyProfilForm, CompteForm
from app.models import User, Facture, Contact, CompanyProfil, Compte
from flask_babel import _

# Page d'accueil pour les utilisateurs - page pour choisir les profils d'entreprise
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = SelectCompanyProfilForm()
    if form.validate_on_submit():
        companyProfil = CompanyProfil.query.filter_by(name=form.company_profil_name.data.name).first()
        if companyProfil:
            user_to_update = User.query.get_or_404(current_user.id)
            user_to_update.profil_courrant = companyProfil.id
            db.session.commit()
            flash(_('Vous avez sélectionné ' + companyProfil.name))
        else:
            companyProfil = CompanyProfil(name=form.company_profil_name.data, user_id=current_user.id)
            flash(_('Erreur. Profil d\'entreprise non trouvé.'))
            return redirect(url_for('index'))

    page = request.args.get('page', 1, type=int)

    # Tous les profils d'entreprise de l'utilisateur actuel
    companyProfil = CompanyProfil.query.filter_by(user_id=current_user.id).paginate(page, app.config['COMPANY_PROFIL_PAR_PAGE'], False)
    next_url = url_for('index', companyProfil=index.next_num) if companyProfil.has_next else None
    prev_url = url_for('index', companyProfil=index.prev_num) if companyProfil.has_prev else None
    return render_template("index.html", title=_('Accueil'), form=form, companyProfil=companyProfil.items, next_url=next_url, prev_url=prev_url)

# Page de modification de profil d'entreprise
@app.route('/register_company_profil', methods=['GET', 'POST'])
@login_required
def register_company_profil():
    form = CompanyProfilForm()

    if form.validate_on_submit():
        companyProfil = CompanyProfil.query.filter_by(name=form.name.data).first()
        if companyProfil:
            flash(_('Ce profil d\'entreprise existe déjà.'))
        else:
            companyProfil = CompanyProfil(name=form.name.data, user_id=current_user.id)
            db.session.add(companyProfil)
            db.session.commit()
            flash(_('Votre profile d\'entreprise a été ajouté.'))
            return redirect(url_for('index'))
    
    page = request.args.get('page', 1, type=int)
    companyProfil = CompanyProfil.query.filter_by(user_id=current_user.id).paginate(page, app.config['COMPANY_PROFIL_PAR_PAGE'], False)
    next_url = url_for('register_company_profil', companyProfil=register_company_profil.next_num) if companyProfil.has_next else None
    prev_url = url_for('register_company_profil', companyProfil=register_company_profil.prev_num) if companyProfil.has_prev else None
    return render_template("update/register_company_profil.html", title=_('Accueil'), companyProfil=companyProfil.items, form=form, next_url=next_url, prev_url=prev_url)

# Page de création de factures
@app.route('/bill', methods=['GET', 'POST'])
@login_required
def bill():
    if current_user.profilEntreprise:
        form = FactureForm()
        form.contact_id.choices = [''] + [(row.name) for row in Contact.query.filter_by(user_id=current_user.id)]
        # À ajouter des attributs
        if form.validate_on_submit():
            facture = Facture.query.filter_by(reference=form.reference.data).first()
            if facture:
                flash(_('Cette référence existe déjà.'))
            else:
                facture = Facture(paid=form.paid.data, reference=form.reference.data, date=form.date.data, due_date=form.due_date.data, description=form.description.data, contact_id=form.contact_id.data.id, compte_id=form.compte_id.data.id, profilEntreprise_id=current_user.profil_courrant, subtotal=form.subtotal.data, total=form.get_total(form.tax.data, form.subtotal.data), tax=form.tax.data, user_id=current_user.id)
                db.session.add(facture)
                db.session.commit()
                flash(_('Votre facture a été ajoutée.'))
                return redirect(url_for('bill'))

        # Toutes les factures de l'utilisateur actuel et du profil d'entreprise actuel
        page = request.args.get('page', 1, type=int)
        factures = Facture.query.filter_by(user_id=current_user.id, profilEntreprise_id=current_user.profil_courrant).paginate(page, app.config['FACTURES_PAR_PAGE'], False)
        next_url = url_for('index', page=factures.next_num) if factures.has_next else None
        prev_url = url_for('index', page=factures.prev_num) if factures.has_prev else None
        return render_template("bill.html", title=_('Facture'), form=form, factures=factures.items, date_today=date.today(), next_url=next_url, prev_url=prev_url)
    else:
        flash(_('Veuillez créer un profil d\'entreprise avant d\'effectuer cette action.'))
        return redirect(url_for('index'))

# Page des contacts
@app.route('/contacts', methods=['GET', 'POST'])
@login_required
def contacts():
    if current_user.profilEntreprise:
        form = ContactForm()
        if form.validate_on_submit():
            contact = Contact.query.filter_by(name=form.name.data, profilEntreprise_id=current_user.profil_courrant).first()
            if contact:
                flash(_('Ce contact existe déjà.'))
            else:
                contact = Contact(name=form.name.data, phone_number=form.phone_number.data, email=form.email.data, address=form.address.data, user_id=current_user.id, profilEntreprise_id=current_user.profil_courrant)
                db.session.add(contact)
                db.session.commit()
                flash(_('Votre contact a été ajouté.'))
                return redirect(url_for('contacts'))

        # Tous les contacts de l'utilisateur actuel
        page = request.args.get('page', 1, type=int)
        contacts = Contact.query.filter_by(user_id=current_user.id, profilEntreprise_id=current_user.profil_courrant).paginate(page, app.config['CONTACTS_PAR_PAGE'], False)
        next_url = url_for('contacts', page=contacts.next_num) if contacts.has_next else None
        prev_url = url_for('contacts', page=contacts.prev_num) if contacts.has_prev else None
        return render_template("contacts.html", title=_('Contacts'), form=form, contacts=contacts.items, next_url=next_url, prev_url=prev_url)
    else:
        flash(_('Veuillez créer un profil d\'entreprise avant d\'effectuer cette action.'))
        return redirect(url_for('index'))

# Page des comptes
@app.route('/comptes', methods=['GET', 'POST'])
@login_required
def comptes():
    if current_user.profilEntreprise:
        form = CompteForm()
        if form.validate_on_submit():
            compte = Compte.query.filter_by(name=form.name.data, profilEntreprise_id=current_user.profil_courrant).first()
            if compte:
                flash(_('Ce compte existe déjà.'))
            else:
                compte = Compte(name=form.name.data, user_id=current_user.id, profilEntreprise_id=current_user.profil_courrant)
                db.session.add(compte)
                db.session.commit()
                flash(_('Votre compte a été ajouté.'))
                return redirect(url_for('comptes'))

        # Tous les comptes de l'utilisateur actuel
        page = request.args.get('page', 1, type=int)
        comptes = Compte.query.filter_by(user_id=current_user.id, profilEntreprise_id=current_user.profil_courrant).paginate(page, app.config['COMPTES_PAR_PAGE'], False)
        next_url = url_for('comptes', page=comptes.next_num) if comptes.has_next else None
        prev_url = url_for('comptes', page=comptes.prev_num) if comptes.has_prev else None
        return render_template("comptes.html", title=_('Comptes'), form=form, comptes=comptes.items, next_url=next_url, prev_url=prev_url)
    else:
        flash(_('Veuillez créer un profil d\'entreprise avant d\'effectuer cette action.'))
        return redirect(url_for('index'))

# Page d'accueil pour les invités
@app.route('/')
@app.route('/welcome')
def welcome():
    # Si l'utilisateur est actuellement connecté, ne pas aller à la page /welcome
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('welcome.html', title=_('Bienvenue'))

# Page profil
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', title=_('Mon profil'), user=user)

# Supprimer un utilisateur et toutes ses factures
@app.route('/delete_user/<username>')
@login_required
def delete_user(username):
    try:
        user = User.query.filter_by(username=username).first_or_404()
        factures = Facture.query.filter_by(user_id=user.id).all()
        for f in factures:
            db.session.delete(f)
        logout_user()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('welcome'))
    except:
        error_string = _('Il y a eu une erreur avec la suppression de l\'utilisateur.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Supprimer des factures
@app.route('/delete_bill/<facture_id>')
@login_required
def delete_bill(facture_id):
    facture_to_delete = Facture.query.get_or_404(facture_id)
    try:
        db.session.delete(facture_to_delete)
        db.session.commit()
        return redirect(url_for('bill'))
    except:
        error_string = _('Il y a eu une erreur avec la suppression de la facture.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Supprimer des contacts
@app.route('/delete_contact/<contact_id>')
@login_required
def delete_contact(contact_id):
    contact_to_delete = Contact.query.get_or_404(contact_id)
    try:
        db.session.delete(contact_to_delete)
        db.session.commit()
        return redirect(url_for('contacts'))
    except:
        error_string = _('Il y a eu une erreur avec la suppression du contact.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Supprimer des comptes
@app.route('/delete_compte/<compte_id>')
@login_required
def delete_compte(compte_id):
    compte_to_delete = Compte.query.get_or_404(compte_id)
    try:
        db.session.delete(compte_to_delete)
        db.session.commit()
        return redirect(url_for('comptes'))
    except:
        error_string = _('Il y a eu une erreur avec la suppression du compte.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Supprimer des profils d'entreprise
@app.route('/delete_company_profil/<company_profil_id>')
@login_required
def delete_company_profil(company_profil_id):
    company_profil_to_delete = CompanyProfil.query.get_or_404(company_profil_id)
    try:
        db.session.delete(company_profil_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        error_string = _('Il y a eu une erreur avec la suppression du profil d\'entreprise.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Modifier des factures
@app.route('/update_bill/<facture_id>', methods=['GET', 'POST'])
def update_bill(facture_id):
    try:
        facture_to_update = Facture.query.get_or_404(facture_id)
        form = FactureForm()
        if form.validate_on_submit():
            facture = Facture.query.filter_by(reference=form.reference.data).first()
            if facture and facture is not facture_to_update:
                flash(_('Cette référence existe déjà.'))
            else:
                facture_to_update.paid = form.paid.data
                facture_to_update.reference = form.reference.data
                facture_to_update.date = form.date.data
                facture_to_update.due_date = form.due_date.data
                facture_to_update.description = form.description.data
                facture_to_update.subtotal = form.subtotal.data
                facture_to_update.total = form.get_total(form.tax.data, form.subtotal.data)
                facture_to_update.tax = form.tax.data
                facture_to_update.contact_id = form.contact_id.id

                db.session.commit()
                flash(_('Les modifications ont été sauvegardées.'))
                return redirect(url_for('bill'))
        elif request.method == 'GET':
            form.paid.data = facture_to_update.paid
            form.reference.data = facture_to_update.reference
            form.date.data = facture_to_update.date
            form.due_date.data = facture_to_update.due_date
            form.description.data = facture_to_update.description
            form.subtotal.data = facture_to_update.subtotal
            form.tax.data = facture_to_update.tax
            form.contact_id.id = facture_to_update.contact_id
        return render_template('update/update_facture.html', title=_('Modification de la facture'), form=form, facture=facture_to_update)
    except:
        error_string = _('Il y a eu une erreur avec la modification de la facture.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Modifier des contacts
@app.route('/update_contact/<contact_id>', methods=['GET', 'POST'])
def update_contact(contact_id):
    try:
        contact_to_update = Contact.query.get_or_404(contact_id)
        form = ContactForm()
        if form.validate_on_submit():
            contact = Contact.query.filter_by(name=form.name.data).first()
            if contact and contact is not contact_to_update:
                flash(_('Ce contact existe déjà.'))
            else:
                contact_to_update.name = form.name.data
                contact_to_update.phone_number = form.phone_number.data
                contact_to_update.email = form.email.data
                contact_to_update.address = form.address.data

                db.session.commit()
                flash(_('Les modifications ont été sauvegardées.'))
                return redirect(url_for('contacts'))
        elif request.method == 'GET':
            form.name.data = contact_to_update.name
            form.phone_number.data = contact_to_update.phone_number
            form.email.data = contact_to_update.email
            form.address.data = contact_to_update.address
        return render_template('update/update_contact.html', title=_('Modification du contact'), form=form, contact=contact_to_update)
    except:
        error_string = _('Il y a eu une erreur avec la modification du contact.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Modifier des comptes
@app.route('/update_compte/<compte_id>', methods=['GET', 'POST'])
def update_compte(compte_id):
    try:
        compte_to_update = Compte.query.get_or_404(compte_id)
        form = CompteForm()
        if form.validate_on_submit():
            compte = Compte.query.filter_by(name=form.name.data).first()
            if compte and compte is not compte_to_update:
                flash(_('Ce compte existe déjà.'))
            else:
                compte_to_update.name = form.name.data
                db.session.commit()
                flash(_('Les modifications ont été sauvegardées.'))
                return redirect(url_for('comptes'))
        elif request.method == 'GET':
            form.name.data = compte_to_update.name
        return render_template('update/update_compte.html', title=_('Modification du compte'), form=form, compte=compte_to_update)
    except:
        error_string = _('Il y a eu une erreur avec la modification du compte.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Modifier des profils d'entreprise
@app.route('/update_company_profil/<company_profil_id>', methods=['GET', 'POST'])
def update_company_profil(company_profil_id):
    try:
        company_profile_to_update = CompanyProfil.query.get_or_404(company_profil_id)
        form = CompanyProfilForm()
        if form.validate_on_submit():
            company_profile = CompanyProfil.query.filter_by(name=form.name.data).first()
            if company_profile and company_profile is not company_profile_to_update:
                flash(_('Ce profil d\'entreprise existe déjà.'))
            else:
                company_profile_to_update.name = form.name.data
                db.session.commit()
                flash(_('Les modifications ont été sauvegardées.'))
                return redirect(url_for('index'))
        elif request.method == 'GET':
            form.name.data = company_profile_to_update.name
        return render_template('update/update_company_profil.html', title=_('Modification du profil d\'entreprise'), form=form, company_profile=company_profile_to_update)
    except:
        error_string = _('Il y a eu une erreur avec la modification du profil d\'entreprise.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Pour savoir c'est quand la dernière fois que l'utilisateur s'est connecté
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

# Modifier son profil
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    try:
        form = EditProfileForm(current_user.username)
        if form.validate_on_submit():
            current_user.username = form.username.data
            current_user.about_me = form.about_me.data
            db.session.commit()
            flash(_('Les modifications ont été sauvegardées.'))
            return redirect(url_for('user', username=current_user.username))
        elif request.method == 'GET':
            form.username.data = current_user.username
            form.about_me.data = current_user.about_me
        return render_template('update/edit_profile.html', title=_('Modifier votre profil'),form=form)
    except:
        error_string = _('Il y a eu une erreur avec la modification du profil.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# UNIQUEMENT POUR LES ADMINISTRATEURS
@app.route('/all')
def all():
    users = User.query.all()
    factures = Facture.query.all()
    return render_template('all.html', users=users, factures=factures)

# Modifier la langue
@app.route('/language/<language>')
def set_language(language=None):
    session['language'] = language
    return redirect(url_for('index'))

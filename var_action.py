from flask import render_template, request, redirect, url_for, flash
from app_pre import db, app
from new_control.Variation import create_variation, get_variation, update_variation, delete_variation, get_all_variations

@app.route('/variations')
def variations():
    all_variations = get_all_variations(session=db.session)
    return render_template('variations.html', variations=all_variations)

@app.route('/create_variation', methods=['GET', 'POST'])
def create_variation_view():
    if request.method == 'POST':
        vtext = request.form.get('vtext')
        create_variation(vtext=vtext, session=db.session)
        flash('Variation created successfully!', 'success')
        return redirect(url_for('variations'))
    return render_template('create_variation.html')

@app.route('/update_variation/<int:vcode>', methods=['GET', 'POST'])
def update_variation_view(vcode):
    variation = get_variation(vcode=vcode, session=db.session)
    if request.method == 'POST':
        vtext = request.form.get('vtext')
        update_variation(vcode=vcode, vtext=vtext, session=db.session)
        flash('Variation updated successfully!', 'success')
        return redirect(url_for('variations'))
    return render_template('update_variation.html', variation=variation)

@app.route('/delete_variation/<int:vcode>', methods=['POST'])
def delete_variation_view(vcode):
    delete_variation(vcode=vcode, session=db.session)
    flash('Variation deleted successfully!', 'success')
    return redirect(url_for('variations'))

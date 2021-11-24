from flask import Blueprint, render_template, redirect, url_for
from toy.web import forms
from toy import models


module = Blueprint("items", __name__, url_prefix='/items')

@module.route('')
def index():
    items = models.Item.objects()
    status = models.Status.objects()
    return render_template(
        'items/index.html',
        items = items,
        status = status,
        )

@module.route('/add', methods = ['GET', 'POST'])
def add():

    form = forms.stocks.ItemForm()
    if not form.validate_on_submit():
        return render_template(
            'items/add.html',
            form = form,
        )

    item = models.Item(
        name = form.name.data,
        description = form.description.data,
        weight = form.weight.data,
    )

    item.save()

    return redirect(url_for('items.index'))

@module.route('/status', methods = ['GET', 'POST'])
def status():

    form = forms.stocks.ItemStatusForm()
    if not form.validate_on_submit():
        return render_template(
            'items/status.html',
            form = form,
        )

    item = models.Status(
        buyer = form.buyer.data,
        seller = form.seller.data,
        item = form.item.data,
    )

    item.save()

    return redirect(url_for('items.index'))
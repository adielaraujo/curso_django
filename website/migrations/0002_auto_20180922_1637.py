# Generated by Django 2.1.1 on 2018-09-22 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='menasgem',
            new_name='mensagem_email',
        ),
    ]

# Generated by Django 4.0.5 on 2022-09-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_consulta_mensaje_alter_consulta_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='numero',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consulta',
            name='mensaje',
            field=models.TextField(max_length=200),
        ),
    ]
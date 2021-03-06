# Generated by Django 2.0 on 2017-12-05 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rnpa', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('localidad', models.CharField(max_length=255)),
                ('ano', models.CharField(max_length=255)),
                ('inegi_localidad', models.CharField(max_length=255)),
                ('inegi_municipio', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rnpa', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BeneficiariosDiesel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(blank=True, max_length=255)),
                ('beneficiario', models.CharField(blank=True, max_length=255)),
                ('rfc', models.CharField(blank=True, max_length=255)),
                ('rnpa', models.CharField(blank=True, max_length=255)),
                ('estado', models.CharField(blank=True, max_length=255)),
                ('municipio', models.CharField(blank=True, max_length=255)),
                ('localidad', models.CharField(blank=True, max_length=255)),
                ('monto', models.FloatField()),
                ('inegi_localidad', models.CharField(blank=True, max_length=255)),
                ('inegi_municipio', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BeneficiariosGasolina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(blank=True, max_length=255)),
                ('beneficiario', models.CharField(blank=True, max_length=255)),
                ('rfc', models.CharField(blank=True, max_length=255)),
                ('rnpa', models.CharField(blank=True, max_length=255)),
                ('estado', models.CharField(blank=True, max_length=255)),
                ('municipio', models.CharField(blank=True, max_length=255)),
                ('localidad', models.CharField(blank=True, max_length=255)),
                ('monto', models.FloatField()),
                ('inegi_localidad', models.CharField(blank=True, max_length=255)),
                ('inegi_municipio', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Embarcacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rnpa', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('rnpa_unidad_economica', models.CharField(max_length=255)),
                ('nombre_unidad_economica', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('localidad', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('fecha_registro', models.CharField(max_length=255)),
                ('inegi_localidad', models.CharField(max_length=255)),
                ('inegi_municipio', models.CharField(max_length=255)),
                ('beneficiario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='embarcaciones', to='api.Beneficiario')),
            ],
        ),
        migrations.CreateModel(
            name='Inegi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_inegi', models.CharField(max_length=255)),
                ('cod_estado', models.CharField(blank=True, max_length=255)),
                ('estado', models.CharField(blank=True, max_length=255)),
                ('estado_abreviado', models.CharField(blank=True, max_length=255)),
                ('cod_municipio', models.CharField(blank=True, max_length=255)),
                ('municipio', models.CharField(blank=True, max_length=255)),
                ('cod_localidad', models.CharField(blank=True, max_length=255)),
                ('localidad', models.CharField(blank=True, max_length=255)),
                ('ambito', models.CharField(blank=True, max_length=255)),
                ('latitud', models.CharField(blank=True, max_length=255)),
                ('longitud', models.CharField(blank=True, max_length=255)),
                ('altitud', models.CharField(blank=True, max_length=255)),
                ('cve_carta', models.CharField(blank=True, max_length=255)),
                ('inegi_localidad', models.CharField(blank=True, max_length=255)),
                ('inegi_municipio', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Marginacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_inegi', models.CharField(blank=True, max_length=255)),
                ('cod_estado', models.CharField(blank=True, max_length=255)),
                ('estado', models.CharField(blank=True, max_length=255)),
                ('cod_municipio', models.CharField(blank=True, max_length=255)),
                ('municipio', models.CharField(blank=True, max_length=255)),
                ('cod_localidad', models.CharField(blank=True, max_length=255)),
                ('localidad', models.CharField(blank=True, max_length=255)),
                ('poblacion_total', models.IntegerField()),
                ('viviendas_particulares', models.IntegerField()),
                ('analfabeta', models.IntegerField()),
                ('sin_primaria', models.IntegerField()),
                ('sin_excusado', models.IntegerField()),
                ('sin_energia_electrica', models.IntegerField()),
                ('sin_agua_entubada', models.IntegerField()),
                ('ocupantes_por_cuarto', models.IntegerField()),
                ('sin_piso_tierra', models.IntegerField()),
                ('sin_refrigerador', models.IntegerField()),
                ('indice_marginacion_2010', models.IntegerField()),
                ('grado_marginacion', models.CharField(blank=True, max_length=255)),
                ('indice_marginacion', models.IntegerField()),
                ('lugar_en_nacional', models.IntegerField()),
                ('lugar_en_estatal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_embarcacion', models.CharField(blank=True, max_length=255)),
                ('tipo_permiso', models.CharField(blank=True, max_length=255)),
                ('estado', models.CharField(blank=True, max_length=255)),
                ('municipio', models.CharField(blank=True, max_length=255)),
                ('localidad', models.CharField(blank=True, max_length=255)),
                ('area', models.CharField(blank=True, max_length=255)),
                ('rnpa', models.CharField(blank=True, max_length=255)),
                ('titular', models.CharField(blank=True, max_length=255)),
                ('especie', models.CharField(blank=True, max_length=255)),
                ('inicio', models.CharField(blank=True, max_length=255)),
                ('termino', models.CharField(blank=True, max_length=255)),
                ('inegi_localidad', models.CharField(blank=True, max_length=255)),
                ('inegi_municipio', models.CharField(blank=True, max_length=255)),
                ('beneficiario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='permisos', to='api.Beneficiario')),
            ],
        ),
        migrations.AddField(
            model_name='activo',
            name='beneficiario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activos', to='api.Beneficiario'),
        ),
    ]

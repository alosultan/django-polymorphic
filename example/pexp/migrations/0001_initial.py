# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-10-23 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import polymorphic.showfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model2A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModelA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(polymorphic.showfields.ShowFieldTypeAndContent, models.Model),
        ),
        migrations.CreateModel(
            name='nModelA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=(polymorphic.showfields.ShowFieldContent, models.Model),
        ),
        migrations.CreateModel(
            name='ProxyBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_pexp.proxybase_set+', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='UUIDModelA',
            fields=[
                ('uuid_primary_key', models.UUIDField(primary_key=True, serialize=False)),
                ('field1', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(polymorphic.showfields.ShowFieldTypeAndContent, models.Model),
        ),
        migrations.CreateModel(
            name='ArtProject',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.Project')),
                ('artist', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('pexp.project',),
        ),
        migrations.CreateModel(
            name='Model2B',
            fields=[
                ('model2a_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.Model2A')),
                ('field2', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('pexp.model2a',),
        ),
        migrations.CreateModel(
            name='ModelB',
            fields=[
                ('modela_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.ModelA')),
                ('field2', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('pexp.modela',),
        ),
        migrations.CreateModel(
            name='nModelB',
            fields=[
                ('nmodela_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.nModelA')),
                ('field2', models.CharField(max_length=10)),
            ],
            bases=('pexp.nmodela',),
        ),
        migrations.CreateModel(
            name='ResearchProject',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.Project')),
                ('supervisor', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('pexp.project',),
        ),
        migrations.CreateModel(
            name='UUIDModelB',
            fields=[
                ('uuidmodela_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.UUIDModelA')),
                ('field2', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('pexp.uuidmodela',),
        ),
        migrations.AddField(
            model_name='uuidmodela',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_pexp.uuidmodela_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='project',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_pexp.project_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='modela',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_pexp.modela_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='model2a',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_pexp.model2a_set+', to='contenttypes.ContentType'),
        ),
        migrations.CreateModel(
            name='ProxyA',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pexp.proxybase',),
        ),
        migrations.CreateModel(
            name='ProxyB',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pexp.proxybase',),
        ),
        migrations.CreateModel(
            name='Model2C',
            fields=[
                ('model2b_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.Model2B')),
                ('field3', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('pexp.model2b',),
        ),
        migrations.CreateModel(
            name='ModelC',
            fields=[
                ('modelb_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.ModelB')),
                ('field3', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('pexp.modelb',),
        ),
        migrations.CreateModel(
            name='nModelC',
            fields=[
                ('nmodelb_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.nModelB')),
                ('field3', models.CharField(max_length=10)),
            ],
            bases=('pexp.nmodelb',),
        ),
        migrations.CreateModel(
            name='UUIDModelC',
            fields=[
                ('uuidmodelb_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pexp.UUIDModelB')),
                ('field3', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('pexp.uuidmodelb',),
        ),
    ]
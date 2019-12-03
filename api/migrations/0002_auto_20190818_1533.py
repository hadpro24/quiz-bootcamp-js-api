# Generated by Django 2.2.4 on 2019-08-18 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='answer',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='quiz/'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, unique=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='api.Quiz')),
            ],
        ),
    ]

# Generated by Django 2.1 on 2023-09-18 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('about', models.TextField()),
                ('date', models.DateTimeField()),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('about', models.TextField()),
                ('is_public', models.BooleanField(default=False)),
                ('pic', models.ImageField(default='media/forums/Dragonfruit2.jpg', upload_to='forums')),
            ],
        ),
        migrations.CreateModel(
            name='JoinReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.Forum')),
            ],
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('about', models.TextField()),
                ('forum', models.ManyToManyField(related_name='notices', to='forums.Forum')),
            ],
        ),
    ]

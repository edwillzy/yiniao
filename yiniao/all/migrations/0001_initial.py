# Generated by Django 3.0.6 on 2021-02-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DY',
            fields=[
                ('xm', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('rdsj', models.CharField(max_length=32)),
                ('jsr', models.CharField(max_length=32)),
                ('szzb', models.CharField(max_length=32)),
                ('zzsj', models.CharField(max_length=32)),
                ('xzzb', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='HJQK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jxjc', models.CharField(max_length=32)),
                ('jllb', models.CharField(max_length=32)),
                ('cgmc', models.CharField(max_length=32)),
                ('hjr', models.CharField(max_length=32)),
                ('hjrs', models.CharField(max_length=32)),
                ('fzjg', models.CharField(max_length=32)),
                ('hjrq', models.CharField(max_length=32)),
                ('hjjb', models.CharField(max_length=32)),
                ('hjdj', models.CharField(max_length=32)),
                ('hjrymd', models.CharField(max_length=32)),
                ('brwc', models.CharField(max_length=32)),
                ('hjzs', models.FileField(upload_to=None)),
                ('bz', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='HXXM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xmjc', models.CharField(max_length=32)),
                ('fzr', models.CharField(max_length=32)),
                ('xmmc', models.CharField(max_length=32)),
                ('htje', models.CharField(max_length=32)),
                ('qdrq', models.CharField(max_length=32)),
                ('ksrq', models.CharField(max_length=32)),
                ('jhwcrq', models.CharField(max_length=32)),
                ('xmzt', models.CharField(max_length=32)),
                ('qtcy', models.CharField(max_length=32)),
                ('brwc', models.CharField(max_length=32)),
                ('dwmc', models.CharField(max_length=32)),
                ('dz', models.CharField(max_length=32)),
                ('lxrxm', models.CharField(max_length=32)),
                ('lxdh', models.CharField(max_length=32)),
                ('xmhts', models.FileField(upload_to='')),
                ('xmfjhts', models.FileField(upload_to='')),
                ('jtbg', models.FileField(upload_to='')),
                ('xmqtwd', models.FileField(upload_to='')),
                ('bz', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='LW',
            fields=[
                ('lwjc', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('fbsj', models.CharField(max_length=32)),
                ('zzqc', models.CharField(max_length=32)),
                ('zzjc', models.CharField(max_length=32)),
                ('lwtm', models.CharField(max_length=32)),
                ('fbkw', models.CharField(max_length=32)),
                ('qtxx', models.CharField(max_length=32)),
                ('txzz', models.CharField(max_length=32)),
                ('dbz', models.CharField(max_length=32)),
                ('ytxm', models.CharField(max_length=32)),
                ('lwqw', models.FileField(upload_to=None)),
                ('lwsy', models.FileField(upload_to=None)),
                ('lwytxmy', models.FileField(upload_to=None)),
                ('lwfm', models.FileField(upload_to=None)),
                ('lwml', models.FileField(upload_to=None)),
                ('syzm', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='personalInfo',
            fields=[
                ('xm', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('ywqm', models.CharField(max_length=32)),
                ('ywjm', models.CharField(max_length=32)),
                ('xb', models.CharField(max_length=32)),
                ('csrq', models.CharField(max_length=32)),
                ('csd', models.CharField(max_length=32)),
                ('jg', models.CharField(max_length=32)),
                ('zzmm', models.CharField(max_length=32)),
                ('mz', models.CharField(max_length=32)),
                ('gh', models.CharField(max_length=32)),
                ('gzh', models.CharField(max_length=32)),
                ('sfzh', models.CharField(max_length=32)),
                ('zc', models.CharField(max_length=32)),
                ('dzrq', models.CharField(max_length=32)),
                ('xw', models.CharField(max_length=32)),
                ('sydw', models.CharField(max_length=32)),
                ('sysj', models.CharField(max_length=32)),
                ('xl', models.CharField(max_length=32)),
                ('byyx', models.CharField(max_length=32)),
                ('bysj', models.CharField(max_length=32)),
                ('zy', models.CharField(max_length=32)),
                ('cszy', models.CharField(max_length=32)),
                ('ssxk', models.CharField(max_length=32)),
                ('bd', models.CharField(max_length=32)),
                ('sd', models.CharField(max_length=32)),
                ('yjfx', models.CharField(max_length=32)),
                ('xzzw', models.CharField(max_length=32)),
                ('zyshjz', models.CharField(max_length=32)),
                ('lxsj', models.CharField(max_length=32)),
                ('wyyz', models.CharField(max_length=32)),
                ('wysp', models.CharField(max_length=32)),
                ('cjgzsj', models.CharField(max_length=32)),
                ('gzdw', models.CharField(max_length=32)),
                ('jtzz', models.CharField(max_length=32)),
                ('grwz', models.CharField(max_length=32)),
                ('txdz', models.CharField(max_length=32)),
                ('yzbm', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('qq', models.CharField(max_length=32)),
                ('lxdh', models.CharField(max_length=32)),
                ('bgdh', models.CharField(max_length=32)),
                ('yddh', models.CharField(max_length=32)),
                ('ms', models.CharField(max_length=32)),
                ('msdh', models.CharField(max_length=32)),
                ('yczp', models.ImageField(upload_to='')),
                ('eczp', models.ImageField(upload_to='')),
                ('lwzp', models.ImageField(upload_to='')),
                ('grjlCT', models.FileField(upload_to='')),
                ('grjlC', models.FileField(upload_to='')),
                ('grjlET', models.FileField(upload_to='')),
                ('grjlE', models.FileField(upload_to='')),
                ('bz', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='QTCG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgjc', models.CharField(max_length=32)),
                ('cglb', models.CharField(max_length=32)),
                ('cgmc', models.CharField(max_length=32)),
                ('hdsj', models.CharField(max_length=32)),
                ('bfbm', models.CharField(max_length=32)),
                ('cgbh', models.CharField(max_length=32)),
                ('zzxx', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
                ('dzwd', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='RJZZQ',
            fields=[
                ('zzqjc', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('sqr', models.CharField(max_length=32)),
                ('zzqmc', models.CharField(max_length=32)),
                ('zzqbh', models.CharField(max_length=32)),
                ('djh', models.CharField(max_length=32)),
                ('hdsj', models.CharField(max_length=32)),
                ('zzqr', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
                ('zzqzs', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='RYCH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hdz', models.CharField(max_length=32)),
                ('hdsj', models.CharField(max_length=32)),
                ('chmc', models.CharField(max_length=32)),
                ('jb', models.CharField(max_length=32)),
                ('pzjg', models.CharField(max_length=32)),
                ('brwc', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
                ('ryzs', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='WDXS',
            fields=[
                ('zwxm', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('ywqm', models.CharField(max_length=32)),
                ('ywjm', models.CharField(max_length=32)),
                ('xb', models.CharField(max_length=32)),
                ('xh', models.CharField(max_length=32)),
                ('csrq', models.CharField(max_length=32)),
                ('xxfs', models.CharField(max_length=32)),
                ('rxrq', models.CharField(max_length=32)),
                ('bylwtm', models.CharField(max_length=32)),
                ('xwlb', models.CharField(max_length=32)),
                ('yjfx', models.CharField(max_length=32)),
                ('ds', models.CharField(max_length=32)),
                ('fds', models.CharField(max_length=32)),
                ('xslx', models.CharField(max_length=32)),
                ('lxdh', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('sfzh', models.CharField(max_length=32)),
                ('byrq', models.CharField(max_length=32)),
                ('byqx', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='YSJB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zdmc', models.CharField(max_length=32)),
                ('hy', models.CharField(max_length=32)),
                ('qx', models.CharField(max_length=32)),
                ('tyc', models.CharField(max_length=32)),
                ('zdsx', models.CharField(max_length=32)),
                ('qzfw', models.CharField(max_length=32)),
                ('jsgs', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ZL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zljc', models.CharField(max_length=32)),
                ('dywfmr', models.CharField(max_length=32)),
                ('fmmc', models.CharField(max_length=32)),
                ('zllx', models.CharField(max_length=32)),
                ('zlfw', models.CharField(max_length=32)),
                ('zlzt', models.CharField(max_length=32)),
                ('sqh', models.CharField(max_length=32)),
                ('zlsqr', models.CharField(max_length=32)),
                ('sqggr', models.CharField(max_length=32)),
                ('sqggh', models.CharField(max_length=32)),
                ('qtfmr', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
                ('zlsltzswjm', models.CharField(max_length=32)),
                ('zlzs', models.FileField(upload_to=None)),
                ('qtwd', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='ZXXM',
            fields=[
                ('xmjc', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('fzr', models.CharField(max_length=32)),
                ('xmmc', models.CharField(max_length=32)),
                ('xmjb', models.CharField(max_length=32)),
                ('xmbh', models.CharField(max_length=32)),
                ('xmlydw', models.CharField(max_length=32)),
                ('xmlb', models.CharField(max_length=32)),
                ('xmjf', models.CharField(max_length=32)),
                ('lxrq', models.CharField(max_length=32)),
                ('kssj', models.CharField(max_length=32)),
                ('jhwcrq', models.CharField(max_length=32)),
                ('xmzqtcy', models.CharField(max_length=32)),
                ('xmsqs', models.FileField(upload_to=None)),
                ('lxpzs', models.FileField(upload_to=None)),
                ('qtwd', models.FileField(upload_to=None)),
                ('bz', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ZZ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zzjc', models.CharField(max_length=32)),
                ('zzmc', models.CharField(max_length=32)),
                ('cbsj', models.CharField(max_length=32)),
                ('cbd', models.CharField(max_length=32)),
                ('zzlb', models.CharField(max_length=32)),
                ('zzs', models.CharField(max_length=32)),
                ('yz', models.CharField(max_length=32)),
                ('cbdw', models.CharField(max_length=32)),
                ('zzxx', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
                ('dzwd', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='ZCJL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xm', models.CharField(max_length=32)),
                ('sj', models.CharField(max_length=32)),
                ('zc', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
            ],
            options={
                'unique_together': {('xm', 'sj')},
            },
        ),
        migrations.CreateModel(
            name='WDJX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xm', models.CharField(max_length=32)),
                ('qzsj', models.CharField(max_length=32)),
                ('jskc', models.CharField(max_length=32)),
                ('xsrs', models.IntegerField()),
                ('xsjb', models.CharField(max_length=32)),
                ('skxs', models.CharField(max_length=32)),
                ('gzl', models.CharField(max_length=32)),
                ('gzlhj', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
            ],
            options={
                'unique_together': {('xm', 'qzsj', 'jskc')},
            },
        ),
        migrations.CreateModel(
            name='JYJL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xm', models.CharField(max_length=32)),
                ('qzsj', models.CharField(max_length=32)),
                ('xx', models.CharField(max_length=32)),
                ('xl', models.CharField(max_length=32)),
                ('xw', models.CharField(max_length=32)),
                ('sxzy', models.CharField(max_length=32)),
                ('ds', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
            ],
            options={
                'unique_together': {('xm', 'qzsj')},
            },
        ),
        migrations.CreateModel(
            name='GZJL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xm', models.CharField(max_length=32)),
                ('qzsj', models.CharField(max_length=32)),
                ('gzdw', models.CharField(max_length=32)),
                ('zw', models.CharField(max_length=32)),
                ('cdrw', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=32)),
            ],
            options={
                'unique_together': {('xm', 'qzsj')},
            },
        ),
    ]

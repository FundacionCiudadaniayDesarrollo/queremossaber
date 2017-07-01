# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'preguntaTemporal'
        db.create_table(u'solicitudes_preguntatemporal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.TextField')()),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('token', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, blank=True)),
        ))
        db.send_create_signal(u'solicitudes', ['preguntaTemporal'])

        # Adding model 'Categoria'
        db.create_table(u'solicitudes_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('color', self.gf('colorfield.fields.ColorField')(max_length=10)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='nombre', unique_with=())),
        ))
        db.send_create_signal(u'solicitudes', ['Categoria'])

        # Adding model 'Solicitud'
        db.create_table(u'solicitudes_solicitud', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('pregunta', self.gf('django.db.models.fields.TextField')()),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['solicitudes.Categoria'], null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('publicado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=100, populate_from='pregunta', unique_with=())),
        ))
        db.send_create_signal(u'solicitudes', ['Solicitud'])

        # Adding M2M table for field seguidores on 'Solicitud'
        m2m_table_name = db.shorten_name(u'solicitudes_solicitud_seguidores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('solicitud', models.ForeignKey(orm[u'solicitudes.solicitud'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['solicitud_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'preguntaTemporal'
        db.delete_table(u'solicitudes_preguntatemporal')

        # Deleting model 'Categoria'
        db.delete_table(u'solicitudes_categoria')

        # Deleting model 'Solicitud'
        db.delete_table(u'solicitudes_solicitud')

        # Removing M2M table for field seguidores on 'Solicitud'
        db.delete_table(db.shorten_name(u'solicitudes_solicitud_seguidores'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'solicitudes.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'color': ('colorfield.fields.ColorField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'nombre'", 'unique_with': '()'})
        },
        u'solicitudes.preguntatemporal': {
            'Meta': {'object_name': 'preguntaTemporal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pregunta': ('django.db.models.fields.TextField', [], {}),
            'token': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'solicitudes.solicitud': {
            'Meta': {'object_name': 'Solicitud'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['solicitudes.Categoria']", 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'pregunta': ('django.db.models.fields.TextField', [], {}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'seguidores': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'usuarios_seguidores'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '100', 'populate_from': "'pregunta'", 'unique_with': '()'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['solicitudes']
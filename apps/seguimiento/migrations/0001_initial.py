# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Estado'
        db.create_table(u'seguimiento_estado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('color', self.gf('colorfield.fields.ColorField')(max_length=10)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='nombre', unique_with=())),
        ))
        db.send_create_signal(u'seguimiento', ['Estado'])

        # Adding model 'Seguimiento'
        db.create_table(u'seguimiento_seguimiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['solicitudes.Solicitud'])),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seguimiento.Estado'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('comentario', self.gf('django.db.models.fields.TextField')()),
            ('documento', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'seguimiento', ['Seguimiento'])


    def backwards(self, orm):
        # Deleting model 'Estado'
        db.delete_table(u'seguimiento_estado')

        # Deleting model 'Seguimiento'
        db.delete_table(u'seguimiento_seguimiento')


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
        u'seguimiento.estado': {
            'Meta': {'object_name': 'Estado'},
            'color': ('colorfield.fields.ColorField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'nombre'", 'unique_with': '()'})
        },
        u'seguimiento.seguimiento': {
            'Meta': {'object_name': 'Seguimiento'},
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'documento': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seguimiento.Estado']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['solicitudes.Solicitud']"})
        },
        u'solicitudes.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'color': ('colorfield.fields.ColorField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'nombre'", 'unique_with': '()'})
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

    complete_apps = ['seguimiento']
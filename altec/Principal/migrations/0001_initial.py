# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Persona'
        db.create_table(u'Principal_persona', (
            ('identificacion', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Apellido', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'Principal', ['Persona'])

        # Adding model 'Cliente'
        db.create_table(u'Principal_cliente', (
            ('identificacion', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Apellido', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('tipo_cliente', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')()),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'Principal', ['Cliente'])

        # Adding model 'Tecnico'
        db.create_table(u'Principal_tecnico', (
            ('identificacion', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Apellido', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('tipo_tecnico', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')()),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'Principal', ['Tecnico'])

        # Adding model 'orden_servicio'
        db.create_table(u'Principal_orden_servicio', (
            ('numero_orden', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('id_cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Principal.Cliente'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('motivo', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('problema', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('actividad', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('observacion_tecnico', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('observacion_cliente', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('hora_entrada', self.gf('django.db.models.fields.TimeField')()),
            ('hora_salida', self.gf('django.db.models.fields.TimeField')()),
            ('responsable', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'Principal', ['orden_servicio'])


    def backwards(self, orm):
        # Deleting model 'Persona'
        db.delete_table(u'Principal_persona')

        # Deleting model 'Cliente'
        db.delete_table(u'Principal_cliente')

        # Deleting model 'Tecnico'
        db.delete_table(u'Principal_tecnico')

        # Deleting model 'orden_servicio'
        db.delete_table(u'Principal_orden_servicio')


    models = {
        u'Principal.cliente': {
            'Apellido': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'Meta': {'object_name': 'Cliente'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'identificacion': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_cliente': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Principal.orden_servicio': {
            'Meta': {'object_name': 'orden_servicio'},
            'actividad': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'hora_entrada': ('django.db.models.fields.TimeField', [], {}),
            'hora_salida': ('django.db.models.fields.TimeField', [], {}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Principal.Cliente']"}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'numero_orden': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'observacion_cliente': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'observacion_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'problema': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'responsable': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'Principal.persona': {
            'Apellido': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'Meta': {'object_name': 'Persona'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'identificacion': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'Principal.tecnico': {
            'Apellido': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'Meta': {'object_name': 'Tecnico'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'identificacion': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Principal']
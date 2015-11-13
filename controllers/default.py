# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################


	

from datetime import datetime


def index():
    

    if "ultima_fecha" not in session:
        session.ultima_fecha='1/1/1999 0:0:0'

    # dia= session.ultima_fecha.split("/")[0]
    # mes= session.ultima_fecha.split("/")[1]
    # year = session.ultima_fecha.split("/")[2].split(" ")[0]
    # fecha_buscar = year + "-" + mes + "-" + dia
    
    formato_fecha = T("%Y-%m-%d %H:%M:%S", lazy=False)
    fecha_object = datetime.strptime(session.ultima_fecha, formato_fecha)
    fecha_buscar = datetime.strftime(fecha_object,"%Y-%m-%d")
    consulta = db.lecturas.fecha >= fecha_buscar

    #fila_senal = db(db.tags.nombre=="Q1").select().first()
    #if fila_senal:
    #    tag_id = fila_senal.id
    #else:
    #    tag_id = 0
    
    #consulta = db.lecturas.tag == tag_id
    
    rejilla = SQLFORM.grid(consulta,  searchable=False, 
    details=False, csv=False)
    
    
    form=FORM('Fecha inicio:',
     INPUT(_name='fecha',_class="datetime",),
     INPUT(_name='otro',_value="33"),
     INPUT(_type='submit', _value="Mirar"))
     
    if form.accepts(request,session):
        #response.flash = 'has mandado una fecha'
        session.ultima_fecha = request.vars.fecha
        #redirect(URL("default", "index"))
        
        

             
    return dict(lecturas=rejilla, form=form)


def etiquetas():
    
    rejilla = SQLFORM.grid(db.tags,details=False, csv=False)

    return dict(lecturas=rejilla)
    
    
def valoresuna():
    etiqueta=db(db.tags.nombre=="Q1").select().first()
    
    # db(db.tags.nombre=="Q1").delete()
    etiqueta.direccion="blblabl"
    db.commit()
    
    
    
    filas = db(db.lecturas.tag == etiqueta.id).select()
    
    
    return dict(datos=filas, fila=etiqueta)



def valoresparom1():
    etiqueta=db(db.tags.nombre=="ParoM1").select().first()
    
    filas = db(db.lecturas.tag == etiqueta.id).select()
    
    
    return dict(datos=filas)
    


def grafica():
    # Ejemplo con json
    return dict()


def valores():
    filas = db(db.lecturas.fecha <= '2008-01-04').select()
    
    return dict(filas=filas)

    

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()



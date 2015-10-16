# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
@auth.requires_login()
def index():
    
    rejilla = SQLFORM.grid(db.lecturas,  searchable=False, 
    details=False, csv=False)

    return dict(lecturas=rejilla)


@auth.requires_login()
def etiquetas():
    
    rejilla = SQLFORM.grid(db.tags,details=False, csv=False)

    return dict(lecturas=rejilla)
    
    
def valoresuna():
    etiqueta=db(db.tags.nombre=="Q1").select().first()
    
    filas = db(db.lecturas.tag == etiqueta.id).select()
    
    
    return dict(datos=filas)



def valoresparom1():
    etiqueta=db(db.tags.nombre=="ParoM1").select().first()
    
    filas = db(db.lecturas.tag == etiqueta.id).select()
    
    
    return dict(datos=filas)
    
    


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



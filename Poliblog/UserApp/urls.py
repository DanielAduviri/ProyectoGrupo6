from django.urls import path
from UserApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="inicio"),
   # path('padre', views.padre, name="padre"),
    path('login', views.Login, name="inicioSesion"),
    path('registro', views.register, name="registro"),
    path('logout', LogoutView.as_view(next_page="inicioSesion"), name="Logout"),
    path('login2', views.login2, name="login2"),
    path('perfil', views.verPerfil, name="Perfil"),
    path('perfil2', views.perfil2, name="perfil2"),
    path('editarPerfil', views.UserEditForm, name="editarPerfil"),
    #path('login2', views.Login2, name="login2"),
    
    path('Posteos/<id>', views.verPosteos, name="Posteos"),
    path('buscarPosteos', views.buscarPosteos, name="buscarPosteos"),
    path('busquedaPosteos', views.busquedaPosteos, name="busquedaPosteos"),
    path('comentarios/<id>', views.verComentarios, name="comentarios"),
    path('crearPost',views.CrearPost, name ="crearPost"),

    path('leerPosts/', views.leerposts, name="leerPosts"),
    path('listaPost', views.listaPost.as_view(), name='listaPost'),
    path('actualizaPost/<pk>/', views.actualizaPost.as_view(), name='actualizaPost'),
    path('eliminaPost/<pk>/', views.eliminaPost.as_view(), name='eliminaPost'),
    
    path('Tematicas', views.verTematicas, name="tematicas"),
    path('tematicasList', views.TematicaList.as_view(), name="tematicasList"),
    path('tematicasDetail/<pk>',views.TematicaDetail.as_view(), name="tematicasDetail"),
    path('tematicasUpdate/<pk>',views.TematicaUpdate.as_view(), name="tematicasUpdate"),
    path('tematicasDelete/<pk>',views.TematicaDelete.as_view(), name="tematicasDelete"),
    path('tematicasCreate',views.TematicaCreate.as_view(), name="tematicasCreate"),

    path('crearTematica',views.CrearTematica, name="crearTematica"),
    path('buscarTematicas', views.buscarTematicas, name="buscarTematicas"),
    path('eliminarTematicas/<id_tematica>',views.eliminarTematicas, name="eliminarTematicas"),
    path('editarTematicas/<id_tematica>',views.editarTematicas, name= 'editarTematicas'),
    
    path('crearLenguajes', views.LenguajeCreate.as_view(), name='New'),
    #path('PostView', views.CantViewPost.as_view(), name="VistasPost")
]

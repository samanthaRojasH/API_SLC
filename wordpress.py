from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts

usuario = "sandrarojasherran"
contraseña = "Admin9876*+"
sitio = "https://ettogether.wordpress.com/xmlrpc.php" #Recuerda que debes llamar al archivo xmlrpc.php
cliente = Client(sitio, usuario, contraseña)
datos_usuario = cliente.call(GetUserInfo())
print("Tu nombre de usuario es {}".format(datos_usuario))

entradas = cliente.call(posts.GetPosts())
if len(entradas) > 0:
    for entrada in entradas:
        print(entrada)
else:
    print("No hay entradas para mostrar")
# Introduzione

Esempio di Kuberneetes (*Minikube*), con due applicativi che comunicano tra di loro in ottica di Microservizi. Al momento non è Kuberneetes puro.

1. **Avvio Minikube:** *minikube start* 
2. **Entro nel coontesto di minikube:** *eval $(minikube docker-env)*
3. **Effettuo la build dei vari container che mi servono:** *docker build -t hellonode:v1 .*
4. **Avvio il tunnel:** *minikube tunnel*
5. **Avvio la dashboard:** *minikube dashboard*

# Da fare

1. Sistemare il discorso delle porte con tipo *LoadBalancer*, visto che in questo modo è solamente accesso locale
2. Provare a fare il Deploy su AWS
3. Capire un po come funziona Docker e Kuberneetes

# Link utili

https://medium.com/@felipedutratine/kubernetes-on-local-with-minikube-tutorial-413475d587e6

https://stackoverflow.com/questions/46180814/how-to-connect-to-minikube-services-from-outside

https://stackoverflow.com/questions/53105262/cant-access-service-in-my-local-kubernetes-cluster-using-nodeport

https://stackoverflow.com/questions/55462654/cant-access-minikube-loadbalancer-service-from-host-machine

https://stackoverflow.com/questions/40144138/pull-a-local-image-to-run-a-pod-in-kubernetes

https://stackoverflow.com/questions/46245508/how-create-service-on-minikube-with-yaml-configuration-which-accessible-from-hos

https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube

https://stackoverflow.com/questions/882712/sending-html-email-using-python

https://stackoverflow.com/questions/20212894/how-do-i-get-flask-to-run-on-port-80

https://stackoverflow.com/questions/41322541/rebuild-docker-container-on-file-changes

https://stackoverflow.com/questions/48077931/delete-all-the-contents-from-a-kubernetes-node
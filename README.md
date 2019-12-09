# Introduzione

Esempio di Kuberneetes (Minikube), con due applicativi che comunicano tra di loro in ottica di Microservizi. Al momento non è Kuberneetes puro.

1. Entro nel coontesto di minikube: eval $(minikube docker-env)
2. Effettuo la build dei vari container che mi servono: docker build -t hellonode:v1 .
3. Avvio il tunnel: minikube tunnel
4. Avvio la dashboard: minikube dashboard

# Da fare

Sistemare il loaad balancer, provare su AWS ecc.
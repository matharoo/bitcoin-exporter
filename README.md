# bitcoin-exporter

## Deploying deployment.yaml
```
kubectl create ns wix
kubectl apply -f deployment.yaml
# to test if deployment is working
kubectl port-forward deployment/bitcoin-exporter 8000:8000 -n wix
# go to browser and try localhost:8000 it should return metrics.
```

## Deploying service.yaml
```
kubectl apply -f service.yaml
# to test if service is working
kubectl port-forward svc/bitcoin-exporter 8000:8000 -n wix
# go to browser and try localhost:8000 it should return metrics.
```

## Deploying ingress-nginx
```
helm upgrade --install ingress-nginx ingress-nginx \                                 
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```

## Deploying prometheus using helm
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm upgrade --install prometheus prometheus-community/prometheus -f values.yaml -n wix
```
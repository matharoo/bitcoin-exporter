# bitcoin-exporter

## Building dockerfile and creating the image
```
docker build -t bitcoin-exporter:1.0.0 .
# now you should have an image bitcoin-exporter with tag 1.0.0
```
## Create a namespace wix and
```
kubectl create ns wix
```

## Deploying deployment.yaml
```
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

## Deploying ingress-nginx into its own namespace ingress-nginx
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

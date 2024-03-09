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
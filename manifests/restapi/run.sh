#!/usr/bin/bash
kubectl apply -f ns.yaml 
kubectl apply -f secret.yaml
kubectl apply -f configmap.yaml 
kubectl apply -f restapi.yaml
kubectl apply -f service.yaml


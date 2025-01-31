# Kubernetes Commands Cheat Sheet

## Namespaces
```bash
# List all namespaces
kubectl get namespaces

# Shorter version
kubectl get ns

# Describe a specific namespace
kubectl describe namespace <namespace-name>

# Filter namespaces by label
kubectl get namespaces -l <label-key>=<label-value>

# Set default namespace for current context
kubectl config set-context --current --namespace=<namespace-name>

# List all pods in the current namespace
kubectl get pods

# List all pods across all namespaces
kubectl get pods --all-namespaces

# List pods in a specific namespace
kubectl get pods -n <namespace-name>

# View detailed info for a specific pod
kubectl describe pod <pod-name> -n <namespace-name>

# View logs for a pod's container
kubectl logs <pod-name> -n <namespace-name>

# For multi-container pods
kubectl logs <pod-name> -n <namespace-name> -c <container-name>

# Filter pods by label
kubectl get pods -l <label-key>=<label-value> -n <namespace-name>

# Monitor pods in real-time
kubectl get pods -w

# Show which nodes pods are running on
kubectl get pods -o wide

# List all deployments
kubectl get deployments

# Describe a deployment
kubectl describe deployment <deployment-name>

# Scale a deployment
kubectl scale deployment <deployment-name> --replicas=<number>

# Rolling restart of a deployment
kubectl rollout restart deployment <deployment-name>

# View rollout status
kubectl rollout status deployment <deployment-name>

# Undo last deployment rollout
kubectl rollout undo deployment <deployment-name>

# List all services
kubectl get services

# Describe a specific service
kubectl describe service <service-name>

# Expose a deployment as a service
kubectl expose deployment <deployment-name> --type=LoadBalancer --port=80 --target-port=8080

# Create a ConfigMap from a file
kubectl create configmap <configmap-name> --from-file=<file-path>

# List ConfigMaps
kubectl get configmaps

# Describe a ConfigMap
kubectl describe configmap <configmap-name>

# Create a Secret from a file
kubectl create secret generic <secret-name> --from-file=<file-path>

# List Secrets
kubectl get secrets

# Describe a Secret
kubectl describe secret <secret-name>

# List all nodes
kubectl get nodes

# Describe a specific node
kubectl describe node <node-name>

# Cordon a node (prevent scheduling)
kubectl cordon <node-name>

# Uncordon a node (allow scheduling)
kubectl uncordon <node-name>

# Drain a node (evict all pods)
kubectl drain <node-name> --ignore-daemonsets

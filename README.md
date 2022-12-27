# ASCN TP 2022

- Criar cluster
`ansible-playbook create-gke-cluster.yml -i inventory/gcp.yml`

- Dar deploy de ghost 
`ansible-playbook deploy-ghost.yml -i inventory/gcp.yml`

- Destruir cluster
`ansible-playbook destroy-gke-cluster -i inventory/gcp.yml`



## Exemplo de um ficheiro secret.yml
```
apiVersion: v1
kind: Secret
metadata:
  name: ghost-data
  namespace: ghost_namespace
type: Opaque
data:
  password: UGFzc3dvcmQkMTIzNDU2 # Password$123456
  root_password: UGFzc3dvcmQkMTIzNDU2 # Password$123456
```

## Ver erros
- Ver o nome do pod
`kubectl get pods`
- Ver qual é o problema
`kubectl logs <nome_do_pod>`

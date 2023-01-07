# ASCN TP 2022

- Criar cluster
`ansible-playbook create-gke-cluster.yml -i inventory/gcp.yml`

- Dar deploy de ghost 
`ansible-playbook deploy-ghost.yml -i inventory/gcp.yml`

- Destruir cluster
`ansible-playbook destroy-gke-cluster -i inventory/gcp.yml`

## Ver erros

- Ver o nome do pod
`kubectl get pods`
- Ver qual é o problema
`kubectl logs <nome_do_pod>`

# ASCN TP 2022

- Criar cluster
`ansible-playbook create-gke-cluster.yml -i inventory/gcp.yml --ask-vault-pass`

- Dar deploy de ghost 
`ansible-playbook deploy-ghost.yml -i inventory/gcp.yml --ask-vault-pass`

- Destruir cluster
`ansible-playbook destroy-gke-cluster.yml -i inventory/gcp.yml --ask-vault-pass`


- Testar Ghost
`ansible-playbook test-all.yml -i inventory/gcp.yml --ask-vault-pass`

## Ver erros

- Ver o nome do pod
`kubectl get pods`
- Ver qual é o problema
`kubectl logs <nome_do_pod>`
